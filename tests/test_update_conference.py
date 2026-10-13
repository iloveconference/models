"""Test cases for the update_conference module.

Everything here is offline. The pieces that would touch a network - Pinecone, the
website, and the voyage-backed splitter - are replaced with fakes whose upsert and
delete methods fail the test if they are ever called, so a dry run that quietly wrote
something would be a red test rather than a production incident.
"""

import ast
import json
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any
from typing import Iterator
from typing import Optional
from typing import Sequence

import click
import numpy as np
import pytest
from click.testing import CliRunner
from pinecone.errors import ApiError
from pinecone.errors import ForbiddenError

from models import update_conference as uc
from models.document import Document
from models.split_utils import clean_text


HOST = "https://www.churchofjesuschrist.org"
TALK_COUNT = 33
CHUNKS_PER_TALK = 4


# --- pure helpers -----------------------------------------------------------------------


@pytest.mark.parametrize(("given", "expected"), [("4", "04"), ("04", "04"), ("10", "10"), (" 10 ", "10")])
def test_normalize_month_pads(given: str, expected: str) -> None:
    """It accepts an unpadded month and zero-pads it.

    Args:
        given: the raw option value.
        expected: the normalized month.
    """
    assert uc._normalize_month(None, None, given) == expected  # type: ignore[arg-type]


@pytest.mark.parametrize("given", ["7", "01", "", "oct", "100"])
def test_normalize_month_rejects_non_conference_months(given: str) -> None:
    """It refuses any month General Conference is not held in.

    Args:
        given: the raw option value.
    """
    with pytest.raises(click.BadParameter, match="must be 04 or 10"):
        uc._normalize_month(None, None, given)  # type: ignore[arg-type]


def test_is_talk_url_accepts_a_real_talk() -> None:
    """It accepts the shape the 2025-10 listing actually links."""
    assert uc.is_talk_url(f"{HOST}/study/general-conference/2025/10/11christofferson?lang=eng", 2025, "10")


@pytest.mark.parametrize(
    "url",
    [
        f"{HOST}/study/general-conference/2025/10/saturday-morning-session?lang=eng",
        f"{HOST}/study/scriptures/bofm/alma/5?lang=eng",
        f"{HOST}/study/general-conference/2025/10/11christofferson?lang=spa",
        f"{HOST}/study/general-conference/2025/10/11christofferson",
        f"{HOST}/study/general-conference/2025/10/?lang=eng",
        f"{HOST}/study/general-conference/2025/04/11christofferson?lang=eng",
        f"{HOST}/study/general-conference/2025/10/11christofferson/extra?lang=eng",
        "https://evil.example.com/study/general-conference/2025/10/11x?lang=eng",
    ],
)
def test_is_talk_url_rejects_everything_else(url: str) -> None:
    """It rejects session pages, scriptures, other languages, other conferences, and other hosts.

    The scripture case is the dangerous one: six path components, no "-session" suffix, so
    the original predicate accepted it and it would have indexed as year="bofm".

    Args:
        url: a url that must not be crawled for 2025-10.
    """
    assert not uc.is_talk_url(url, 2025, "10")


def test_canonical_url_drops_fragments_and_normalizes_the_query() -> None:
    """It produces the byte-exact url form the index stores, because get_doc_id hashes it."""
    messy = f"{HOST}/study/general-conference/2025/10/11x?lang=eng&foo=1#p7"
    assert uc.canonical_url(messy) == f"{HOST}/study/general-conference/2025/10/11x?lang=eng"


def test_talk_stem_matches_the_notebook_convention() -> None:
    """It names files exactly as notebook 05 did, so data/update stays interchangeable."""
    assert uc.talk_stem(f"{HOST}/study/general-conference/2026/10/11christofferson?lang=eng") == (
        "2026-10-11christofferson"
    )


def test_talk_stem_refuses_a_traversing_slug() -> None:
    """It refuses to build a path that could escape the data directory."""
    with pytest.raises(ValueError):
        uc.talk_stem(f"{HOST}/study/general-conference/2025/10/..?lang=eng")


def test_batch_bounds_covers_every_item_once() -> None:
    """It partitions a count into contiguous half-open ranges."""
    assert uc._batch_bounds(250, 100) == [(0, 100), (100, 200), (200, 250)]
    assert uc._batch_bounds(0, 100) == []


# --- the .env parser --------------------------------------------------------------------


def test_read_env_file_skips_a_commented_duplicate(tmp_path: Path) -> None:
    """It takes the live key, not the commented-out development key written just below it.

    This is the single most load-bearing line in rail 2: server/.env really does hold a
    live PINECONE_KEY followed by a commented development key of the same length, and any
    parser that strips a leading "#" before splitting selects the wrong one - after which
    every stage of the run succeeds into an empty project.
    """
    path = tmp_path / ".env"
    path.write_text("PINECONE_KEY=real\n# dev - someone@example.com\n# PINECONE_KEY=fake\n", encoding="utf-8")

    assert uc.read_env_file(path)["PINECONE_KEY"] == "real"


def test_read_env_file_handles_quotes_exports_and_blanks(tmp_path: Path) -> None:
    """It strips surrounding quotes and an "export" prefix, and ignores blank lines."""
    path = tmp_path / ".env"
    path.write_text("\nexport A=\"one\"\nB='two'\nC=three\nnot_a_pair\n", encoding="utf-8")

    assert uc.read_env_file(path) == {"A": "one", "B": "two", "C": "three"}


def test_resolve_pinecone_key_prefers_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """It takes $PINECONE_PROD_KEY ahead of the file.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
    """
    monkeypatch.setenv("PINECONE_PROD_KEY", "from-env")

    assert uc.resolve_pinecone_key() == ("from-env", "$PINECONE_PROD_KEY")


def test_resolve_pinecone_key_ignores_an_empty_environment_variable(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """An exported-but-empty variable is absent, not a key.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
    """
    monkeypatch.setenv("PINECONE_PROD_KEY", "   ")
    sibling = tmp_path / "server" / ".env"
    sibling.parent.mkdir()
    sibling.write_text("PINECONE_KEY=from-file\n", encoding="utf-8")
    monkeypatch.setattr(uc, "SIBLING_ENV", sibling)

    assert uc.resolve_pinecone_key() == ("from-file", "server/.env:PINECONE_KEY")


def test_resolve_pinecone_key_never_falls_back_to_the_dev_key(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """With no production key anywhere it aborts, rather than using models/.env.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
    """
    monkeypatch.delenv("PINECONE_PROD_KEY", raising=False)
    monkeypatch.setenv("PINECONE_API_KEY", "the-dev-key")
    monkeypatch.setattr(uc, "SIBLING_ENV", tmp_path / "nope" / ".env")

    with pytest.raises(uc._Abort) as caught:
        uc.resolve_pinecone_key()
    assert caught.value.code == uc.EXIT_NO_KEY
    assert "the-dev-key" not in caught.value.body


# --- rails that are pure functions --------------------------------------------------------


@pytest.mark.parametrize(("year", "month"), [(2023, "04"), (2015, "10"), (1995, "04")])
def test_era_guard_refuses_the_integer_id_era(year: int, month: str) -> None:
    """It refuses every conference whose vectors have integer ids.

    Args:
        year: the conference year.
        month: the conference month.
    """
    with pytest.raises(uc._Abort) as caught:
        uc.check_era(year, month)
    assert caught.value.code == uc.EXIT_ERA
    assert "--force does not override this" in caught.value.body


@pytest.mark.parametrize(("year", "month"), [(2023, "10"), (2025, "10"), (2026, "04")])
def test_era_guard_allows_the_content_hash_era(year: int, month: str) -> None:
    """It allows 2023-10 and everything after it.

    Args:
        year: the conference year.
        month: the conference month.
    """
    uc.check_era(year, month)


def test_plausible_year_guard_catches_a_typo() -> None:
    """It refuses a year that cannot have had a conference yet."""
    with pytest.raises(uc._Abort) as caught:
        uc.check_plausible_year(2999)
    assert caught.value.code == uc.EXIT_ERA


@pytest.mark.parametrize("count", [0, 14, 29, 61, 400])
def test_talk_count_guard_refuses_a_partial_or_runaway_listing(count: int) -> None:
    """It refuses both a half-published conference and a predicate that matched too much.

    Args:
        count: the talk count to test.
    """
    with pytest.raises(uc._Abort) as caught:
        uc.check_talk_count(count, "the listing", "detail")
    assert caught.value.code == uc.EXIT_TALK_COUNT


@pytest.mark.parametrize("count", [30, 35, 38, 60])
def test_talk_count_guard_allows_every_observed_size(count: int) -> None:
    """It allows the conference sizes that actually occur.

    Args:
        count: the talk count to test.
    """
    uc.check_talk_count(count, "the listing", "detail")


def test_extract_talk_urls_deduplicates_double_linked_talks() -> None:
    """It applies the floor to unique talks: a real listing links every talk twice.

    A count check on the raw match list would pass with half the real talks, which is
    precisely the half-published conference rail 3 exists to catch.
    """
    hrefs = "".join(
        f'<a href="/study/general-conference/2025/10/{n}x?lang=eng">t</a>'
        f'<a href="/study/general-conference/2025/10/{n}x?lang=eng#p1">t again</a>'
        for n in range(5)
    )
    html = f'<html><body>{hrefs}<a href="/study/general-conference/2025/10/sunday-session?lang=eng">s</a></body></html>'

    urls, anchors, matched, near_misses = uc.extract_talk_urls(html, f"{HOST}/x", 2025, "10")

    assert len(urls) == 5
    assert matched == 10
    assert anchors == 11
    assert near_misses == []


def test_check_embeddings_refuses_the_wrong_dimension() -> None:
    """It refuses a vector width the production index cannot hold."""
    with pytest.raises(uc._Abort) as caught:
        uc.check_embeddings([[0.1] * 768, [0.1] * 768], 2)
    assert caught.value.code == uc.EXIT_BAD_EMBEDDINGS


def test_check_embeddings_refuses_non_finite_values() -> None:
    """It refuses NaN, which Pinecone would accept and retrieval would never recover from."""
    with pytest.raises(uc._Abort) as caught:
        uc.check_embeddings([[float("nan")] + [0.1] * (uc.INDEX_DIM - 1)], 1)
    assert caught.value.code == uc.EXIT_BAD_EMBEDDINGS


def test_check_embeddings_accepts_a_correct_batch() -> None:
    """It accepts the shape ada-002 actually returns."""
    uc.check_embeddings([[0.1] * uc.INDEX_DIM, [0.2] * uc.INDEX_DIM], 2)


# --- the single delete call site ------------------------------------------------------------


def test_module_contains_exactly_one_delete_and_never_a_bulk_one() -> None:
    """Deletion protection is disabled on this index, so a stray bulk delete is unrecoverable.

    Parsed rather than grepped, so prose about delete_all in a docstring cannot fail the
    test and a real delete_all cannot hide behind one. Exactly one delete call site, with
    a literal single-element id list, and never delete_all or filter.
    """
    tree = ast.parse(Path(uc.__file__).read_text(encoding="utf-8"))
    deletes = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "delete"
    ]

    assert len(deletes) == 1, f"expected one delete call site, found {len(deletes)}"
    call = deletes[0]
    assert not call.args, "delete must be called with keywords only"
    keywords = {keyword.arg for keyword in call.keywords}
    assert keywords == {"ids", "namespace"}, f"delete must pass only ids and namespace, got {keywords}"
    ids = next(keyword.value for keyword in call.keywords if keyword.arg == "ids")
    assert isinstance(ids, ast.List) and len(ids.elts) == 1, "delete must pass a literal one-element id list"


def test_canary_metadata_has_every_key_the_server_reads() -> None:
    """A metadata-less vector in a live top-20 would 500 the whole /search request."""
    metadata = uc._canary_metadata()

    assert set(metadata) == uc.METADATA_KEYS
    assert all(isinstance(value, str) for value in metadata.values())
    assert (metadata["year"], metadata["month"]) == ("0000", "00")


def test_probe_vector_is_a_unit_vector_of_the_right_width() -> None:
    """The canary's vector must be valid for a cosine index and unable to rank."""
    assert len(uc.PROBE_VECTOR) == uc.INDEX_DIM
    assert abs(sum(value * value for value in uc.PROBE_VECTOR) - 1.0) < 1e-9


# --- the run record -------------------------------------------------------------------------


def _record(tmp_path: Path) -> uc.RunRecord:
    """Build a run record in a temporary directory.

    Args:
        tmp_path: a temporary directory.

    Returns:
        A fresh run record.
    """
    return uc.RunRecord(tmp_path / "run.json", tmp_path / ".tmp")


def test_run_record_round_trips_through_disk(tmp_path: Path) -> None:
    """A stage finished by one invocation is visible to the next.

    Args:
        tmp_path: a temporary directory.
    """
    record = _record(tmp_path)
    record.finish_stage("crawl", "completed", 1.5, talk_urls=["a", "b"])

    reopened = _record(tmp_path)

    assert reopened.data["stages"]["crawl"]["status"] == "completed"
    assert reopened.data["stages"]["crawl"]["talk_urls"] == ["a", "b"]
    assert reopened.data["schema_version"] == uc.SCHEMA_VERSION


def test_run_record_starts_every_stage_not_started(tmp_path: Path) -> None:
    """A new record claims nothing has happened yet.

    Args:
        tmp_path: a temporary directory.
    """
    record = _record(tmp_path)

    assert {name: record.stage(name)["status"] for name in uc.STAGE_NAMES} == {
        name: "not_started" for name in uc.STAGE_NAMES
    }


def _ctx(tmp_path: Path, **overrides: Any) -> uc.Ctx:
    """Build a run context rooted in a temporary directory.

    Args:
        tmp_path: a temporary directory.
        overrides: fields to override.

    Returns:
        A run context.
    """
    options: dict[str, Any] = {
        "delay": 8,
        "dry_run": False,
        "allow_skips": 0,
        "force": False,
        "write_probe": "update",
    }
    options.update(overrides)
    data_dir = tmp_path / "data" / "update" / "2026-10"
    for directory in (data_dir, data_dir / "raw", data_dir / "split", data_dir / ".tmp"):
        directory.mkdir(parents=True, exist_ok=True)
    return uc.Ctx(
        year=2026,
        month="10",
        data_dir=data_dir,
        run=uc.RunRecord(data_dir / "run.json", data_dir / ".tmp"),
        started=0.0,
        **options,
    )


def test_completed_run_is_refused_but_force_overrides(tmp_path: Path) -> None:
    """A finished conference is not re-run by accident, but --force reaches it.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    ctx.run.data["status"] = "completed"

    with pytest.raises(uc._Abort) as caught:
        uc.check_no_completed_run(ctx)
    assert caught.value.code == uc.EXIT_GUARD

    uc.check_no_completed_run(_forced(tmp_path))


def _forced(tmp_path: Path) -> uc.Ctx:
    """Build a forced context whose record says the run completed.

    Args:
        tmp_path: a temporary directory.

    Returns:
        A forced run context.
    """
    ctx = _ctx(tmp_path, force=True)
    ctx.run.data["status"] = "completed"
    return ctx


def test_already_indexed_guard_refuses_a_metadata_hit(tmp_path: Path) -> None:
    """A conference the index already holds is refused.

    Args:
        tmp_path: a temporary directory.
    """
    with pytest.raises(uc._Abort) as caught:
        uc.check_not_already_indexed(_ctx(tmp_path), 1)
    assert caught.value.code == uc.EXIT_ALREADY_INDEXED

    uc.check_not_already_indexed(_ctx(tmp_path), 0)
    uc.check_not_already_indexed(_ctx(tmp_path, force=True), 5)


def test_shard_is_reused_only_when_source_and_code_both_match(tmp_path: Path) -> None:
    """A cached shard is reused only when its input and the pipeline code are unchanged.

    Never "the file exists, therefore skip": that is how half a conference ends up split
    by one version of the code and half by another.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    doc = Document(page_content="the body", metadata={"url": "u"})
    stem = "2026-10-11x"
    (ctx.split_dir / f"{stem}.jsonl").write_text("", encoding="utf-8")
    fingerprint = uc._code_sha256()
    ctx.run.stage("split")["shards"] = {stem: {"source_sha256": uc._sha256("the body"), "fingerprint": fingerprint}}

    assert uc._shard_is_reusable(ctx, stem, doc, fingerprint)
    assert not uc._shard_is_reusable(ctx, stem, doc, "a-different-code-fingerprint")
    assert not uc._shard_is_reusable(ctx, stem, Document(page_content="edited", metadata={"url": "u"}), fingerprint)
    assert not uc._shard_is_reusable(ctx, "2026-10-missing", doc, fingerprint)


# --- the upsert plan ----------------------------------------------------------------------


def _chunk(position: int) -> Document:
    """Build one chunk with the metadata the splitter produces.

    Args:
        position: a number to make the chunk unique.

    Returns:
        A chunk document.
    """
    return Document(
        page_content=f"chunk body {position}",
        metadata={
            "year": "2026",
            "month": "10",
            "url": f"{HOST}/study/general-conference/2026/10/{position}x?lang=eng",
            "title": f"Talk {position}",
            "author": "Elder Someone",
            "author_role": "Of the Quorum",
            "anchor": f"p{position}",
        },
    )


def test_plan_upsert_produces_the_nine_metadata_keys_the_server_reads() -> None:
    """The preview is built by index_documents itself, so it cannot drift from a real run."""
    batches = uc.plan_upsert([_chunk(n) for n in range(3)])

    assert len(batches) == 1
    vector_id, values, metadata = batches[0][0]
    assert set(metadata) == uc.METADATA_KEYS
    assert metadata["source"] == vector_id
    assert metadata["text"] == "chunk body 0"
    assert len(values) == uc.INDEX_DIM


def test_plan_upsert_batches_at_one_hundred() -> None:
    """Batches stay at 100, which is about a quarter of the server's request cap."""
    batches = uc.plan_upsert([_chunk(n) for n in range(250)])

    assert [len(batch) for batch in batches] == [100, 100, 50]


def test_check_metadata_shape_refuses_a_none_value() -> None:
    """A None metadata value is a 400 at the server, after the embeddings are paid for."""
    chunk = _chunk(0)
    chunk.metadata["author_role"] = None

    with pytest.raises(uc._Abort):
        uc.check_metadata_shape(uc.plan_upsert([chunk]))


def test_write_manifest_records_the_ids_before_any_write(tmp_path: Path) -> None:
    """The rollback manifest exists in full before a cent is spent or a vector written.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    chunks = [_chunk(n) for n in range(150)]

    manifest = uc.write_manifest(ctx, chunks, uc.plan_upsert(chunks))

    assert manifest["recorded_before_any_write"] is True
    assert manifest["chunk_count"] == 150
    assert manifest["duplicate_ids"] == 0
    assert [batch["end"] - batch["start"] for batch in manifest["batches"]] == [100, 50]
    on_disk = json.loads(ctx.run.path.read_text(encoding="utf-8"))
    assert on_disk["planned_upsert"]["chunk_ids"] == manifest["chunk_ids"]
    assert "never by {year,month}" not in on_disk["rollback"]["note"]
    assert "Never roll back with a {year,month} metadata filter" in on_disk["rollback"]["note"]


def test_resumable_index_skips_batches_a_previous_invocation_sent(tmp_path: Path) -> None:
    """A resumed upsert does not re-send what already landed.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    sent: list[int] = []
    ctx.index = _SpyIndex(sent)
    ctx.run.stage("upsert")["batches_done"] = 2

    sink = uc._ResumableIndex(ctx, 3)
    for batch in uc.plan_upsert([_chunk(n) for n in range(250)]):
        sink.upsert(vectors=batch)

    assert sent == [50]
    assert ctx.run.stage("upsert")["batches_done"] == 3
    assert sink.sent == 50


class _SpyIndex:
    """An index that records the size of each batch it is asked to upsert."""

    def __init__(self, sent: list[int]) -> None:
        """Record batch sizes into the given list.

        Args:
            sent: the list to append batch sizes to.
        """
        self.sent = sent

    def upsert(self, *, vectors: Sequence[Any], namespace: str = "") -> Any:
        """Record one batch.

        Args:
            vectors: the batch.
            namespace: the namespace, ignored.

        Returns:
            A response carrying the upserted count.
        """
        self.sent.append(len(vectors))
        return type("R", (), {"upserted_count": len(vectors)})()


# --- an end-to-end dry run ------------------------------------------------------------------


def _talk_html(slug: str) -> str:
    """Build a talk page the real loader can parse.

    Args:
        slug: the talk slug.

    Returns:
        The page html.
    """
    paragraphs = "".join(
        f'<p id="p{n}">Paragraph {n} of {slug} carries enough plain words to read as a real body.</p>'
        for n in range(1, 5)
    )
    return (
        "<html><body><article>"
        f"<header><h1>The Discourse of {slug}</h1></header>"
        '<p class="author-name">Elder Someone</p>'
        '<p class="author-role">Of the Quorum of the Twelve Apostles</p>'
        f'<div class="body-block">{paragraphs}</div>'
        "</article></body></html>"
    )


def _listing_html(slugs: list[str]) -> str:
    """Build a listing page that links every talk twice, as the real one does.

    Args:
        slugs: the talk slugs.

    Returns:
        The page html.
    """
    links = "".join(
        f'<a href="/study/general-conference/2026/10/{slug}?lang=eng">{slug}</a>'
        f'<a href="/study/general-conference/2026/10/{slug}?lang=eng#p1">{slug}</a>'
        for slug in slugs
    )
    session = '<a href="/study/general-conference/2026/10/saturday-morning-session?lang=eng">session</a>'
    return f"<html><body>{links}{session}</body></html>"


class _FakeSplitter:
    """A splitter that slices the cleaned talk text, so rail 8 sees genuine substrings."""

    def transform_documents(self, documents: Sequence[Document], **kwargs: Any) -> list[Document]:
        """Split each document into four slices of its normalized text.

        Args:
            documents: the documents to split.
            kwargs: accepted and ignored.

        Returns:
            The chunks.
        """
        chunks = []
        for doc in documents:
            text = clean_text(doc.page_content)
            size = len(text) // CHUNKS_PER_TALK
            for position in range(CHUNKS_PER_TALK):
                start = position * size
                end = (position + 1) * size if position < CHUNKS_PER_TALK - 1 else len(text)
                metadata = dict(doc.metadata, anchor=f"p{position + 1}")
                chunks.append(Document(page_content=text[start:end], metadata=metadata))
        return chunks


class _FakeIndex:
    """A Pinecone index that answers reads and fails the test on any write."""

    def __init__(self, total: int = 35_454) -> None:
        """Start empty, holding the production vector count.

        Args:
            total: the total vector count to report.
        """
        self.total = total

    def describe_index_stats(self, **kwargs: Any) -> Any:
        """Report the production index's shape.

        Args:
            kwargs: accepted and ignored.

        Returns:
            A stats object.
        """
        return type("S", (), {"total_vector_count": self.total, "dimension": 1536, "metric": "cosine"})()

    def fetch(self, *, ids: Sequence[str], namespace: str = "") -> Any:
        """Return no vectors: nothing in this conference is indexed yet.

        Args:
            ids: the ids to look up.
            namespace: the namespace, ignored.

        Returns:
            An empty fetch response.
        """
        return type("F", (), {"vectors": {}})()

    def fetch_by_metadata(self, *, filter: Any, namespace: str = "", limit: Optional[int] = None) -> Any:  # noqa: A002
        """Return no vectors for this conference's metadata.

        Args:
            filter: the metadata filter.
            namespace: the namespace, ignored.
            limit: the result limit, ignored.

        Returns:
            An empty response.
        """
        assert filter == {"year": {"$eq": "2026"}, "month": {"$eq": "10"}}
        return type("F", (), {"vectors": []})()

    def upsert(self, **kwargs: Any) -> None:
        """Fail the test: a dry run must never write.

        Args:
            kwargs: the upsert arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("a dry run must not upsert")

    def delete(self, **kwargs: Any) -> None:
        """Fail the test: a dry run must never delete.

        Args:
            kwargs: the delete arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("a dry run must not delete")

    def update(self, **kwargs: Any) -> None:
        """Fail the test: a dry run must not run the write probe.

        Args:
            kwargs: the update arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("a dry run must not probe for write permission")


class _FakeClient:
    """A Pinecone client handing out the fake index."""

    def __init__(self, api_key: str = "", **kwargs: Any) -> None:
        """Record the key it was built with.

        Args:
            api_key: the api key.
            kwargs: accepted and ignored.
        """
        self.api_key = api_key

    def index(self, host: str = "", **kwargs: Any) -> _FakeIndex:
        """Return the fake index, asserting it was addressed by host.

        Args:
            host: the index host.
            kwargs: accepted and ignored.

        Returns:
            The fake index.
        """
        assert host == uc.INDEX_HOST
        return _FakeIndex()

    def describe_index(self, name: str) -> Any:
        """Describe the index on the control plane.

        Args:
            name: the index name.

        Returns:
            An index model.
        """
        assert name == uc.INDEX_NAME
        return type("M", (), {"host": uc.INDEX_HOST, "deletion_protection": "disabled"})()


@pytest.fixture
def conference(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Iterator[dict[str, Any]]:
    """Stand up a fake 2026-10 conference with no network anywhere.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.

    Yields:
        A mapping holding the recorded page requests and the data root.
    """
    import sys
    import types

    slugs = [f"{n}speaker" for n in range(11, 11 + TALK_COUNT)]
    requests: list[dict[str, Any]] = []

    def fake_get_page(url: str, delay_seconds: int = 30, **kwargs: Any) -> tuple[int, str]:
        requests.append({"url": url, "delay_seconds": delay_seconds})
        if url.endswith("/2026/10?lang=eng"):
            return 200, _listing_html(slugs)
        return 200, _talk_html(url.rsplit("/", 1)[1].split("?")[0])

    monkeypatch.setenv("PINECONE_PROD_KEY", "a-fake-production-key")
    monkeypatch.setattr(uc, "load_dotenv", lambda *a, **k: None)
    monkeypatch.setattr(uc, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(uc, "get_page", fake_get_page)
    monkeypatch.setattr(uc, "Pinecone", _FakeClient)
    module = sys.modules.get("models.split_model")
    if module is None:
        module = types.ModuleType("models.split_model")
        monkeypatch.setitem(sys.modules, "models.split_model", module)
    monkeypatch.setattr(module, "MarkdownSyntacticEmbeddingSplitter", _FakeSplitter, raising=False)
    yield {"requests": requests, "data_dir": tmp_path / "data" / "update" / "2026-10", "slugs": slugs}


def test_dry_run_previews_without_embedding_or_writing(conference: dict[str, Any]) -> None:
    """It crawls, loads, and splits for real, then prints the plan and stops.

    The fake index fails the test on upsert, delete, or update, so "nothing was written"
    is enforced rather than asserted after the fact.

    Args:
        conference: the fake conference fixture.
    """
    result = CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])

    assert result.exit_code == 0, result.output
    assert "DRY RUN -- nothing was embedded and nothing was sent to Pinecone." in result.output
    assert f"would upsert:   {TALK_COUNT * CHUNKS_PER_TALK} vectors in 2 batches of 100" in result.output
    assert "-> 9 metadata keys" in result.output
    assert "--dry-run does not test write permission" in result.output

    data_dir = conference["data_dir"]
    assert len(list((data_dir / "raw").glob("*.json"))) == TALK_COUNT
    assert len(list((data_dir / "split").glob("*.jsonl"))) == TALK_COUNT
    assert (data_dir / "load.jsonl").exists() and (data_dir / "split.jsonl").exists()
    assert not (data_dir / "embeddings.npy").exists()


def test_dry_run_threads_the_delay_into_every_request(conference: dict[str, Any]) -> None:
    """Every fetch, the listing included, uses --delay rather than get_page's default of 30.

    Args:
        conference: the fake conference fixture.
    """
    CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])

    requests = conference["requests"]
    assert len(requests) == TALK_COUNT + 1
    assert {request["delay_seconds"] for request in requests} == {8}


def test_dry_run_writes_the_rollback_manifest_before_anything_else(conference: dict[str, Any]) -> None:
    """The chunk ids a real run will write are on disk after a dry run alone.

    get_doc_id depends on nothing from the embedder, so these are byte-identical to the
    ids the real run uses - which is what makes the manifest a rollback plan rather than
    a receipt.

    Args:
        conference: the fake conference fixture.
    """
    CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])

    record = json.loads((conference["data_dir"] / "run.json").read_text(encoding="utf-8"))

    assert record["status"] == "dry_run_completed"
    assert record["planned_upsert"]["recorded_before_any_write"] is True
    assert record["planned_upsert"]["chunk_count"] == TALK_COUNT * CHUNKS_PER_TALK
    assert len(set(record["planned_upsert"]["chunk_ids"])) == TALK_COUNT * CHUNKS_PER_TALK
    assert record["stages"]["embed"]["status"] == "skipped_dry_run"
    assert record["stages"]["upsert"]["status"] == "skipped_dry_run"
    assert record["stages"]["preflight"]["write_probe"] == "skipped_dry_run"
    assert record["credentials"]["pinecone"]["source"] == "$PINECONE_PROD_KEY"
    assert "a-fake-production-key" not in json.dumps(record)


def test_second_run_resumes_from_cache_without_refetching(conference: dict[str, Any]) -> None:
    """A re-run reuses raw/ and the split shards, fetching only the listing again.

    Args:
        conference: the fake conference fixture.
    """
    runner = CliRunner()
    first = runner.invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])
    assert first.exit_code == 0, first.output
    conference["requests"].clear()

    second = runner.invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])

    assert second.exit_code == 0, second.output
    assert len(conference["requests"]) == 1
    assert "(cached shard)" in second.output
    first_ids = json.loads((conference["data_dir"] / "run.json").read_text(encoding="utf-8"))
    assert first_ids["planned_upsert"]["ids_sha256"]


def test_a_short_listing_aborts_before_any_talk_is_fetched(
    conference: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    """A half-published conference is refused, and refused before the crawl spends time.

    Args:
        conference: the fake conference fixture.
        monkeypatch: the pytest monkeypatch fixture.
    """

    def short_listing(url: str, delay_seconds: int = 30, **kwargs: Any) -> tuple[int, str]:
        conference["requests"].append({"url": url, "delay_seconds": delay_seconds})
        return 200, _listing_html(conference["slugs"][:14])

    monkeypatch.setattr(uc, "get_page", short_listing)

    result = CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])

    assert result.exit_code == uc.EXIT_TALK_COUNT
    assert "below the floor of 30" in result.output
    assert len(conference["requests"]) == 1


def test_loader_skips_abort_and_allow_skips_permits_them(
    conference: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    """A talk served as a JavaScript shell aborts the run unless it is explicitly allowed.

    Args:
        conference: the fake conference fixture.
        monkeypatch: the pytest monkeypatch fixture.
    """
    shells = set(conference["slugs"][:2])

    def shell_pages(url: str, delay_seconds: int = 30, **kwargs: Any) -> tuple[int, str]:
        conference["requests"].append({"url": url, "delay_seconds": delay_seconds})
        if url.endswith("/2026/10?lang=eng"):
            return 200, _listing_html(conference["slugs"])
        slug = url.rsplit("/", 1)[1].split("?")[0]
        if slug in shells:
            return 200, "<html><body><article><header><h1>Shell</h1></header></article></body></html>"
        return 200, _talk_html(slug)

    monkeypatch.setattr(uc, "get_page", shell_pages)
    arguments = ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"]

    refused = CliRunner().invoke(uc.main, arguments)
    assert refused.exit_code == uc.EXIT_LOADER_SKIPS
    assert f"the loader dropped 2 of {TALK_COUNT} talks" in refused.output
    assert "--allow-skips=2" in refused.output

    allowed = CliRunner().invoke(uc.main, arguments + ["--allow-skips", "2"])
    assert allowed.exit_code == 0, allowed.output
    assert f"would upsert:   {(TALK_COUNT - 2) * CHUNKS_PER_TALK} vectors" in allowed.output


def test_allow_skips_cannot_drop_the_run_below_the_talk_floor(
    conference: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    """--allow-skips tolerates drops, but not to the point of indexing a partial conference.

    This is the interlock: without it, --allow-skips=25 would reintroduce the exact
    failure rail 3 exists to prevent.

    Args:
        conference: the fake conference fixture.
        monkeypatch: the pytest monkeypatch fixture.
    """
    shells = set(conference["slugs"][:6])

    def shell_pages(url: str, delay_seconds: int = 30, **kwargs: Any) -> tuple[int, str]:
        if url.endswith("/2026/10?lang=eng"):
            return 200, _listing_html(conference["slugs"])
        slug = url.rsplit("/", 1)[1].split("?")[0]
        if slug in shells:
            return 200, "<html><body><article><header><h1>Shell</h1></header></article></body></html>"
        return 200, _talk_html(slug)

    monkeypatch.setattr(uc, "get_page", shell_pages)

    result = CliRunner().invoke(
        uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8", "--allow-skips", "6"]
    )

    assert result.exit_code == uc.EXIT_TALK_COUNT
    assert "yielded 27 talks, below the floor of 30" in result.output


# --- the production key: every path, including the one that must never be taken ----------

DEV_KEY = "models-dot-env-development-key"


def _point_at_sibling(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, body: str) -> Path:
    """Write a temporary server/.env and point SIBLING_ENV at it.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
        body: the contents of the file.

    Returns:
        The path the module will now read as the sibling .env.
    """
    sibling = tmp_path / "server" / ".env"
    sibling.parent.mkdir(parents=True, exist_ok=True)
    sibling.write_text(body, encoding="utf-8")
    monkeypatch.setattr(uc, "SIBLING_ENV", sibling)
    return sibling


def test_resolve_pinecone_key_falls_back_to_the_sibling_server_env(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """With no $PINECONE_PROD_KEY it reads PINECONE_KEY out of ../server/.env.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
    """
    monkeypatch.delenv("PINECONE_PROD_KEY", raising=False)
    _point_at_sibling(monkeypatch, tmp_path, "OPENAI_KEY=unrelated\nPINECONE_KEY=the-production-key\n")

    assert uc.resolve_pinecone_key() == ("the-production-key", "server/.env:PINECONE_KEY")


def test_resolve_pinecone_key_aborts_when_the_sibling_defines_no_production_key(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """A sibling file holding only a commented-out key is no key at all.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
    """
    monkeypatch.delenv("PINECONE_PROD_KEY", raising=False)
    _point_at_sibling(monkeypatch, tmp_path, "# PINECONE_KEY=a-retired-key\nOPENAI_KEY=unrelated\n")

    with pytest.raises(uc._Abort) as caught:
        uc.resolve_pinecone_key()

    assert caught.value.code == uc.EXIT_NO_KEY
    assert "defines no PINECONE_KEY" in caught.value.body
    assert "a-retired-key" not in caught.value.body


def test_resolve_pinecone_key_abort_explains_why_models_env_is_not_a_fallback(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """The refusal names the dev key by variable and says why it is excluded.

    The next person to hit this will have models/.env open in front of them with a
    PINECONE_API_KEY in it; the message has to say "not that one" out loud, or the
    obvious fix is to add it as a third source.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
    """
    monkeypatch.delenv("PINECONE_PROD_KEY", raising=False)
    monkeypatch.setattr(uc, "SIBLING_ENV", tmp_path / "absent" / ".env")

    with pytest.raises(uc._Abort) as caught:
        uc.resolve_pinecone_key()

    assert "models/.env's PINECONE_API_KEY is deliberately NOT a fallback" in caught.value.body
    assert "$PINECONE_PROD_KEY" in caught.value.body


def test_the_development_key_is_never_the_resolved_key(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Every exit from resolve_pinecone_key, with models/.env's key live in the environment.

    This is the dangerous case, so it is tested as an exhaustive sweep rather than one
    scenario: the dev key is exported throughout, and each of the three reachable
    outcomes is checked for it. A run that quietly used it would index ~300 vectors into
    an empty project and report success.

    Args:
        monkeypatch: the pytest monkeypatch fixture.
        tmp_path: a temporary directory.
    """
    monkeypatch.setenv("PINECONE_API_KEY", DEV_KEY)
    _point_at_sibling(monkeypatch, tmp_path, f"PINECONE_KEY=prod-from-file\n# PINECONE_API_KEY={DEV_KEY}\n")

    monkeypatch.setenv("PINECONE_PROD_KEY", "prod-from-env")
    assert uc.resolve_pinecone_key() == ("prod-from-env", "$PINECONE_PROD_KEY")

    monkeypatch.delenv("PINECONE_PROD_KEY")
    assert uc.resolve_pinecone_key() == ("prod-from-file", "server/.env:PINECONE_KEY")

    monkeypatch.setattr(uc, "SIBLING_ENV", tmp_path / "absent" / ".env")
    with pytest.raises(uc._Abort) as caught:
        uc.resolve_pinecone_key()
    assert caught.value.code == uc.EXIT_NO_KEY
    assert DEV_KEY not in caught.value.body + caught.value.summary


# --- rail 2b: the handle really is the production index -----------------------------------


@dataclass
class _Stats:
    """The three fields rail 2b reads off a describe_index_stats response.

    Attributes:
        total_vector_count: how many vectors the index holds.
        dimension: the index's vector width.
        metric: the index's distance metric.
    """

    total_vector_count: int = 35_454
    dimension: int = uc.INDEX_DIM
    metric: str = uc.INDEX_METRIC


@pytest.mark.parametrize(
    ("stats", "why"),
    [
        (_Stats(dimension=3072), "a text-embedding-3-large index"),
        (_Stats(metric="dotproduct"), "an index built with another metric"),
        (_Stats(total_vector_count=12), "a fresh, empty index"),
        (_Stats(total_vector_count=1_000_000), "something far too large to be this corpus"),
    ],
)
def test_index_identity_refuses_anything_but_the_production_shape(stats: _Stats, why: str) -> None:
    """A key that reaches some other index is caught before a cent is spent.

    Args:
        stats: the stats of the index the key actually reached.
        why: what that index would be, for the failure message.
    """
    with pytest.raises(uc._Abort) as caught:
        uc.check_index_identity(stats, "ab12cd34", "$PINECONE_PROD_KEY")

    assert caught.value.code == uc.EXIT_WRONG_INDEX, why
    assert "Nothing was crawled or written" in caught.value.body


def test_index_identity_accepts_the_production_index() -> None:
    """The real index's shape passes, so the guard is not vacuous."""
    uc.check_index_identity(_Stats(), "ab12cd34", "$PINECONE_PROD_KEY")


def test_describe_stats_turns_a_rejected_key_into_rail_2b() -> None:
    """A 403 on the first read is reported as the wrong key, not as a crash."""

    class _RefusingIndex:
        """An index that rejects the key."""

        def describe_index_stats(self) -> Any:
            """Reject the key.

            Raises:
                ForbiddenError: always.
            """
            raise ForbiddenError("not authorized for this index", 403)

    with pytest.raises(uc._Abort) as caught:
        uc._describe_stats(_RefusingIndex(), "ab12cd34", "server/.env:PINECONE_KEY")

    assert caught.value.code == uc.EXIT_WRONG_INDEX
    assert "403 ForbiddenError" in caught.value.body
    assert "server/.env:PINECONE_KEY" in caught.value.body


# --- rail 6: the already-indexed lookup, against a mocked index ----------------------------


@dataclass
class _Response:
    """A minimal stand-in for a Pinecone data-plane response.

    Attributes:
        vectors: what fetch and fetch_by_metadata return.
        matches: what query returns.
    """

    vectors: Any = field(default_factory=dict)
    matches: Any = field(default_factory=list)


class _MetadataIndex:
    """An index that answers the conference lookup and records how it was asked."""

    def __init__(self, hits: int = 0, exact_lookup_fails: bool = False) -> None:
        """Answer with the given number of hits.

        Args:
            hits: how many matching vectors to report.
            exact_lookup_fails: whether fetch_by_metadata should raise, forcing the fallback.
        """
        self.hits = hits
        self.exact_lookup_fails = exact_lookup_fails
        self.filters: list[Any] = []
        self.queries: list[dict[str, Any]] = []

    def fetch_by_metadata(self, *, filter: Any, namespace: str = "", limit: Optional[int] = None) -> Any:  # noqa: A002
        """Look vectors up by metadata.

        Args:
            filter: the metadata filter.
            namespace: the namespace.
            limit: the result cap.

        Returns:
            A response holding one entry per hit.

        Raises:
            ApiError: when this fake was built to reject the exact lookup.
        """
        self.filters.append(filter)
        assert namespace == uc.NAMESPACE
        if self.exact_lookup_fails:
            raise ApiError("fetch_by_metadata is not available here", 400)
        return _Response(vectors={f"hit{n}": None for n in range(self.hits)})

    def query(self, **kwargs: Any) -> Any:
        """Run the fallback filtered query.

        Args:
            kwargs: the query arguments.

        Returns:
            A response holding one match per hit.
        """
        self.queries.append(kwargs)
        return _Response(matches=[object() for _ in range(self.hits)])


def test_metadata_lookup_compares_year_and_month_as_strings() -> None:
    """Year and month are stored zero-padded as strings; an int filter would match nothing.

    An int filter does not error, it returns zero hits - so the guard would fail open and
    let the script double-index a conference that is already there.
    """
    index = _MetadataIndex(hits=3)

    assert uc._metadata_hits(index, 2026, "10") == 3
    assert index.filters == [{"year": {"$eq": "2026"}, "month": {"$eq": "10"}}]
    assert isinstance(index.filters[0]["year"]["$eq"], str)


def test_metadata_lookup_falls_back_to_a_filtered_query() -> None:
    """When the exact lookup is unavailable the approximate one still answers."""
    index = _MetadataIndex(hits=2, exact_lookup_fails=True)

    assert uc._metadata_hits(index, 2026, "10") == 2
    assert index.queries[0]["filter"] == {"year": "2026", "month": "10"}
    assert index.queries[0]["vector"] == uc.PROBE_VECTOR
    assert index.queries[0]["namespace"] == uc.NAMESPACE


def test_already_indexed_guard_acts_on_what_the_mocked_index_reports(tmp_path: Path) -> None:
    """A conference the mocked index already holds is refused; an empty one proceeds.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)

    with pytest.raises(uc._Abort) as caught:
        uc.check_not_already_indexed(ctx, uc._metadata_hits(_MetadataIndex(hits=4), ctx.year, ctx.month))
    assert caught.value.code == uc.EXIT_ALREADY_INDEXED
    assert "returned 4 matches" in caught.value.body
    assert "Nothing was written to Pinecone" in caught.value.body

    uc.check_not_already_indexed(ctx, uc._metadata_hits(_MetadataIndex(hits=0), ctx.year, ctx.month))


class _FetchIndex:
    """An index that answers exact id lookups and records the batch sizes it was asked for."""

    def __init__(self, present: set[str]) -> None:
        """Hold the given ids.

        Args:
            present: the ids this index already has.
        """
        self.present = present
        self.batches: list[int] = []

    def fetch(self, *, ids: Sequence[str], namespace: str = "") -> Any:
        """Look up ids.

        Args:
            ids: the ids to look up.
            namespace: the namespace.

        Returns:
            A response holding the ids that are present.
        """
        self.batches.append(len(ids))
        return _Response(vectors={one: None for one in ids if one in self.present})


def test_chunk_ids_already_in_the_index_are_refused_unless_forced(tmp_path: Path) -> None:
    """The exact-id guard is the authoritative one, and it pages through in batches of 100.

    Args:
        tmp_path: a temporary directory.
    """
    chunk_ids = [f"id{n:03d}" for n in range(250)]
    ctx = _ctx(tmp_path)
    ctx.index = _FetchIndex({"id007", "id201"})

    with pytest.raises(uc._Abort) as caught:
        uc.check_ids_absent(ctx, chunk_ids)
    assert caught.value.code == uc.EXIT_ALREADY_INDEXED
    assert "2 of 250 chunk ids" in caught.value.summary
    assert ctx.index.batches == [100, 100, 50]

    forced = _ctx(tmp_path, force=True)
    forced.index = _FetchIndex({"id007", "id201"})
    assert sorted(uc.check_ids_absent(forced, chunk_ids)) == ["id007", "id201"]


def test_chunk_ids_absent_from_the_index_let_the_run_through(tmp_path: Path) -> None:
    """A conference nothing in the index knows about is not refused.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    ctx.index = _FetchIndex(set())

    assert uc.check_ids_absent(ctx, [f"id{n}" for n in range(5)]) == []


# --- rail 7: the write-permission probe ------------------------------------------------------


class _NoWriteIndex:
    """An index on which every data-plane call fails the test."""

    def update(self, **kwargs: Any) -> None:
        """Fail the test.

        Args:
            kwargs: the update arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("the probe must not run here")

    def upsert(self, **kwargs: Any) -> None:
        """Fail the test.

        Args:
            kwargs: the upsert arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("nothing may be upserted here")

    def delete(self, **kwargs: Any) -> None:
        """Fail the test.

        Args:
            kwargs: the delete arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("nothing may be deleted here")


class _ProbeIndex(_NoWriteIndex):
    """An index that records the no-op update probe, and can refuse it."""

    def __init__(self, refuse: bool = False) -> None:
        """Accept or refuse the probe.

        Args:
            refuse: whether to answer the probe with a 403, as a read-only key would.
        """
        self.refuse = refuse
        self.updates: list[dict[str, Any]] = []

    def update(self, **kwargs: Any) -> None:
        """Record the probe.

        Args:
            kwargs: the update arguments.

        Raises:
            ForbiddenError: when this fake was built to refuse.
        """
        self.updates.append(kwargs)
        if self.refuse:
            raise ForbiddenError("the api key does not have write permission", 403)


def test_a_dry_run_never_probes_for_write_permission(tmp_path: Path) -> None:
    """--dry-run means no data-plane write path is exercised at all.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path, dry_run=True)
    ctx.index = _NoWriteIndex()

    assert uc.run_write_probe(ctx, "ab12cd34", "$PINECONE_PROD_KEY") == "skipped_dry_run"


def test_write_probe_skip_touches_nothing(tmp_path: Path) -> None:
    """--write-probe=skip is honored, and says so in the record.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path, write_probe="skip")
    ctx.index = _NoWriteIndex()

    assert uc.run_write_probe(ctx, "ab12cd34", "$PINECONE_PROD_KEY") == "skipped"


def test_the_default_probe_writes_nothing_and_targets_an_impossible_id(tmp_path: Path) -> None:
    """The update probe traverses the write path without creating a vector.

    An update against an id that cannot exist is a server-side no-op, so unlike PLAN.md's
    canary it never puts anything in production - and the inherited upsert and delete
    fail the test if the implementation ever drifts back to writing one.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    ctx.index = _ProbeIndex()

    assert uc.run_write_probe(ctx, "ab12cd34", "$PINECONE_PROD_KEY") == "ok:update"
    assert ctx.index.updates == [{"id": uc.UPDATE_PROBE_ID, "set_metadata": {"probe": "1"}, "namespace": uc.NAMESPACE}]
    assert uc.UPDATE_PROBE_ID.startswith("__") and uc.UPDATE_PROBE_ID != uc.CANARY_ID


def test_a_read_only_key_is_refused_before_the_crawl(tmp_path: Path) -> None:
    """A 403 on the probe exits 70, with the key source in the message.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    ctx.index = _ProbeIndex(refuse=True)

    with pytest.raises(uc._Abort) as caught:
        uc.run_write_probe(ctx, "ab12cd34", "server/.env:PINECONE_KEY")

    assert caught.value.code == uc.EXIT_CANARY_REFUSED
    assert "403 ForbiddenError" in caught.value.body
    assert "server/.env:PINECONE_KEY" in caught.value.body
    assert "before a single embedding was purchased" in caught.value.body


class _CanaryIndex:
    """A tiny in-memory index, so the canary's write-confirm-remove loop is observable."""

    def __init__(self, confirm: bool = True, preloaded: bool = False) -> None:
        """Start empty, or holding a canary a previous run left behind.

        Args:
            confirm: whether an upserted vector becomes readable, as a real index would.
            preloaded: whether a stale canary is already present.
        """
        self.confirm = confirm
        self.store: dict[str, Any] = {uc.CANARY_ID: None} if preloaded else {}
        self.upserts: list[Any] = []
        self.deletes: list[list[str]] = []

    def upsert(self, *, vectors: Sequence[Any], namespace: str = "") -> None:
        """Write the given vectors.

        Args:
            vectors: the (id, values, metadata) triples.
            namespace: the namespace.
        """
        self.upserts.append(list(vectors))
        if self.confirm:
            for vector_id, _values, metadata in vectors:
                self.store[vector_id] = metadata

    def fetch(self, *, ids: Sequence[str], namespace: str = "") -> Any:
        """Look up ids.

        Args:
            ids: the ids to look up.
            namespace: the namespace.

        Returns:
            A response holding the ids that are present.
        """
        return _Response(vectors={one: self.store[one] for one in ids if one in self.store})

    def delete(self, *, ids: Sequence[str], namespace: str = "") -> None:
        """Remove ids.

        Args:
            ids: the ids to remove.
            namespace: the namespace.
        """
        self.deletes.append(list(ids))
        for one in ids:
            self.store.pop(one, None)


def test_the_canary_writes_one_vector_and_takes_it_back_out(tmp_path: Path) -> None:
    """PLAN.md's canary leaves the index exactly as it found it.

    --write-probe=canary is a documented fallback, so the path has to be known-good even
    though the default probe writes nothing. Exercised against an in-memory index: no
    Pinecone, production or otherwise, is involved.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path, write_probe="canary")
    ctx.index = _CanaryIndex()

    assert uc.run_write_probe(ctx, "ab12cd34", "$PINECONE_PROD_KEY") == "ok:canary"

    assert len(ctx.index.upserts) == 1 and len(ctx.index.upserts[0]) == 1
    vector_id, values, metadata = ctx.index.upserts[0][0]
    assert (vector_id, len(values)) == (uc.CANARY_ID, uc.INDEX_DIM)
    assert metadata == uc._canary_metadata()
    assert ctx.index.deletes == [[uc.CANARY_ID]]
    assert ctx.index.store == {}


def test_the_canary_is_removed_even_when_the_run_aborts(tmp_path: Path) -> None:
    """An abort between the write and the removal still takes the vector back out.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path, write_probe="canary")
    ctx.index = _CanaryIndex(confirm=False)

    with pytest.raises(uc._Abort) as caught:
        uc.run_write_probe(ctx, "ab12cd34", "$PINECONE_PROD_KEY")

    assert caught.value.code == uc.EXIT_CANARY_REFUSED
    assert ctx.index.deletes == [[uc.CANARY_ID]]
    assert ctx.index.store == {}


def test_a_stale_canary_is_swept_before_the_already_indexed_guard(tmp_path: Path) -> None:
    """A canary a killed run left behind is removed, and only looked at on a dry run.

    Args:
        tmp_path: a temporary directory.
    """
    dry = _ctx(tmp_path, dry_run=True)
    dry.index = _CanaryIndex(preloaded=True)
    uc.sweep_stale_canary(dry)
    assert dry.index.deletes == []

    real = _ctx(tmp_path)
    real.index = _CanaryIndex(preloaded=True)
    uc.sweep_stale_canary(real)
    assert real.index.deletes == [[uc.CANARY_ID]]
    assert real.index.store == {}


# --- rail 3: the crawl floor, and the pages that back it --------------------------------------


@pytest.mark.parametrize(("talks", "allowed"), [(14, False), (29, False), (30, True), (35, True)])
def test_a_listing_of_fourteen_aborts_and_one_of_thirty_five_proceeds(talks: int, allowed: bool) -> None:
    """The predicate and the floor together: a half-published conference never reaches the crawl.

    Args:
        talks: how many talks the listing links.
        allowed: whether a listing that size may proceed.
    """
    html = _listing_html([f"{n}speaker" for n in range(11, 11 + talks)])
    urls, _anchors, _matched, _near_misses = uc.extract_talk_urls(html, f"{HOST}/x", 2026, "10")

    assert len(urls) == talks
    if allowed:
        uc.check_talk_count(len(urls), "the listing", "detail")
        return
    with pytest.raises(uc._Abort) as caught:
        uc.check_talk_count(len(urls), "the listing", "detail")
    assert caught.value.code == uc.EXIT_TALK_COUNT


def _write_raw(ctx: uc.Ctx, url: str) -> None:
    """Put a well-formed crawled page on disk for one url.

    Args:
        ctx: the run context.
        url: the canonical talk url.
    """
    path = ctx.raw_dir / f"{uc.talk_stem(url)}.json"
    path.write_text(json.dumps({"url": url, "html": "<html></html>"}), encoding="utf-8")


def test_a_talk_missing_from_raw_aborts_the_run(tmp_path: Path) -> None:
    """A conference with a hole in it is never loaded as if it were complete.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    urls = [f"{HOST}/study/general-conference/2026/10/{n}speaker?lang=eng" for n in (11, 12)]
    _write_raw(ctx, urls[0])

    with pytest.raises(uc._Abort) as caught:
        uc._check_crawl_complete(ctx, urls, [{"url": urls[1], "status_code": 503}])

    assert caught.value.code == uc.EXIT_GUARD
    assert "1 of 2 talks are missing" in caught.value.summary
    assert "503" in caught.value.body

    _write_raw(ctx, urls[1])
    assert uc._check_crawl_complete(ctx, urls, []) == 2


def test_a_listing_that_grew_since_the_crawl_aborts_unless_forced(tmp_path: Path) -> None:
    """A conference that was half-published at first crawl must not stay half-indexed.

    Args:
        tmp_path: a temporary directory.
    """
    cached = [f"{HOST}/study/general-conference/2026/10/{n}speaker?lang=eng" for n in (11, 12)]
    fresh = cached + [f"{HOST}/study/general-conference/2026/10/13speaker?lang=eng"]

    ctx = _ctx(tmp_path)
    ctx.run.stage("crawl")["talk_urls"] = cached
    with pytest.raises(uc._Abort) as caught:
        uc._check_listing_unchanged(ctx, fresh)
    assert caught.value.code == uc.EXIT_GUARD
    assert "+ " + fresh[2] in caught.value.body

    forced = _ctx(tmp_path, force=True)
    forced.run.stage("crawl")["talk_urls"] = cached
    uc._check_listing_unchanged(forced, fresh)
    uc._check_listing_unchanged(ctx, cached)


# --- rail 8: a chunk's text really came from the talk -------------------------------------------

TALK_MARKDOWN = (
    '<a name="p1"></a>In the beginning the Saints gathered, and they '
    "[read the record](https://www.churchofjesuschrist.org/study/scriptures) together.[1]\n\n"
    '<a name="p2"></a>They spoke of “peace,” and of a hope that does not fail.'
)
TALK_URL = f"{HOST}/study/general-conference/2026/10/11speaker?lang=eng"


def _talk_document() -> Document:
    """Build the loaded talk the chunks are checked against.

    Returns:
        A document holding markdown with the anchors, links and citations the loader emits.
    """
    return Document(page_content=TALK_MARKDOWN, metadata={"url": TALK_URL, "title": "A Talk", "year": "2026"})


def _chunk_of(text: str, **overrides: str) -> Document:
    """Build one chunk attributed to the talk above.

    Args:
        text: the chunk's text.
        overrides: metadata fields to replace.

    Returns:
        A chunk document.
    """
    metadata: dict[str, Any] = {"url": TALK_URL, "year": "2026", "month": "10", "anchor": "p1"}
    metadata.update(overrides)
    return Document(page_content=text, metadata=metadata)


def test_text_integrity_compares_normalized_text_not_raw_markdown(tmp_path: Path) -> None:
    """A chunk the splitter legitimately rewrote still passes.

    This is the measured correction to the original rail: verbatim containment holds for
    only 10 of 62 real chunks, because clean_text rewrites links, anchors, citations and
    whitespace between the loaded markdown and the final chunk. The chunk asserted here
    is deliberately NOT a substring of the source, and must still be accepted.

    Args:
        tmp_path: a temporary directory.
    """
    doc = _talk_document()
    chunk = _chunk_of("In the beginning the Saints gathered, and they read the record together.")

    assert chunk.page_content not in doc.page_content

    uc.check_text_integrity(_ctx(tmp_path), doc, [chunk])


def test_text_integrity_refuses_a_chunk_that_is_not_in_the_talk(tmp_path: Path) -> None:
    """Text the talk never contained is refused, before anything is embedded.

    Args:
        tmp_path: a temporary directory.
    """
    doc = _talk_document()
    chunk = _chunk_of("The Saints departed for a city that is not in this talk at all.")

    with pytest.raises(uc._Abort) as caught:
        uc.check_text_integrity(_ctx(tmp_path), doc, [chunk])

    assert caught.value.code == uc.EXIT_TEXT_INTEGRITY
    assert TALK_URL in caught.value.body
    assert "chunk: 1 of 1" in caught.value.body
    assert "Nothing was embedded or written to Pinecone" in caught.value.body


def test_text_integrity_catches_a_single_corrupted_word(tmp_path: Path) -> None:
    """One wrong word is the realistic corruption, and normalized containment still sees it.

    Args:
        tmp_path: a temporary directory.
    """
    doc = _talk_document()
    chunk = _chunk_of("In the beginning the Saints scattered, and they read the record together.")

    with pytest.raises(uc._Abort) as caught:
        uc.check_text_integrity(_ctx(tmp_path), doc, [chunk])

    assert caught.value.code == uc.EXIT_TEXT_INTEGRITY


def test_text_integrity_reports_at_most_three_failures_and_counts_the_rest(tmp_path: Path) -> None:
    """Every chunk is checked, and the report stays readable when many fail.

    Args:
        tmp_path: a temporary directory.
    """
    doc = _talk_document()
    chunks = [_chunk_of(f"text number {n} that the talk never contained") for n in range(5)]

    with pytest.raises(uc._Abort) as caught:
        uc.check_text_integrity(_ctx(tmp_path), doc, chunks)

    assert "... and 2 more failing chunks in this talk" in caught.value.body
    assert "checked 5 of 5 chunks for this talk; 5 failed." in caught.value.body


@pytest.mark.parametrize(
    ("overrides", "why"),
    [
        ({"url": f"{HOST}/study/general-conference/2026/10/12other?lang=eng"}, "another talk's url"),
        ({"year": "2025"}, "another conference's year"),
    ],
)
def test_text_integrity_refuses_a_chunk_carrying_another_talks_metadata(
    tmp_path: Path, overrides: dict[str, str], why: str
) -> None:
    """A chunk that inherited the wrong parent would deep-link readers into the wrong talk.

    The text is a genuine substring here, so only the metadata check can catch it.

    Args:
        tmp_path: a temporary directory.
        overrides: the metadata field that is wrong.
        why: what is wrong with it, for the failure message.
    """
    doc = _talk_document()
    chunk = _chunk_of("In the beginning the Saints gathered", **overrides)

    with pytest.raises(uc._Abort) as caught:
        uc.check_text_integrity(_ctx(tmp_path), doc, [chunk])

    assert caught.value.code == uc.EXIT_TEXT_INTEGRITY, why
    assert "different talk or conference" in caught.value.summary


# --- the embedding cache is keyed to the chunk plan ----------------------------------------------


def test_cached_embeddings_are_reused_only_for_the_identical_chunk_plan(tmp_path: Path) -> None:
    """embeddings.npy is reused only when run.json says it belongs to these exact ids.

    "The file exists, therefore skip" would hand the upsert stage vectors belonging to a
    previous, different set of chunks - every one of them attached to the wrong id.

    Args:
        tmp_path: a temporary directory.
    """
    ctx = _ctx(tmp_path)
    np.save(ctx.data_dir / "embeddings.npy", np.zeros((4, uc.INDEX_DIM), dtype=np.float32))
    ctx.run.stage("embed")["ids_sha256"] = "the-plan-digest"

    assert uc._reuse_embeddings(ctx, 4, "the-plan-digest") is not None
    assert uc._reuse_embeddings(ctx, 4, "a-different-plan-digest") is None
    assert uc._reuse_embeddings(ctx, 5, "the-plan-digest") is None


# --- a complete, non-dry run against an index that records instead of writing ---------------


@dataclass
class _UpsertResponse:
    """What a Pinecone upsert returns.

    Attributes:
        upserted_count: how many vectors the server accepted.
    """

    upserted_count: int


class _RecordingIndex:
    """A small in-memory index: it answers reads from what it has been given, over no network.

    Stateful on purpose. A fake that forgets what it was sent would let a second run of
    the same conference sail past rail 6, which is exactly the mistake rail 6 exists to
    catch. It also snapshots run.json as the first batch arrives, which is how the "ids
    on disk before anything is sent" ordering is enforced rather than inferred.
    """

    def __init__(self, run_path: Path) -> None:
        """Start at the production vector count, holding nothing of this conference.

        Args:
            run_path: the run record to snapshot when the first batch arrives.
        """
        self.run_path = run_path
        self.base_total = 35_454
        self.store: dict[str, dict[str, Any]] = {}
        self.upserted: list[tuple[str, Sequence[float], dict[str, Any]]] = []
        self.updates: list[dict[str, Any]] = []
        self.deletes: list[list[str]] = []
        self.snapshot: Optional[dict[str, Any]] = None

    def describe_index_stats(self, **kwargs: Any) -> Any:
        """Report the index's shape and current size.

        Args:
            kwargs: accepted and ignored.

        Returns:
            A stats object.
        """
        return _Stats(total_vector_count=self.base_total + len(self.store))

    def fetch(self, *, ids: Sequence[str], namespace: str = "") -> Any:
        """Look ids up exactly.

        Args:
            ids: the ids to look up.
            namespace: the namespace.

        Returns:
            A response holding the ids that are present.
        """
        return _Response(vectors={one: self.store[one] for one in ids if one in self.store})

    def fetch_by_metadata(self, *, filter: Any, namespace: str = "", limit: Optional[int] = None) -> Any:  # noqa: A002
        """Look vectors up by year and month.

        Args:
            filter: the metadata filter.
            namespace: the namespace.
            limit: the result cap.

        Returns:
            A response holding up to limit matching vectors.
        """
        wanted = {key: value["$eq"] for key, value in filter.items()}
        matches = [one for one, metadata in self.store.items() if all(metadata.get(k) == v for k, v in wanted.items())]
        return _Response(vectors=matches[: limit or len(matches)])

    def update(self, **kwargs: Any) -> None:
        """Record the write-permission probe. It names an id that cannot exist, so it stores nothing.

        Args:
            kwargs: the update arguments.
        """
        self.updates.append(kwargs)

    def upsert(self, *, vectors: Sequence[Any], namespace: str = "") -> _UpsertResponse:
        """Record one batch.

        Args:
            vectors: the (id, values, metadata) triples.
            namespace: the namespace.

        Returns:
            The accepted count.
        """
        if self.snapshot is None:
            self.snapshot = json.loads(self.run_path.read_text(encoding="utf-8"))
        for vector_id, _values, metadata in vectors:
            self.store[vector_id] = metadata
        self.upserted.extend(vectors)
        return _UpsertResponse(len(vectors))

    def delete(self, **kwargs: Any) -> None:
        """Fail the test: a run using the default probe never deletes.

        Args:
            kwargs: the delete arguments.

        Raises:
            AssertionError: always.
        """
        raise AssertionError("a run with the update probe must never delete")


class _StubEmbedder:
    """Stands in for OpenAIEmbedder so no key is read and no request is made."""

    def embed_documents(self, texts: Sequence[str]) -> list[list[float]]:
        """Embed texts.

        Args:
            texts: the texts to embed.

        Returns:
            One unit vector of the production width per text.
        """
        return [[1.0] + [0.0] * (uc.INDEX_DIM - 1) for _ in texts]


@pytest.fixture
def writing_conference(conference: dict[str, Any], monkeypatch: pytest.MonkeyPatch) -> Iterator[dict[str, Any]]:
    """Let the fake 2026-10 conference run all the way through stage 4, writing nowhere.

    Args:
        conference: the fake conference fixture.
        monkeypatch: the pytest monkeypatch fixture.

    Yields:
        The conference mapping, with the recording index added.
    """
    index = _RecordingIndex(conference["data_dir"] / "run.json")

    class _RecordingClient:
        """A Pinecone client handing out the recording index."""

        def __init__(self, api_key: str = "", **kwargs: Any) -> None:
            """Accept any key.

            Args:
                api_key: the api key.
                kwargs: accepted and ignored.
            """
            self.api_key = api_key

        def index(self, host: str = "", **kwargs: Any) -> _RecordingIndex:
            """Return the recording index.

            Args:
                host: the index host.
                kwargs: accepted and ignored.

            Returns:
                The recording index.
            """
            assert host == uc.INDEX_HOST
            return index

        def describe_index(self, name: str) -> Any:
            """Describe the index on the control plane.

            Args:
                name: the index name.

            Returns:
                An index model.
            """
            return type("M", (), {"host": uc.INDEX_HOST, "deletion_protection": "disabled"})()

    def fake_embed_documents(embedder: Any, docs: Sequence[Document], batch_size: int, delay: float) -> list[Any]:
        """Embed every chunk without calling OpenAI.

        Args:
            embedder: the embedder, ignored.
            docs: the chunks to embed.
            batch_size: the batch size, ignored.
            delay: the inter-batch delay, ignored.

        Returns:
            One unit vector of the production width per chunk.
        """
        return [[1.0] + [0.0] * (uc.INDEX_DIM - 1) for _ in docs]

    monkeypatch.setattr(uc, "Pinecone", _RecordingClient)
    monkeypatch.setattr(uc, "OpenAIEmbedder", _StubEmbedder)
    monkeypatch.setattr(uc, "embed_documents", fake_embed_documents)
    conference["index"] = index
    yield conference


def test_a_real_run_writes_exactly_the_ids_it_recorded_first(writing_conference: dict[str, Any]) -> None:
    """The vectors that reach the index are, id for id, the manifest written before them.

    The recording index snapshots run.json as the first batch arrives, so the ordering is
    enforced by the fake rather than inferred from the finished file: a manifest written
    after the upsert, or an id sent that was never planned, fails here.

    Args:
        writing_conference: the fake conference fixture, with a recording index.
    """
    result = CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--delay", "8"])

    assert result.exit_code == 0, result.output
    index = writing_conference["index"]
    record = json.loads((writing_conference["data_dir"] / "run.json").read_text(encoding="utf-8"))
    planned = record["planned_upsert"]["chunk_ids"]

    assert index.snapshot is not None, "nothing was ever upserted"
    assert index.snapshot["planned_upsert"]["chunk_ids"] == planned
    assert [vector_id for vector_id, _values, _metadata in index.upserted] == planned
    assert len(planned) == TALK_COUNT * CHUNKS_PER_TALK
    assert index.snapshot["planned_upsert"]["recorded_before_any_write"] is False
    assert index.snapshot["stages"]["upsert"]["status"] == "in_progress"


def test_a_real_run_sends_the_nine_metadata_keys_and_nothing_else(writing_conference: dict[str, Any]) -> None:
    """Every vector carries exactly what server/server/main.py subscripts unguarded.

    Args:
        writing_conference: the fake conference fixture, with a recording index.
    """
    assert CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--delay", "8"]).exit_code == 0

    for vector_id, values, metadata in writing_conference["index"].upserted:
        assert set(metadata) == uc.METADATA_KEYS
        assert metadata["source"] == vector_id
        assert (metadata["year"], metadata["month"]) == ("2026", "10")
        assert len(values) == uc.INDEX_DIM


def test_a_real_run_probes_without_writing_and_cannot_be_repeated(writing_conference: dict[str, Any]) -> None:
    """One no-op probe, no deletes, and a second run refused by the index's own contents.

    Args:
        writing_conference: the fake conference fixture, with a recording index.
    """
    first = CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--delay", "8"])
    assert first.exit_code == 0, first.output

    index = writing_conference["index"]
    record = json.loads((writing_conference["data_dir"] / "run.json").read_text(encoding="utf-8"))

    assert [update["id"] for update in index.updates] == [uc.UPDATE_PROBE_ID]
    assert index.deletes == []
    assert record["status"] == "completed"
    assert record["index_stats"]["delta"] == TALK_COUNT * CHUNKS_PER_TALK
    assert record["stages"]["upsert"]["vectors_sent"] == TALK_COUNT * CHUNKS_PER_TALK
    assert "complete in" in first.output

    second = CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--delay", "8"])

    # Rail 6a (the completed run.json) fires before the index is ever consulted, so the
    # repeat is refused with EXIT_GUARD rather than reaching rail 6b's EXIT_ALREADY_INDEXED.
    # Rail 6b keeps its own coverage in the unit tests above.
    assert second.exit_code == uc.EXIT_GUARD
    assert "records a completed run" in second.output
    assert len(index.upserted) == TALK_COUNT * CHUNKS_PER_TALK


def test_a_completed_run_is_refused_from_the_command_line(conference: dict[str, Any]) -> None:
    """run.json saying "completed" should stop a re-run before the index is consulted at all.

    The unit test above proves check_no_completed_run itself works; this proves whether
    anything ever reaches it. The index is not the backstop here: rail 6b only sees a
    conference that is genuinely indexed, so a completed run whose vectors were since
    removed, or a run against a lagging index, gets no refusal at all.

    Args:
        conference: the fake conference fixture.
    """
    data_dir = conference["data_dir"]
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "run.json").write_text(
        json.dumps({"schema_version": uc.SCHEMA_VERSION, "status": "completed", "stages": {}}), encoding="utf-8"
    )

    result = CliRunner().invoke(uc.main, ["--year", "2026", "--month", "10", "--dry-run", "--delay", "8"])

    assert result.exit_code == uc.EXIT_GUARD
    assert "records a completed run" in result.output


def test_the_site_year_reminder_stays_quiet_when_the_constant_is_current(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """A reminder that fires on every run teaches the operator to ignore it.

    Args:
        tmp_path: pytest temporary directory.
        monkeypatch: pytest monkeypatch fixture.
        capsys: pytest stdout capture.
    """
    constant = tmp_path / "client" / "src" / "lib" / "coverage.ts"
    constant.parent.mkdir(parents=True)
    constant.write_text("export const LATEST_CONFERENCE_YEAR = 2026\n", encoding="utf-8")
    monkeypatch.setattr(uc, "REPO_ROOT", tmp_path / "models")

    uc._warn_if_site_year_is_stale(2026)

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


def test_the_site_year_reminder_names_the_exact_edit_when_the_constant_is_behind(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Being behind is the one case worth interrupting for, so it must be actionable.

    Args:
        tmp_path: pytest temporary directory.
        monkeypatch: pytest monkeypatch fixture.
        capsys: pytest stdout capture.
    """
    constant = tmp_path / "client" / "src" / "lib" / "coverage.ts"
    constant.parent.mkdir(parents=True)
    constant.write_text("export const LATEST_CONFERENCE_YEAR = 2025\n", encoding="utf-8")
    monkeypatch.setattr(uc, "REPO_ROOT", tmp_path / "models")

    uc._warn_if_site_year_is_stale(2026)

    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert "advertises conferences through 2025" in output
    assert "2026" in output
    assert str(constant) in output


def test_a_refused_rerun_does_not_rewrite_a_completed_run_record(tmp_path: Path) -> None:
    """run.json is the rollback manifest for live vectors; a no-op refusal must not mark it failed.

    Args:
        tmp_path: pytest temporary directory.
    """
    record = uc.RunRecord(tmp_path / "run.json", tmp_path / ".tmp")
    record.data["status"] = "completed"
    record.save()

    record.close("failed", uc.EXIT_GUARD, 0.1, "RAIL-6: already completed")

    reloaded = json.loads((tmp_path / "run.json").read_text(encoding="utf-8"))
    assert reloaded["status"] == "completed"
    assert reloaded["refused_invocations"] == 1
    assert "error" not in reloaded
