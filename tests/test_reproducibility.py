"""Test cases for reproducibility of the conference talk indexing pipeline.

This test is the gate between library-upgrade commits: it re-runs load -> split -> id
over committed talk fixtures and compares the result against the chunk ids that are
actually in the production Pinecone index (captured once in expected_chunks.json).

It is deliberately hermetic apart from the embedding calls: the talk html is read from
tests/fixtures/talks, never crawled, and Pinecone is never queried. A talk the website
revises, or an index someone re-builds, must not be able to turn this test red - only
a change in our own code may do that.

How expected_chunks.json was produced, and why you must not regenerate it:
each entry was captured by running load -> split over the committed fixture html and
then confirming, against the live production index, that every regenerated chunk id
was already present on that talk's url. "verified_against_index" records that check.

That flag lives inside the file this test reads, so it certifies nothing on its own.
Regenerating the file from whatever the code currently produces would turn any red
gate green while silently re-baselining the thing being guarded - and the diff would
look like a routine fixture update.

So: a red gate means the pipeline changed. Find out why. The only legitimate reason to
regenerate these expectations is a deliberate, reviewed decision to re-chunk the whole
corpus, which also means re-indexing all ~36,000 vectors.
"""

import inspect
import json
import os
from pathlib import Path
from typing import Any
from typing import cast

import pytest

from models.document import Document
from models.index_utils import get_doc_id
from models.load_conf import load_conference_talk
from models.split_model import MarkdownSyntacticEmbeddingSplitter


FIXTURES_PATH = Path(__file__).parent / "fixtures"
TALKS_PATH = FIXTURES_PATH / "talks"
EXPECTED_PATH = FIXTURES_PATH / "expected_chunks.json"

# the settings the production index was built with - changing either re-chunks everything
SPLIT_THRESHOLD = 0.83
MAX_CHARS = 2000

# how many mismatching chunks to describe before truncating the failure report
MAX_REPORTED_MISMATCHES = 5

SKIP_REASON = (
    "VOYAGE_API_KEY is not set, so the voyage-01 embeddings the splitter needs are unavailable; "
    "run 'set -a; . ./.env; set +a' before pytest to enable this test"
)


def _read_json(path: Path) -> dict[str, Any]:
    """Read a json object from a file.

    Args:
        path: path of the file to read.

    Returns:
        The parsed json object.
    """
    with open(path, encoding="utf8") as f:
        return cast(dict[str, Any], json.load(f))


EXPECTED_CHUNKS = _read_json(EXPECTED_PATH)
TALK_FILENAMES = sorted(EXPECTED_CHUNKS)


@pytest.fixture(scope="module")
def splitter() -> MarkdownSyntacticEmbeddingSplitter:
    """Fixture for the splitter the production index was built with.

    Module-scoped because constructing it loads spacy.

    Built with no arguments on purpose: the pipeline uses the defaults, so a changed
    default must re-chunk here too. test_splitter_defaults_are_unchanged pins the
    values themselves, so a default change fails loudly instead of silently.

    Returns:
        A splitter configured exactly as the indexing pipeline configures it.
    """
    return MarkdownSyntacticEmbeddingSplitter()


def _regenerate_chunks(talk_splitter: MarkdownSyntacticEmbeddingSplitter, filename: str) -> list[Document]:
    """Load a committed talk fixture from disk and split it into chunks.

    Args:
        talk_splitter: the splitter to split the loaded talk with.
        filename: name of the fixture file in tests/fixtures/talks.

    Returns:
        The chunks the pipeline produces for the talk, in order.
    """
    page = _read_json(TALKS_PATH / filename)
    doc = load_conference_talk(page["url"], page["html"])
    return list(talk_splitter.transform_documents([doc]))


def _describe_chunk(chunk_ids: list[str], anchors: list[str], lengths: list[int], ix: int) -> str:
    """Describe one chunk of a side of the comparison.

    Args:
        chunk_ids: chunk ids of this side, in order.
        anchors: chunk anchors of this side, in order.
        lengths: chunk text lengths of this side, in order.
        ix: index of the chunk to describe.

    Returns:
        A one-line description, or "(missing)" if this side has no chunk at ix.
    """
    if ix >= len(chunk_ids):
        return "(missing)"
    return f"id={chunk_ids[ix]} anchor={anchors[ix]!r} chars={lengths[ix]}"


def _compare_chunks(filename: str, expected: dict[str, Any], chunks: list[Document]) -> list[str]:
    """Compare regenerated chunks against the expectations captured from the production index.

    Args:
        filename: name of the fixture file, used to label the report.
        expected: the expected_chunks.json entry for this talk.
        chunks: the chunks the pipeline just regenerated, in order.

    Returns:
        A list of human readable problem lines, empty when the chunks match.
    """
    expected_ids = cast(list[str], expected["chunk_ids"])
    expected_anchors = cast(list[str], expected["anchors"])
    expected_lengths = cast(list[int], expected["chunk_lengths"])
    actual_ids = [get_doc_id(chunk) for chunk in chunks]
    actual_anchors = [str(chunk.metadata.get("anchor", "")) for chunk in chunks]
    actual_lengths = [len(chunk.page_content) for chunk in chunks]

    problems = []
    if len(actual_ids) != expected["chunk_count"]:
        problems.append(f"  chunk count: expected {expected['chunk_count']}, got {len(actual_ids)}")

    mismatches = 0
    for ix in range(max(len(expected_ids), len(actual_ids))):
        expected_chunk = _describe_chunk(expected_ids, expected_anchors, expected_lengths, ix)
        actual_chunk = _describe_chunk(actual_ids, actual_anchors, actual_lengths, ix)
        if expected_chunk == actual_chunk:
            continue
        mismatches += 1
        if mismatches > MAX_REPORTED_MISMATCHES:
            continue
        label = f"chunk {ix}:"
        problems.append(f"  {label} expected {expected_chunk}")
        problems.append(f"  {' ' * len(label)} actual   {actual_chunk}")
        if ix < len(chunks):
            problems.append(f"  {' ' * len(label)} actual text starts: {chunks[ix].page_content[:80]!r}")
    if mismatches > MAX_REPORTED_MISMATCHES:
        problems.append(f"  ... and {mismatches - MAX_REPORTED_MISMATCHES} more mismatching chunks")

    if problems:
        problems.insert(0, f"{filename} ({expected['url']}) no longer reproduces the indexed chunks:")
    return problems


def test_splitter_defaults_are_unchanged() -> None:
    """It checks the splitter defaults still match what the production index was built with.

    The reproducibility test builds the splitter with no arguments, so this is what
    turns a changed default into a legible failure rather than a wall of chunk diffs.
    """
    signature = inspect.signature(MarkdownSyntacticEmbeddingSplitter.__init__)
    actual = {
        "split_threshold": signature.parameters["split_threshold"].default,
        "max_chars": signature.parameters["max_chars"].default,
    }
    assert actual == {"split_threshold": SPLIT_THRESHOLD, "max_chars": MAX_CHARS}, (
        f"the splitter defaults changed to {actual}; the production index was built with "
        f"split_threshold={SPLIT_THRESHOLD}, max_chars={MAX_CHARS}. Re-chunking the whole "
        "corpus is the only way to change these safely."
    )


def test_every_talk_fixture_is_pinned() -> None:
    """It checks that every committed talk fixture has an entry in expected_chunks.json."""
    on_disk = sorted(path.name for path in TALKS_PATH.glob("*.json"))
    assert on_disk == TALK_FILENAMES, (
        "tests/fixtures/talks and tests/fixtures/expected_chunks.json disagree: "
        f"only on disk {sorted(set(on_disk) - set(TALK_FILENAMES))}, "
        f"only expected {sorted(set(TALK_FILENAMES) - set(on_disk))}"
    )


def test_the_gate_is_not_silently_skipped_in_ci() -> None:
    """It fails when CI would skip the reproducibility checks for want of a key.

    Skipping is the right behaviour on a laptop without credentials. In CI it is not:
    a dependency bump would go green having never re-derived a single chunk id, which
    is the one thing this file exists to prevent. So on CI a missing key is a failure,
    and a loud one, rather than seven quiet skips in the summary.
    """
    if not os.environ.get("CI"):
        pytest.skip("not running in CI")
    if "VOYAGE_API_KEY" not in os.environ:
        pytest.fail(
            "VOYAGE_API_KEY is not available to CI, so the reproducibility checks below "
            "would skip and this run would prove nothing about chunk stability.\n"
            "Add it once with:  gh secret set VOYAGE_API_KEY --repo iloveconference/models\n"
            "then pass it to the nox step as an env var.",
            pytrace=False,
        )


@pytest.mark.network
@pytest.mark.skipif("VOYAGE_API_KEY" not in os.environ, reason=SKIP_REASON)
@pytest.mark.parametrize("filename", TALK_FILENAMES)
def test_talk_chunks_are_reproducible(splitter: MarkdownSyntacticEmbeddingSplitter, filename: str) -> None:
    """It regenerates the chunk ids, chunk count, and anchors that are in the production index.

    Args:
        splitter: the production splitter, built once for the module.
        filename: name of the talk fixture to regenerate, one test per talk.
    """
    expected = EXPECTED_CHUNKS[filename]
    assert expected["verified_against_index"], f"{filename} was never cross-checked against the production index"

    chunks = _regenerate_chunks(splitter, filename)
    problems = _compare_chunks(filename, expected, chunks)
    if problems:
        pytest.fail("\n".join(problems), pytrace=False)


@pytest.mark.parametrize("filename", TALK_FILENAMES)
def test_talk_metadata_is_reproducible(filename: str) -> None:
    r"""It checks the loader still produces the title and url the index was built from.

    get_doc_id hashes only url and text, but index_utils embeds f"{title}\n\ntext", so a
    loader change that corrupts the title would move every vector while leaving every
    chunk id intact. Needs no network, so it runs even when the embedding test skips.

    Args:
        filename: name of the talk fixture to load, one test per talk.
    """
    expected = EXPECTED_CHUNKS[filename]
    page = _read_json(TALKS_PATH / filename)
    doc = load_conference_talk(str(page["url"]), str(page["html"]))

    assert doc.metadata["title"] == expected["title"], (
        f"{filename}: loader title changed from {expected['title']!r} to {doc.metadata['title']!r}; "
        "this changes the embedded text without changing any chunk id"
    )
    assert doc.metadata["url"] == expected["url"]
    assert doc.metadata["author"], f"{filename}: loader produced an empty author"
    assert doc.page_content, f"{filename}: loader produced empty content"
