"""Add one General Conference to the production Pinecone index.

This command replaces the four-notebook sequence 05 -> 15 -> 25 -> 35 with a single
resumable run::

    poetry run python -m models.update_conference --year 2025 --month 10

Every stage writes its output under ``data/update/<year>-<month>/`` and records what it
did in ``run.json``, so a crash resumes instead of restarting and a completed run leaves
behind the exact list of vector ids it wrote. Nothing is reimplemented here: the crawl,
load, split, embed, and upsert steps all call the same functions the notebooks called,
so chunk ids and embeddings match the 35,454 vectors already in the index.

Safety rails, in the order they fire. Only rail 6 answers to ``--force``; the exit code
names which one refused, so a wrapper can tell a typo from a destructive refusal:

- rail 1, exit 10 -- the conference is older than 2023-10.
- rail 2a, exit 20 -- no production Pinecone key can be resolved.
- rail 2b, exit 21 -- the resolved key does not reach the expected index.
- rail 3, exit 30 -- the talk count is outside 30..60.
- rail 4 -- a url predicate rather than an abort; its failures surface through rail 3.
- rail 5, exit 50 -- the loader dropped talks, or produced none at all.
- rail 6, exit 60 -- the conference is already in the index. ``--force`` overrides this one.
- rail 7, exit 70/71 -- the key cannot write, or a canary could not be removed.
- rail 8, exit 80 -- a chunk's text is not found in the talk it is attributed to.

Rail 1 is the one that matters most. Vectors indexed before 2023-10 use integer ids, so
the content-hash ids this script writes cannot overwrite them - a run there would add
duplicates silently. No flag reaches that guard.
"""

import hashlib
import json
import os
import re
import subprocess  # nosec B404
import sys
import time
import traceback
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import Any
from typing import Iterable
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import cast
from urllib.parse import parse_qs
from urllib.parse import urljoin
from urllib.parse import urlsplit
from urllib.parse import urlunsplit

import click
import numpy as np
import voyageai  # type: ignore
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from numpy.typing import NDArray
from pinecone import Pinecone
from pinecone import RetryConfig
from pinecone.errors import ApiError
from pinecone.errors import ForbiddenError
from pinecone.errors import NotFoundError
from pinecone.errors import UnauthorizedError
from pinecone.exceptions import PineconeException

from models.crawl_utils import get_page
from models.crawl_utils import save_page
from models.document import Document
from models.index_utils import EMBEDDING_MODEL
from models.index_utils import OpenAIEmbedder
from models.index_utils import embed_documents
from models.index_utils import get_doc_id
from models.index_utils import index_documents
from models.load_conf import ConferenceTalkLoader
from models.load_utils import load_docs_from_jsonl
from models.load_utils import save_docs_to_jsonl
from models.split_utils import clean_text


# --- the production index -------------------------------------------------------------
# Addressed by host, never by name: a key for some other project that happens to hold an
# index of the same name would resolve by name and silently succeed into the wrong place.
INDEX_NAME = "conf-ada-002-svrless"
INDEX_HOST = "https://conf-ada-002-svrless-29e6444.svc.aped-4627-b74a.pinecone.io"
INDEX_DIM = 1536
INDEX_METRIC = "cosine"
# The data plane calls this namespace "", describe_index_stats reports it as "__default__".
NAMESPACE = ""
# A floor and a ceiling, not an equality: the count grows by ~300 per conference.
MIN_INDEXED_VECTORS = 35_000
MAX_INDEXED_VECTORS = 60_000

# --- the conference -------------------------------------------------------------------
HOST = "https://www.churchofjesuschrist.org"
HOST_NETLOC = "www.churchofjesuschrist.org"
# Content-hash ids cannot overwrite the integer ids used before this conference.
EARLIEST = (2023, 10)
MIN_TALKS = 30
MAX_TALKS = 60
VALID_MONTHS = ("04", "10")

# --- the pipeline ---------------------------------------------------------------------
SCHEMA_VERSION = 1
UPSERT_BATCH_SIZE = 100  # ~1.0 MB decoded, 24% of the 4 MiB server cap
EMBED_BATCH_SIZE = 100
EMBED_DELAY = 1.0
SPLIT_THRESHOLD = 0.83
MAX_CHARS = 2000
ANCHOR = "anchor"
PARAGRAPH_EMBEDDER = "voyage-01"
# The nine keys index_documents produces and server/server/main.py reads unguarded.
METADATA_KEYS = frozenset({"year", "month", "url", "title", "author", "author_role", "anchor", "source", "text"})
# A fingerprint change invalidates every cached split shard, not just the touched ones.
FINGERPRINT_MODULES = (
    "document.py",
    "index_utils.py",
    "load_conf.py",
    "load_utils.py",
    "split_model.py",
    "split_model_train.py",
    "split_utils.py",
)
MIN_CHUNKS_PER_TALK = 3.0
MAX_CHUNKS_PER_TALK = 25.0

# --- the write-permission probe ---------------------------------------------------------
CANARY_ID = "__canary__"
UPDATE_PROBE_ID = "__update_probe__"
SETTLE_POLL_SECONDS = 5.0
SETTLE_TIMEOUT_SECONDS = 60.0

# --- paths ------------------------------------------------------------------------------
PACKAGE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_DIR.parent
SIBLING_ENV = REPO_ROOT.parent / "server" / ".env"

# --- exit codes ---------------------------------------------------------------------------
# 0 success or dry run, 1 unexpected exception, 2 click usage error. 3 is a guard refusal
# with nothing written; 4 means some batches landed and a human must look. Everything from
# 10 up names the specific rail that refused, so a wrapper can tell a typo from a refusal.
EXIT_OK = 0
EXIT_UNEXPECTED = 1
EXIT_GUARD = 3
EXIT_PARTIAL_UPSERT = 4
EXIT_ERA = 10
EXIT_NO_KEY = 20
EXIT_WRONG_INDEX = 21
EXIT_TALK_COUNT = 30
EXIT_LOADER_SKIPS = 50
EXIT_ALREADY_INDEXED = 60
EXIT_CANARY_REFUSED = 70
EXIT_CANARY_STUCK = 71
EXIT_TEXT_INTEGRITY = 80
EXIT_BAD_EMBEDDINGS = 90


def _probe_vector() -> list[float]:
    """Build the unit vector used by the canary and by filter queries.

    Near-orthogonal to real ada-002 query embeddings (measured abs cosine <= 0.012 against
    a live top-20 floor of ~0.87), so it cannot enter a reader's result set. An all-zero
    vector is not usable: a cosine index rejects it.

    Returns:
        A 1536-element unit vector, reproducible across machines (NEP 19 pins the stream).
    """
    raw: NDArray[np.float64] = np.random.default_rng(0).standard_normal(INDEX_DIM)
    return cast(list[float], (raw / np.linalg.norm(raw)).tolist())


PROBE_VECTOR = _probe_vector()


class _Abort(Exception):
    """A rail refused to continue.

    Attributes:
        code: the process exit code naming which rail refused.
        rail: the rail label printed in the abort banner.
        summary: the one-line summary.
        body: the indented explanation.
    """

    def __init__(self, code: int, rail: str, summary: str, body: str) -> None:
        """Record the refusal.

        Args:
            code: the process exit code naming which rail refused.
            rail: the rail label printed in the abort banner.
            summary: the one-line summary.
            body: the indented explanation.
        """
        super().__init__(code, rail, summary, body)
        self.code = code
        self.rail = rail
        self.summary = summary
        self.body = body


def _abort(code: int, rail: str, summary: str, body: str = "") -> NoReturn:
    """Refuse to continue, naming the rail that refused.

    Args:
        code: the process exit code naming which rail refused.
        rail: the rail label printed in the abort banner.
        summary: the one-line summary.
        body: the indented explanation.

    Raises:
        _Abort: always; main turns it into the banner and the exit code.
    """
    raise _Abort(code, rail, summary, body)


def _sha256(text: str) -> str:
    """Hash a string.

    Args:
        text: the string to hash.

    Returns:
        The hex sha256 digest.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _fingerprint(secret: str) -> str:
    """Summarize a credential so two runs can be compared without exposing it.

    Args:
        secret: the credential.

    Returns:
        The first eight hex characters of its sha256 digest.
    """
    return _sha256(secret)[:8]


def _now() -> str:
    """Return the current UTC time.

    Returns:
        An ISO-8601 timestamp with a trailing Z.
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _duration(seconds: float) -> str:
    """Format an elapsed duration for the transcript.

    Args:
        seconds: the elapsed seconds.

    Returns:
        Either "12.3s" or "10m13s".
    """
    if seconds < 60:
        return f"{seconds:.1f}s"
    return f"{int(seconds) // 60}m{int(seconds) % 60:02d}s"


def _clock(seconds: float) -> str:
    """Format the run clock shown in each stage header.

    Args:
        seconds: seconds since the run started.

    Returns:
        A "(MM:SS)" string.
    """
    return f"({int(seconds) // 60:02d}:{int(seconds) % 60:02d})"


def _code_sha256() -> str:
    """Hash the pipeline modules whose behaviour decides chunk boundaries.

    This is what stops an edit made halfway through a 25-minute run from producing a
    split.jsonl that is half old-code and half new-code: a changed digest invalidates
    every cached shard.

    Returns:
        The hex sha256 digest over the sorted, concatenated module bytes.
    """
    digest = hashlib.sha256()
    for name in sorted(FINGERPRINT_MODULES):
        digest.update((PACKAGE_DIR / name).read_bytes())
    return digest.hexdigest()


def _package_versions() -> dict[str, str]:
    """Collect the versions of the packages that can move a chunk boundary.

    Returns:
        A mapping of distribution name to version, with "unknown" where lookup failed.
    """
    import importlib.metadata as metadata

    versions = {}
    for name in ("openai", "pinecone", "voyageai", "numpy", "spacy", "en-core-web-sm"):
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:  # pragma: no cover - environment dependent
            versions[name] = "unknown"
    return versions


def _git_state() -> dict[str, Any]:
    """Record which commit the run was made from.

    Read-only: this never mutates the working tree or the index.

    Returns:
        A mapping with "git_head" and "git_dirty", both None/False when git is unavailable.
    """
    try:
        head = subprocess.run(  # nosec B603 B607
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        ).stdout.strip()
        status = subprocess.run(  # nosec B603 B607
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):  # pragma: no cover - environment dependent
        return {"git_head": None, "git_dirty": False}
    return {"git_head": head, "git_dirty": bool(status)}


def _atomic_write(path: Path, payload: bytes, tmp_dir: Path) -> None:
    """Write a file so a crash can never leave a half-written one behind.

    The temporary file lives outside the directory the loader scans, because
    ConferenceTalkLoader json-parses every entry it finds in raw/ - a ".part" file there
    would crash it rather than be ignored.

    Args:
        path: the final path.
        payload: the bytes to write.
        tmp_dir: a scratch directory on the same filesystem, outside raw/.
    """
    tmp_dir.mkdir(parents=True, exist_ok=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = tmp_dir / f"{path.name}.tmp"
    tmp_path.write_bytes(payload)
    os.replace(tmp_path, path)


def read_env_file(path: Path) -> dict[str, str]:
    """Parse a .env file into a mapping without touching os.environ.

    Comment lines are skipped before any "=" is looked for. That line is load-bearing:
    server/.env holds a live PINECONE_KEY followed by a commented-out development key of
    the same length, so a regex - or any parser that strips a leading "#" before
    splitting - selects the development key and the whole run succeeds into an empty
    project. load_dotenv is not usable here for the same class of reason: it injects
    unrelated variables into os.environ and lets a stale shell value win over the file.

    Args:
        path: the .env file to read.

    Returns:
        A mapping of name to value; later definitions win, as in sh.
    """
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].lstrip()
        key, sep, value = line.partition("=")
        if not sep:
            continue
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return values


def canonical_url(url: str) -> str:
    """Normalize a talk url to the exact form the index stores.

    get_doc_id hashes ``url + "~" + text``, so a fragment or a reordered query string
    produces a different id and therefore a duplicate vector instead of an idempotent
    overwrite.

    Args:
        url: the url as found on the listing page.

    Returns:
        The url with the fragment dropped and the query normalized to "lang=eng".
    """
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "lang=eng", ""))


def is_talk_url(url: str, year: int, month: str) -> bool:
    """Decide whether a link on the listing page is a talk in this conference.

    Four conditions beyond the notebook's original count-and-suffix test, each closing a
    way the crawl could pick up something that is not a talk of this conference:

    * the host must be churchofjesuschrist.org, since hrefs are resolved with urljoin and
      an absolute off-site link keeps its own netloc;
    * the slug must be non-empty, or "/study/general-conference/2025/10/" - six components
      whose last is "" - is accepted and saved as "2025-10-.json";
    * the path must be under this conference, or "/study/scriptures/bofm/alma/5" is
      accepted and indexed with year="bofm", month="alma";
    * the language must be exactly English, or a "?lang=spa" link maps to the same
      filename as its English twin and whichever is crawled first wins.

    Args:
        url: an absolute url.
        year: the conference year.
        month: the zero-padded conference month.

    Returns:
        True when the url is an English talk page of this conference.
    """
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or parts.netloc != HOST_NETLOC:
        return False
    components = parts.path.split("/")
    if len(components) != 6 or not components[-1] or components[-1].endswith("-session"):
        return False
    if not parts.path.startswith(f"/study/general-conference/{year}/{month}/"):
        return False
    return parse_qs(parts.query).get("lang") == ["eng"]


def talk_stem(url: str) -> str:
    """Build the "<year>-<month>-<slug>" filename stem for a talk.

    Inherited verbatim from notebook 05 cell 4 so files stay interchangeable with
    data/load/raw/. The 2026 slugs are short ("11christofferson"), which the
    path-component logic handles unchanged.

    Args:
        url: a canonical talk url.

    Returns:
        The filename stem, without an extension.

    Raises:
        ValueError: if the slug could escape the data directory.
    """
    year, month, slug = urlsplit(url).path.split("/")[3:6]
    if not slug or "/" in slug or "\\" in slug or ".." in slug:
        raise ValueError(f"refusing to build a path from slug {slug!r} in {url!r}")
    return f"{year}-{month}-{slug}"


def _listing_url(year: int, month: str) -> str:
    """Build the conference listing url.

    Args:
        year: the conference year.
        month: the zero-padded conference month.

    Returns:
        The listing url.
    """
    return f"{HOST}/study/general-conference/{year}/{month}?lang=eng"


def _batch_bounds(total: int, batch_size: int) -> list[tuple[int, int]]:
    """Split a count into the half-open ranges the upsert loop will use.

    Args:
        total: the number of items.
        batch_size: the batch size.

    Returns:
        A list of (start, end) pairs covering 0..total.
    """
    return [(start, min(start + batch_size, total)) for start in range(0, total, batch_size)]


STAGE_NAMES = ("preflight", "crawl", "load", "split", "embed", "upsert")


class RunRecord:
    """The on-disk state machine for one conference.

    Rewritten atomically after every stage transition and on every abort, which is what
    makes it a resume record rather than a receipt: ``status: "failed"`` with the error is
    a valid, expected end state.
    """

    def __init__(self, path: Path, tmp_dir: Path) -> None:
        """Load the record for this conference, or start a new one.

        Args:
            path: the run.json path.
            tmp_dir: the scratch directory atomic writes go through.
        """
        self.path = path
        self.tmp_dir = tmp_dir
        self.data: dict[str, Any] = self._load()

    def _load(self) -> dict[str, Any]:
        """Read the existing record, or build an empty one.

        Returns:
            The run record contents.
        """
        if self.path.exists():
            return cast(dict[str, Any], json.loads(self.path.read_text(encoding="utf-8")))
        return {
            "schema_version": SCHEMA_VERSION,
            "status": "not_started",
            "created_at": _now(),
            "invocations": [],
            "stages": {name: {"status": "not_started"} for name in STAGE_NAMES},
        }

    def save(self) -> None:
        """Write the record to disk atomically."""
        self.data["updated_at"] = _now()
        payload = json.dumps(self.data, indent=2, ensure_ascii=False) + "\n"
        _atomic_write(self.path, payload.encode("utf-8"), self.tmp_dir)

    def stage(self, name: str) -> dict[str, Any]:
        """Return the mutable record of one stage.

        Args:
            name: the stage name.

        Returns:
            The stage's sub-record, created if it was absent.
        """
        stages = cast(dict[str, Any], self.data.setdefault("stages", {}))
        return cast(dict[str, Any], stages.setdefault(name, {"status": "not_started"}))

    def finish_stage(self, name: str, status: str, elapsed: float, **fields: Any) -> None:
        """Mark a stage finished and flush the record.

        Args:
            name: the stage name.
            status: one of the stage status values.
            elapsed: seconds the stage took.
            fields: extra fields to record on the stage.
        """
        stage = self.stage(name)
        stage.update(fields)
        stage["status"] = status
        stage["elapsed_seconds"] = round(elapsed, 1)
        self.save()

    def close(self, status: str, exit_code: int, elapsed: float, error: Optional[str] = None) -> None:
        """Record the outcome of this invocation and flush.

        Args:
            status: the run status.
            exit_code: the process exit code.
            elapsed: seconds the invocation took.
            error: the error description, when the run failed.
        """
        if self.data.get("status") == "completed" and status != "completed":
            # A later invocation that was refused by a guard did no work, so it must not
            # rewrite the record of the run that succeeded. run.json is both the audit
            # trail and the rollback manifest for vectors that are live in production;
            # marking it "failed" would send someone looking for a problem that is not
            # there, or worse, rolling back a good run.
            self.data.setdefault("refused_invocations", 0)
            self.data["refused_invocations"] += 1
            self.save()
            return
        self.data["status"] = status
        self.data["elapsed_seconds"] = round(elapsed, 1)
        if error is not None:
            self.data["error"] = error
        invocations = cast(list[dict[str, Any]], self.data.setdefault("invocations", []))
        if invocations:
            invocations[-1].update({"finished_at": _now(), "outcome": status, "exit_code": exit_code})
        self.save()


@dataclass
class Ctx:
    """Everything one invocation needs, resolved once in stage 0.

    Attributes:
        year: the conference year.
        month: the zero-padded conference month.
        delay: seconds between churchofjesuschrist.org requests.
        dry_run: whether stage 4 is a preview rather than a write.
        allow_skips: how many loader drops to tolerate.
        force: whether the already-indexed guards are overridden.
        write_probe: which write-permission probe to run.
        data_dir: the conference's data directory.
        run: the run record.
        started: the monotonic clock reading when the run began.
        index: the Pinecone index handle, set by stage 0.
        chunk_ids: the planned vector ids, set after stage 3.
    """

    year: int
    month: str
    delay: int
    dry_run: bool
    allow_skips: int
    force: bool
    write_probe: str
    data_dir: Path
    run: RunRecord
    started: float
    index: Any = None
    chunk_ids: list[str] = field(default_factory=list)

    @property
    def key(self) -> str:
        """Return the conference key.

        Returns:
            The "<year>-<month>" key.
        """
        return f"{self.year}-{self.month}"

    @property
    def raw_dir(self) -> Path:
        """Return the directory of crawled talk pages.

        Only talk json may live here: ConferenceTalkLoader json-parses every entry.

        Returns:
            The raw/ directory.
        """
        return self.data_dir / "raw"

    @property
    def tmp_dir(self) -> Path:
        """Return the scratch directory for atomic writes.

        Returns:
            The .tmp/ directory, deliberately outside raw/.
        """
        return self.data_dir / ".tmp"

    @property
    def split_dir(self) -> Path:
        """Return the directory of per-talk split shards.

        Returns:
            The split/ directory.
        """
        return self.data_dir / "split"

    def elapsed(self) -> float:
        """Return how long this invocation has been running.

        Returns:
            Seconds since the run started.
        """
        return time.monotonic() - self.started


def _echo(message: str = "") -> None:
    """Print one transcript line to stdout.

    Args:
        message: the line.
    """
    click.echo(message)


def _warn(message: str) -> None:
    """Print one warning to stderr.

    Args:
        message: the warning.
    """
    click.secho(message, err=True, fg="yellow")


def _header(ctx: Ctx, number: str, name: str) -> float:
    """Print a stage header and return its start time.

    Args:
        ctx: the run context.
        number: the "[n/4]" stage label.
        name: the stage name.

    Returns:
        The monotonic clock reading at the start of the stage.
    """
    _echo(f"{number} {name} ...".ljust(63) + _clock(ctx.elapsed()))
    return time.monotonic()


# ---------------------------------------------------------------------------------------
# Stage 0 - preflight. Never skipped, and deliberately ahead of the crawl: a bad key or a
# read-only key should cost seconds, not the twenty-five minutes of politeness sleep that
# the crawl spends before it would otherwise be discovered.
# ---------------------------------------------------------------------------------------


def check_era(year: int, month: str) -> None:
    """Refuse any conference older than 2023-10.

    No flag reaches this guard, by design. The next person's instinct will be to wire
    --force through it; the reason not to is that the failure it prevents is silent.

    Args:
        year: the conference year.
        month: the zero-padded conference month.
    """
    if (year, int(month)) >= EARLIEST:
        return
    _abort(
        EXIT_ERA,
        "RAIL-1",
        f"{year}-{month} is before {EARLIEST[0]}-{EARLIEST[1]:02d}; this script cannot be pointed at it.",
        "The production index holds two eras. Talks from 1980-04 through 2023-04\n"
        '(~34,300 vectors) were indexed with integer ids such as "31191", and were\n'
        "embedded on their text alone. Talks from 2023-10 onward (~1,150 vectors) use\n"
        'content-hash ids - sha256(url + "~" + chunk_text) - and are embedded on\n'
        '"title\\n\\ntext".\n'
        "\n"
        "This script only knows how to write content-hash ids. A content hash can\n"
        f"never equal an integer id, so nothing it writes would overwrite the existing\n"
        f"{year}-{month} vectors. It would ADD a second, differently-embedded copy of every\n"
        "chunk of every talk in that conference, permanently, with no record of which\n"
        "copy is which. There is no undo: the old ids are not recoverable from the\n"
        "new ones.\n"
        "\n"
        "Re-indexing a pre-2023-10 conference requires deleting its existing vectors\n"
        "first, which is a separate, deliberate operation that this script does not\n"
        "perform and must not be taught to perform. Vectors before 2023-10 use integer\n"
        "ids and were embedded on the chunk text alone; everything after uses a sha256\n"
        "of url+text and embeds title+text. A content-hash id cannot overwrite an\n"
        "integer one, so a run here would silently duplicate rather than replace.\n"
        "\n"
        "--force does not override this.\n"
        "Nothing was read, crawled, or written. Exiting.",
    )


def check_plausible_year(year: int) -> None:
    """Refuse a year that cannot be a conference yet.

    Args:
        year: the conference year.
    """
    latest = datetime.now(timezone.utc).year + 1
    if year <= latest:
        return
    _abort(
        EXIT_ERA,
        "RAIL-1",
        f"{year} is not a plausible conference year.",
        f"The latest conference this script will accept is {latest}. This looks like a\n"
        "typo in --year. --force does not override this.\n"
        "Nothing was read, crawled, or written. Exiting.",
    )


def resolve_pinecone_key() -> tuple[str, str]:
    """Resolve the production Pinecone key.

    models/.env's PINECONE_API_KEY is never consulted and must not be added as a third
    source: it is a development-project key, and using it would make every stage appear
    to succeed while writing into a project the live site never queries.

    Returns:
        The key and a short description of where it came from.
    """
    from_env = os.environ.get("PINECONE_PROD_KEY", "").strip()
    if from_env:
        return from_env, "$PINECONE_PROD_KEY"
    reason = f"file not found at {SIBLING_ENV}"
    if SIBLING_ENV.exists():
        value = read_env_file(SIBLING_ENV).get("PINECONE_KEY", "").strip()
        if value:
            return value, "server/.env:PINECONE_KEY"
        reason = (
            f"{SIBLING_ENV} exists, but defines no PINECONE_KEY\n"
            "                                     (only commented-out ones were found)"
        )
    _abort(
        EXIT_NO_KEY,
        "RAIL-2a",
        "No production Pinecone key found.",
        "Looked, in order:\n"
        "  1. $PINECONE_PROD_KEY            - not set (or empty)\n"
        f"  2. {reason}\n"
        "\n"
        "models/.env's PINECONE_API_KEY is deliberately NOT a fallback: it is a\n"
        "development-project key. Using it would make every stage of this run appear\n"
        "to succeed while writing ~300 vectors into a project the live site never\n"
        "queries - the single worst outcome available here, because it looks like\n"
        "success.\n"
        "\n"
        "Fix: export PINECONE_PROD_KEY=..., or restore PINECONE_KEY in server/.env.\n"
        "Nothing was crawled or written. Exiting.",
    )


def _describe_stats(index: Any, fingerprint: str, source: str) -> Any:
    """Read index stats, translating an auth failure into the rail-2b message.

    Args:
        index: the Pinecone index handle.
        fingerprint: the key fingerprint, for the abort message.
        source: where the key came from, for the abort message.

    Returns:
        The describe_index_stats response.
    """
    try:
        return index.describe_index_stats()
    except (UnauthorizedError, ForbiddenError) as error:
        _abort(
            EXIT_WRONG_INDEX,
            "RAIL-2b",
            "The resolved Pinecone key does not reach the expected index.",
            f"key source:  {source}  (fingerprint {fingerprint})\n"
            f"target host: {INDEX_HOST}\n"
            "\n"
            f"Pinecone rejected the key: {error.status_code} {type(error).__name__}.\n"
            "This key has no access to the production index - it is most likely the\n"
            "development key from models/.env. Exiting.",
        )


def check_index_identity(stats: Any, fingerprint: str, source: str) -> None:
    """Refuse unless the handle really is the production conference index.

    Args:
        stats: the describe_index_stats response.
        fingerprint: the key fingerprint, for the abort message.
        source: where the key came from, for the abort message.
    """
    total = int(stats.total_vector_count)
    problems = (
        stats.dimension != INDEX_DIM,
        stats.metric != INDEX_METRIC,
        not MIN_INDEXED_VECTORS <= total <= MAX_INDEXED_VECTORS,
    )
    if not any(problems):
        return
    _abort(
        EXIT_WRONG_INDEX,
        "RAIL-2b",
        "The resolved Pinecone key does not reach the expected index.",
        f"key source:   {source}  (fingerprint {fingerprint})\n"
        f"target host:  {INDEX_HOST}\n"
        "\n"
        "  expected                      actual\n"
        f"    dimension  {INDEX_DIM:<18} {stats.dimension}\n"
        f"    metric     {INDEX_METRIC:<18} {stats.metric}\n"
        f"    vectors    {f'{MIN_INDEXED_VECTORS:,}..{MAX_INDEXED_VECTORS:,}':<18} {total:,}\n"
        "\n"
        "This is not the production conference index. Writing to it would index this\n"
        "conference somewhere the live site never reads, and the run would otherwise\n"
        "report success. Check which key is in $PINECONE_PROD_KEY / server/.env.\n"
        "Nothing was crawled or written. Exiting.",
    )


def _check_control_plane(client: Any) -> None:
    """Best-effort check that the key's project really holds this host.

    Catches a valid key belonging to a different project that happens to hold an index of
    the same name. The check is best-effort on purpose: addressing the index by host means
    the key never needs control-plane scope, so a key that cannot call describe_index is
    usable and must not be refused for that alone. The data-plane assertions in
    check_index_identity are the substantive ones.

    Args:
        client: the Pinecone client.
    """
    try:
        model = client.describe_index(INDEX_NAME)
    except ApiError as error:  # pragma: no cover - depends on the key's scope
        _warn(f"      note: control-plane describe_index unavailable ({error.status_code}); host not cross-checked")
        return
    actual = str(model.host).removeprefix("https://")
    if actual != INDEX_HOST.removeprefix("https://"):
        _abort(
            EXIT_WRONG_INDEX,
            "RAIL-2b",
            f"The key's project resolves {INDEX_NAME} to a different host.",
            f"expected host: {INDEX_HOST.removeprefix('https://')}\n"
            f"actual host:   {actual}\n"
            "\n"
            "A key for a different project holds an index of the same name. Writing to\n"
            "it would index this conference where the live site never reads. Exiting.",
        )
    _echo(f"      index {INDEX_NAME}: deletion_protection={getattr(model, 'deletion_protection', 'unknown')}")


def _metadata_hits(index: Any, year: int, month: str) -> int:
    """Count indexed vectors already carrying this conference's metadata.

    year and month are stored as zero-padded strings, so the filter must compare against
    strings. An int comparison silently returns zero hits, which would make this guard
    fail open and let the script double-index a conference.

    fetch_by_metadata is an exact metadata lookup and needs no probe vector; a filtered
    serverless query is an approximate search, and so is used only as a fallback.

    Args:
        index: the Pinecone index handle.
        year: the conference year.
        month: the zero-padded conference month.

    Returns:
        The number of matching vectors found, capped by the lookup limit.
    """
    metadata_filter = {"year": {"$eq": str(year)}, "month": {"$eq": month}}
    try:
        response = index.fetch_by_metadata(filter=metadata_filter, namespace=NAMESPACE, limit=5)
        return len(response.vectors)
    except ApiError:  # pragma: no cover - only when the server rejects the exact lookup
        matches = index.query(
            vector=PROBE_VECTOR,
            top_k=5,
            namespace=NAMESPACE,
            filter={"year": str(year), "month": month},
            include_metadata=True,
        ).matches
        return len(matches)


def check_not_already_indexed(ctx: Ctx, hits: int) -> None:
    """Refuse a conference the index already holds, unless --force.

    Args:
        ctx: the run context.
        hits: how many vectors the metadata lookup found.
    """
    if hits == 0:
        return
    if ctx.force:
        _warn(f"      --force: {ctx.key} already has vectors in the index; continuing anyway")
        return
    _abort(
        EXIT_ALREADY_INDEXED,
        "RAIL-6",
        f"{ctx.key} already has vectors in the production index.",
        f"A metadata filter on {{year: {str(ctx.year)!r}, month: {ctx.month!r}}} returned {hits} matches.\n"
        "\n"
        "This script is meant to be run once per conference. It has no --replace mode\n"
        "and does not handle revised talks: a talk whose text has changed since it was\n"
        "indexed produces new chunk ids, so re-running would ADD the new chunks and\n"
        "leave the old ones orphaned in the index rather than replacing them.\n"
        "\n"
        "If a previous run crashed part-way through and you are resuming it, re-run\n"
        "with --force. Re-upserting a chunk whose text is unchanged writes the same\n"
        "id and is harmless.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def _canary_metadata() -> dict[str, str]:
    """Build the canary's metadata.

    All nine keys, all strings. server/server/main.py subscripts eight of them unguarded
    over every match, and its middleware turns any exception into a blanket 500 - so a
    metadata-less vector that ever ranked would fail the whole search request, not just
    one result. The sentinel year and month mean a leaked canary can never be returned by
    a real {year, month} filter, nor trip rail 6 for any conference.

    Returns:
        The canary metadata.
    """
    return {
        "title": "__canary__ write permission test",
        "text": "__canary__ write permission test - not conference content",
        "author": "__canary__",
        "author_role": "__canary__",
        "year": "0000",
        "month": "00",
        "url": "https://example.invalid/__canary__",
        "anchor": "",
        "source": CANARY_ID,
    }


def _delete_canary(index: Any) -> None:
    """Delete the canary vector.

    This is the only delete call site in this module, and it passes a literal
    single-element id list. deletion_protection is disabled on this index, so there is
    nothing between a stray delete_all or a filter delete and the irrecoverable loss of
    all 35,454 vectors. Never add delete_all. Never add filter.

    Args:
        index: the Pinecone index handle.
    """
    index.delete(ids=[CANARY_ID], namespace=NAMESPACE)


def sweep_stale_canary(ctx: Ctx) -> None:
    """Remove a canary a previous run left behind.

    try/finally covers an exception and a Ctrl-C, but not a SIGKILL, a power loss, or a
    container eviction. This sweep is what covers those, and it is why the canary has a
    fixed id rather than a random one. It runs before the already-indexed guard: a
    leftover canary carrying this conference's metadata would otherwise trip rail 6.

    Args:
        ctx: the run context.
    """
    leftover = ctx.index.fetch(ids=[CANARY_ID], namespace=NAMESPACE).vectors
    if not leftover:
        return
    if ctx.dry_run:
        _warn(f"      a stale {CANARY_ID} vector is in the index; a real run would remove it")
        return
    _warn(f"      removing a stale {CANARY_ID} vector left by an earlier run")
    _delete_canary(ctx.index)
    if CANARY_ID in ctx.index.fetch(ids=[CANARY_ID], namespace=NAMESPACE).vectors:  # pragma: no cover - network
        _abort(
            EXIT_CANARY_STUCK,
            "RAIL-7",
            "A stale canary vector could not be removed.",
            f"Remove it manually: index.delete(ids=[{CANARY_ID!r}], namespace='')\n"
            "Do NOT pass delete_all or a filter: deletion protection is disabled on this\n"
            "index. The conference was NOT indexed. Re-run after the canary is gone.",
        )


def _probe_refused(error: ApiError, fingerprint: str, source: str) -> NoReturn:
    """Report that the key cannot write.

    Args:
        error: the error Pinecone returned.
        fingerprint: the key fingerprint.
        source: where the key came from.
    """
    _abort(
        EXIT_CANARY_REFUSED,
        "RAIL-7",
        "The production Pinecone key cannot write to the index.",
        f"the write-permission probe returned {error.status_code} {type(error).__name__}\n"
        "\n"
        f"key source:  {source}  (fingerprint {fingerprint})\n"
        f"index:       {INDEX_NAME} (host ...29e6444...)\n"
        "\n"
        "This key has only ever been used read-only by the server, so it may be\n"
        "scoped ReadOnly. Issue a key with write access in the Pinecone console and\n"
        "supply it via $PINECONE_PROD_KEY.\n"
        "\n"
        "Caught before the crawl and before a single embedding was purchased.\n"
        "No canary vector was left in the index. Exiting.",
    )


def _run_canary(ctx: Ctx, fingerprint: str, source: str) -> None:
    """Write a throwaway vector, confirm it, and remove it.

    It really does put a vector in production for about a second, which is why
    run_update_probe is the default: that proves the same thing without writing.

    Args:
        ctx: the run context.
        fingerprint: the key fingerprint, for the abort message.
        source: where the key came from, for the abort message.
    """
    wrote = False
    try:
        ctx.index.upsert(vectors=[(CANARY_ID, PROBE_VECTOR, _canary_metadata())], namespace=NAMESPACE)
        wrote = True
        if CANARY_ID not in ctx.index.fetch(ids=[CANARY_ID], namespace=NAMESPACE).vectors:
            _abort(
                EXIT_CANARY_REFUSED,
                "RAIL-7",
                "The canary upsert reported success but the vector is not readable.",
                "Something between this process and the index is not doing what it says.\n"
                "Nothing was crawled or indexed. Exiting.",
            )
    except (ForbiddenError, UnauthorizedError) as error:
        _probe_refused(error, fingerprint, source)
    finally:
        if wrote:
            _remove_canary(ctx)


def _remove_canary(ctx: Ctx) -> None:
    """Delete the canary, retrying, and refuse to continue if it survives.

    Args:
        ctx: the run context.
    """
    for _attempt in range(3):
        _delete_canary(ctx.index)
        if CANARY_ID not in ctx.index.fetch(ids=[CANARY_ID], namespace=NAMESPACE).vectors:
            return
        time.sleep(2)
    _abort(
        EXIT_CANARY_STUCK,
        "RAIL-7",
        "A canary vector was written and could NOT be removed.",
        f"id:        {CANARY_ID}\n"
        'namespace: "" (the namespace the live site queries)\n'
        f"index:     {INDEX_NAME}\n"
        "\n"
        "Three delete attempts were made; the vector is still readable.\n"
        "\n"
        "It carries a full, valid 9-key metadata set, so it cannot break the /search\n"
        "handler, and its vector is near-orthogonal to real query embeddings\n"
        "(|cos| <= 0.012 vs a top-20 floor of ~0.87), so it will not surface in\n"
        "results. It is inert - but it must not be left in production.\n"
        "\n"
        f"Remove it manually:\n    index.delete(ids=[{CANARY_ID!r}], namespace='')\n"
        "Do NOT pass delete_all or a filter: deletion protection is disabled on this\n"
        "index.\n"
        "\n"
        "The conference was NOT indexed. Re-run after the canary is gone.",
    )


def _run_update_probe(ctx: Ctx, fingerprint: str, source: str) -> None:
    """Prove the key can write without writing anything.

    An update against an id that cannot exist is a no-op at the server, so no vector is
    ever created - but the request still traverses the data-plane write path, and a
    read-only key still returns 403. Same signal as the canary above, none of its
    exposure.

    Args:
        ctx: the run context.
        fingerprint: the key fingerprint, for the abort message.
        source: where the key came from, for the abort message.
    """
    try:
        ctx.index.update(id=UPDATE_PROBE_ID, set_metadata={"probe": "1"}, namespace=NAMESPACE)
    except (ForbiddenError, UnauthorizedError) as error:
        _probe_refused(error, fingerprint, source)
    except NotFoundError:  # pragma: no cover - serverless may 404 an update to a missing id
        # The write was accepted and found nothing to update, which still proves the key
        # may write. Only a 401/403 means refused.
        pass


def run_write_probe(ctx: Ctx, fingerprint: str, source: str) -> str:
    """Check that the key may write, in whichever way the operator chose.

    Args:
        ctx: the run context.
        fingerprint: the key fingerprint, for the abort message.
        source: where the key came from, for the abort message.

    Returns:
        What the probe did, for the run record.
    """
    if ctx.dry_run:
        return "skipped_dry_run"
    if ctx.write_probe == "skip":
        _warn("      write permission: NOT TESTED (--write-probe=skip)")
        return "skipped"
    if ctx.write_probe == "canary":
        _run_canary(ctx, fingerprint, source)
    else:
        _run_update_probe(ctx, fingerprint, source)
    _echo(f"      write permission: ok ({ctx.write_probe} probe)")
    return f"ok:{ctx.write_probe}"


def check_no_completed_run(ctx: Ctx) -> None:
    """Refuse to re-run a conference this directory already completed.

    Args:
        ctx: the run context.
    """
    if ctx.run.data.get("status") != "completed":
        return
    if ctx.force:
        _warn(f"      --force: {ctx.run.path} records a completed run; continuing anyway")
        return
    _abort(
        EXIT_GUARD,
        "RAIL-6",
        f"{ctx.run.path} records a completed run for {ctx.key}.",
        "This conference has already been indexed by this script. Re-running would\n"
        "re-upsert the same ids, which is harmless, or add new ids for any talk whose\n"
        "text has changed since - which is not.\n"
        "\n"
        "Pass --force if you are deliberately resuming or repairing that run.\n"
        "Nothing was crawled or written. Exiting.",
    )


def stage_preflight(ctx: Ctx, key: str, source: str) -> None:
    """Run stage 0: prove the target is right and reachable before spending anything.

    Args:
        ctx: the run context.
        key: the production Pinecone key.
        source: where the key came from.
    """
    started = _header(ctx, "[0/4]", "preflight")
    fingerprint = _fingerprint(key)
    client = Pinecone(api_key=key, retry_config=RetryConfig(max_retries=5, max_wait=60.0))
    ctx.index = client.index(host=INDEX_HOST)

    stats = _describe_stats(ctx.index, fingerprint, source)
    check_index_identity(stats, fingerprint, source)
    _echo(f"      index holds {int(stats.total_vector_count):,} vectors, dim {stats.dimension}")
    _check_control_plane(client)

    sweep_stale_canary(ctx)
    hits = _metadata_hits(ctx.index, ctx.year, ctx.month)
    _echo(f"      {ctx.key} already indexed? {'YES' if hits else 'no'} ({hits} metadata hits)")
    check_not_already_indexed(ctx, hits)

    probe = run_write_probe(ctx, fingerprint, source)
    elapsed = time.monotonic() - started
    ctx.run.finish_stage(
        "preflight",
        "completed",
        elapsed,
        index_total_before=int(stats.total_vector_count),
        index_dimension=int(stats.dimension),
        index_metric=str(stats.metric),
        existing_conference_hits=hits,
        write_probe=probe,
    )
    _echo(f"      done in {_duration(elapsed)}")


# ---------------------------------------------------------------------------------------
# Stage 1 - crawl.
# ---------------------------------------------------------------------------------------


def check_talk_count(count: int, what: str, detail: str) -> None:
    """Refuse a talk count outside the range every real conference has fallen in.

    The floor stops a half-published conference from being indexed as a complete one -
    which would pass every other guard and report success. The ceiling is politeness
    insurance: if the url predicate ever regresses to matching broadly, this aborts
    immediately instead of queueing hundreds of requests at --delay seconds apiece.

    Args:
        count: the number of talks found.
        what: what was counted, for the message.
        detail: extra context lines for the message.
    """
    if MIN_TALKS <= count <= MAX_TALKS:
        return
    bound = "below the floor of" if count < MIN_TALKS else "above the ceiling of"
    limit = MIN_TALKS if count < MIN_TALKS else MAX_TALKS
    _abort(
        EXIT_TALK_COUNT,
        "RAIL-3",
        f"{what} yielded {count} talks, {bound} {limit}.",
        f"{detail}\n"
        "\n"
        "Recent conferences publish 35-38 talks (2025-10: 35, 2026-04: 37, 2026-10: 38).\n"
        "A count this far off means the conference is only partly published, the page\n"
        "was served as a JavaScript shell, or the markup changed. Indexing a subset as\n"
        "a complete conference would leave the gap invisible: every later check would\n"
        "pass and the run would report success.\n"
        "\n"
        "Re-run once the conference is fully posted. --force does not override this.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def extract_talk_urls(html: str, listing_url: str, year: int, month: str) -> tuple[list[str], int, int, list[str]]:
    """Pull this conference's talk urls out of the listing page.

    Every talk is linked twice on a real listing page, so the floor must be applied to
    the deduplicated set: on the live 2025-10 listing the predicate matches 70 links for
    35 talks, and a count check on the raw list would pass with only 15 real talks.

    Args:
        html: the listing page html.
        listing_url: the url the page came from, for resolving relative hrefs.
        year: the conference year.
        month: the zero-padded conference month.

    Returns:
        The unique canonical talk urls, the number of anchors seen, the number of links
        matched, and up to five near misses that the hardened conditions rejected.
    """
    soup = BeautifulSoup(html, "html.parser")
    hrefs = [urljoin(listing_url, str(a["href"])) for a in soup.find_all("a", href=True)]
    matched = [url for url in hrefs if is_talk_url(url, year, month)]
    near_misses = []
    for url in hrefs:
        components = urlsplit(url).path.split("/")
        if len(components) == 6 and not components[-1].endswith("-session") and not is_talk_url(url, year, month):
            near_misses.append(url)
    unique: list[str] = []
    for url in matched:
        canonical = canonical_url(url)
        if canonical not in unique:
            unique.append(canonical)
    return unique, len(hrefs), len(matched), near_misses[:5]


def _check_listing_unchanged(ctx: Ctx, talk_urls: list[str]) -> None:
    """Refuse when the listing has changed since the crawl that filled raw/.

    This is what catches a conference that was half-published at first crawl and has
    since grown; the cached raw/ would otherwise stay silently incomplete forever.

    Args:
        ctx: the run context.
        talk_urls: the urls the fresh listing yielded.
    """
    cached = ctx.run.stage("crawl").get("talk_urls")
    if not cached or set(cached) == set(talk_urls):
        return
    added = sorted(set(talk_urls) - set(cached))
    removed = sorted(set(cached) - set(talk_urls))
    detail = "\n".join([f"  + {url}" for url in added] + [f"  - {url}" for url in removed])
    if ctx.force:
        _warn(f"      --force: the talk-url listing changed since the last run\n{detail}")
        return
    _abort(
        EXIT_GUARD,
        "RAIL-3",
        "The talk-url listing changed since the last run.",
        f"{detail}\n"
        "\n"
        "raw/ was filled from the earlier listing, so it is now either incomplete or\n"
        "holds a talk the conference no longer lists. Delete the conference directory\n"
        f"({ctx.data_dir}) to crawl it cleanly, or pass --force to accept the new set.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def _raw_file_is_valid(path: Path, url: str) -> bool:
    """Decide whether a cached talk file can be reused.

    Anything but a well-formed file for exactly this url is re-fetched. os.replace makes
    a truncated write impossible going forward; this keeps pre-existing damage from
    becoming a mystery.

    Args:
        path: the raw/ file path.
        url: the url the file should hold.

    Returns:
        True when the file parses and matches.
    """
    if not path.exists():
        return False
    try:
        page = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return bool(page.get("html")) and page.get("url") == url


def _save_talk(ctx: Ctx, url: str, html: str) -> None:
    """Write one crawled talk into raw/ atomically.

    Args:
        ctx: the run context.
        url: the canonical talk url.
        html: the page html.
    """
    ctx.tmp_dir.mkdir(parents=True, exist_ok=True)
    tmp_path = ctx.tmp_dir / f"{talk_stem(url)}.json.part"
    save_page(str(tmp_path), url, html)
    ctx.raw_dir.mkdir(parents=True, exist_ok=True)
    os.replace(tmp_path, ctx.raw_dir / f"{talk_stem(url)}.json")


def _crawl_talks(ctx: Ctx, talk_urls: list[str]) -> tuple[int, int, list[dict[str, Any]]]:
    """Fetch every talk that is not already cached, one at a time.

    Sequential and never concurrent: the delay between requests is the whole point.

    Args:
        ctx: the run context.
        talk_urls: the canonical talk urls to ensure are on disk.

    Returns:
        How many were fetched, how many were reused, and one record per failure.
    """
    todo = [url for url in talk_urls if not _raw_file_is_valid(ctx.raw_dir / f"{talk_stem(url)}.json", url)]
    reused = len(talk_urls) - len(todo)
    eta = len(todo) * ctx.delay
    _echo(f"      {reused} cached, {len(todo)} to fetch at {ctx.delay}s apart -> ~{_duration(eta)}")
    if todo:
        _echo(f"      each fetch is followed by a {ctx.delay}s pause, including the last one")

    failed: list[dict[str, Any]] = []
    fetched = 0
    for position, url in enumerate(talk_urls, start=1):
        label = f"      [{position:>2}/{len(talk_urls)}] {talk_stem(url).split('-', 2)[2]:<28}"
        if url not in todo:
            _echo(f"{label} (cached)")
            continue
        click.echo(label, nl=False)
        status_code, html = get_page(url, delay_seconds=ctx.delay)
        if status_code != 200 or not html:
            _echo(" FAILED")
            _warn(f"      status {status_code} for {url}")
            failed.append({"url": url, "status_code": status_code})
            continue
        _save_talk(ctx, url, html)
        fetched += 1
        _echo(f" {len(html) / 1024:.1f} KB")
    return fetched, reused, failed


def _check_crawl_complete(ctx: Ctx, talk_urls: list[str], failed: list[dict[str, Any]]) -> int:
    """Refuse to load a raw/ directory that is missing a talk.

    A missing talk is not a resumable condition to paper over: it would be indexed as a
    complete conference with a hole in it.

    Args:
        ctx: the run context.
        talk_urls: the canonical talk urls the listing yielded.
        failed: the per-url failure records from the crawl loop.

    Returns:
        The number of valid files in raw/.
    """
    on_disk = sum(1 for url in talk_urls if _raw_file_is_valid(ctx.raw_dir / f"{talk_stem(url)}.json", url))
    if on_disk == len(talk_urls):
        return on_disk
    lines = "\n".join(f"  {record['status_code']}  {record['url']}" for record in failed)
    _abort(
        EXIT_GUARD,
        "RAIL-3",
        f"{len(talk_urls) - on_disk} of {len(talk_urls)} talks are missing from raw/.",
        f"{lines or '  (no http failures were recorded; files may have been removed)'}\n"
        "\n"
        "Re-run to retry only the missing talks: every page already on disk is reused.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def stage_crawl(ctx: Ctx) -> list[str]:
    """Run stage 1: fetch the listing and every talk page in it.

    The listing is always re-fetched. It is one request against a run that already
    spends twenty-five minutes being polite, and it is the only thing that notices a
    conference which has grown since the first crawl.

    Args:
        ctx: the run context.

    Returns:
        The canonical talk urls, in listing order.
    """
    started = _header(ctx, "[1/4]", "crawl")
    listing_url = _listing_url(ctx.year, ctx.month)
    status_code, html = get_page(listing_url, delay_seconds=ctx.delay)
    if status_code != 200:
        _abort(
            EXIT_GUARD,
            "RAIL-3",
            f"the {ctx.key} listing returned {status_code}.",
            f"url: {listing_url}\n\nNothing was written to Pinecone. Exiting.",
        )

    talk_urls, anchors, matched, near_misses = extract_talk_urls(html, listing_url, ctx.year, ctx.month)
    _echo(f"      listing: {anchors} anchors, {matched} matched, {len(talk_urls)} unique (floor {MIN_TALKS})")
    for url in near_misses:
        _echo(f"      rejected near miss: {url}")
    check_talk_count(
        len(talk_urls),
        f"the {ctx.key} listing",
        f"listing:  {listing_url}\nstatus:   200\nanchors on page:            {anchors}\n"
        f"matched the talk predicate: {matched}   ({len(talk_urls)} unique after canonicalization)",
    )
    _check_listing_unchanged(ctx, talk_urls)
    ctx.run.stage("crawl").update({"status": "in_progress", "talk_urls": talk_urls})
    ctx.run.save()

    fetched, reused, failed = _crawl_talks(ctx, talk_urls)
    on_disk = _check_crawl_complete(ctx, talk_urls, failed)
    check_talk_count(on_disk, f"raw/ for {ctx.key}", f"directory: {ctx.raw_dir}")

    elapsed = time.monotonic() - started
    ctx.run.finish_stage(
        "crawl",
        "completed",
        elapsed,
        listing_status_code=status_code,
        talk_urls_found=len(talk_urls),
        talk_urls=talk_urls,
        anchors_seen=anchors,
        links_matched=matched,
        fetched_this_run=fetched,
        reused_from_disk=reused,
        failed=failed,
    )
    _echo(f"      done in {_duration(elapsed)}: {len(talk_urls)} talks on disk ({fetched} fetched, {reused} reused)")
    return talk_urls


# ---------------------------------------------------------------------------------------
# Stage 2 - load. Always re-runs: it is offline, deterministic, and about two seconds for
# thirty-five talks, so caching it would add a staleness rule with no payoff.
# ---------------------------------------------------------------------------------------


def _check_no_contamination(ctx: Ctx, loaded: set[str], expected: set[str]) -> None:
    """Refuse a raw/ directory holding pages from another conference.

    The per-conference directory layout exists to prevent this; the assert is what proves
    the layout held. Loading a stray talk would re-embed and re-upsert unrelated content.

    Args:
        ctx: the run context.
        loaded: the urls the loader produced.
        expected: the urls this run crawled.
    """
    extra = sorted(loaded - expected)
    if not extra:
        return
    _abort(
        EXIT_LOADER_SKIPS,
        "RAIL-5",
        f"{ctx.raw_dir} holds {len(extra)} page(s) that are not part of {ctx.key}.",
        "\n".join(f"  {url}" for url in extra) + "\n"
        "\n"
        "Indexing them would re-embed and re-upsert talks this run never crawled.\n"
        "Remove them, or delete the directory and re-crawl.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def _check_loader_skips(ctx: Ctx, skipped: list[str], total: int) -> None:
    """Refuse when the loader dropped more talks than the operator allowed.

    Args:
        ctx: the run context.
        skipped: the urls the loader dropped.
        total: how many pages were on disk.
    """
    if not skipped:
        return
    listing = "\n".join(f"  {url}" for url in skipped)
    if len(skipped) <= ctx.allow_skips:
        _warn(f"      --allow-skips={ctx.allow_skips}: continuing without {len(skipped)} talk(s)\n{listing}")
        return
    _abort(
        EXIT_LOADER_SKIPS,
        "RAIL-5",
        f"the loader dropped {len(skipped)} of {total} talks (missing title or body):",
        f"{listing}\n"
        "\n"
        'A talk is skipped when "article header h1" or "article div.body-block" did\n'
        "not match (models/load_conf.py:86-89). A 200 response carrying a JS-rendered\n"
        "shell yields zero body-block matches and looks exactly like this.\n"
        f"Inspect {ctx.raw_dir} before deciding.\n"
        "\n"
        f"To index anyway, knowing these talks will be missing:\n    --allow-skips={len(skipped)}\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def _check_zero_docs(ctx: Ctx, docs: list[Document], total: int) -> None:
    """Refuse when every page parsed to nothing. --allow-skips cannot reach this.

    Args:
        ctx: the run context.
        docs: the documents the loader produced.
        total: how many pages were on disk.
    """
    if docs:
        return
    _abort(
        EXIT_LOADER_SKIPS,
        "RAIL-5",
        f"the loader produced zero documents from {total} crawled pages.",
        "Every page parsed to an empty title or empty body. This is what a\n"
        "JavaScript-rendered shell looks like to this pipeline: HTTP 200, plausible\n"
        'page size, and no "article div.body-block" anywhere in it.\n'
        "\n"
        f"--allow-skips cannot override this. Inspect one of the saved pages:\n    {ctx.raw_dir}\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def _check_authors(docs: list[Document]) -> list[str]:
    """Warn about missing authors, and refuse when most of them are missing.

    The loader keeps a doc with no author, and an empty author is harmless to the server.
    But if the "article p.author-name" selector ever rots, every talk loses its author at
    once - a selector regression, not an editorial omission, and nothing else would
    notice it.

    Args:
        docs: the loaded documents.

    Returns:
        The urls whose author is empty.
    """
    missing = [str(doc.metadata["url"]) for doc in docs if not doc.metadata.get("author")]
    if not missing:
        return missing
    _warn(f"      {len(missing)} of {len(docs)} talks have no author")
    if len(missing) * 2 > len(docs):
        _abort(
            EXIT_LOADER_SKIPS,
            "RAIL-5",
            f"{len(missing)} of {len(docs)} talks have an empty author.",
            "More than half the conference lost its author, which is a selector\n"
            'regression in "article p.author-name", not an editorial omission.\n'
            "Nothing was written to Pinecone. Exiting.",
        )
    return missing


def stage_load(ctx: Ctx, talk_urls: list[str]) -> list[Document]:
    """Run stage 2: parse the crawled pages into documents.

    The url sort is load-bearing. os.listdir order is arbitrary, and shard order,
    split.jsonl line order, embeddings.npy row order, batch boundaries, and the chunk id
    list in the rollback manifest all have to be reproducible across machines and across
    a resume.

    Args:
        ctx: the run context.
        talk_urls: the canonical talk urls this run crawled.

    Returns:
        The loaded documents, sorted by url.
    """
    started = _header(ctx, "[2/4]", "load")
    docs = ConferenceTalkLoader(str(ctx.raw_dir)).load(verbose=True)
    docs.sort(key=lambda doc: str(doc.metadata["url"]))

    loaded_urls = {str(doc.metadata["url"]) for doc in docs}
    expected_urls = set(talk_urls)
    _check_no_contamination(ctx, loaded_urls, expected_urls)
    _check_zero_docs(ctx, docs, len(talk_urls))
    skipped = sorted(expected_urls - loaded_urls)
    _check_loader_skips(ctx, skipped, len(talk_urls))
    missing_author = _check_authors(docs)
    check_talk_count(len(docs), f"the loader for {ctx.key}", f"skipped: {len(skipped)}")

    save_docs_to_jsonl(docs, str(ctx.tmp_dir / "load.jsonl"))
    os.replace(ctx.tmp_dir / "load.jsonl", ctx.data_dir / "load.jsonl")
    elapsed = time.monotonic() - started
    total_chars = sum(len(doc.page_content) for doc in docs)
    ctx.run.finish_stage(
        "load",
        "completed",
        elapsed,
        raw_files=len(talk_urls),
        docs_loaded=len(docs),
        skipped_urls=skipped,
        missing_author_urls=missing_author,
        total_chars=total_chars,
    )
    _echo(f"      done in {_duration(elapsed)}: {len(docs)} docs, {total_chars:,} chars")
    return docs


# ---------------------------------------------------------------------------------------
# Stage 3 - split.
# ---------------------------------------------------------------------------------------


def pipeline_fingerprint() -> dict[str, Any]:
    """Describe everything that can move a chunk boundary.

    Returns:
        The fingerprint recorded in run.json and compared against each cached shard.
    """
    return {
        "splitter": "MarkdownSyntacticEmbeddingSplitter",
        "split_threshold": SPLIT_THRESHOLD,
        "max_chars": MAX_CHARS,
        "anchor": ANCHOR,
        "paragraph_embedder": PARAGRAPH_EMBEDDER,
        "embedding_model": EMBEDDING_MODEL,
        "code_sha256": _code_sha256(),
        "python": ".".join(str(part) for part in sys.version_info[:3]),
        "versions": _package_versions(),
    }


def _describe_integrity_failure(doc: Document, chunk: Document, position: int, total: int) -> str:
    """Build the rail-8 abort body for one failing chunk.

    Args:
        doc: the talk the chunk should have come from.
        chunk: the failing chunk.
        position: the chunk's 1-based position in the talk.
        total: how many chunks the talk produced.

    Returns:
        The message body.
    """
    return (
        f"talk:  {doc.metadata['url']}\n"
        f"chunk: {position} of {total}   (anchor {chunk.metadata.get(ANCHOR, '')!r}, "
        f"{len(chunk.page_content):,} chars)\n"
        "\n"
        "After normalization, this chunk's text is not a substring of the normalized\n"
        "talk. Comparison is on clean_text() output on both sides, because the\n"
        "splitter legitimately rewrites links, anchors, citations, quote characters\n"
        "and whitespace - raw text is NOT expected to match.\n"
        "\n"
        f"chunk starts:  {chunk.page_content[:70]!r}\n"
        "\n"
        "This means the loader, the markdown converter, or the splitter is producing\n"
        "text that is not in the source document. Everything downstream - the chunk\n"
        'id, the embedding, the "text" the server shows the reader - would be wrong,\n'
        "and no other check in this script would notice."
    )


def check_text_integrity(ctx: Ctx, doc: Document, chunks: Sequence[Document]) -> None:
    """Refuse a chunk whose text is not in the talk it is attributed to.

    Containment is tested on clean_text() output on both sides. A verbatim test does not
    hold and never did: measured over the committed fixtures, only 10 of 62 legitimate
    chunks are substrings of their talk, because clean_text rewrites links, anchors,
    citations and whitespace between the loaded markdown and the final chunk. Normalized
    containment holds for all 62, and still catches a single corrupted word in all 62.
    Every chunk is checked, not a sample: it costs about 112 ms for a whole conference.

    Args:
        ctx: the run context.
        doc: the talk the chunks came from.
        chunks: the chunks the splitter produced for it.
    """
    normalized_talk = clean_text(doc.page_content)
    failures = [
        (position, chunk)
        for position, chunk in enumerate(chunks, start=1)
        if clean_text(chunk.page_content) not in normalized_talk
    ]
    for chunk in chunks:
        if chunk.metadata.get("url") != doc.metadata["url"] or chunk.metadata.get("year") != str(ctx.year):
            _abort(
                EXIT_TEXT_INTEGRITY,
                "RAIL-8",
                "A chunk carries metadata from a different talk or conference.",
                f"talk:  {doc.metadata['url']}\nchunk: {chunk.metadata}\n"
                "\n"
                "split_document_content copies and mutates metadata; a chunk that inherited\n"
                "the wrong parent would be indexed under the wrong talk and deep-link to it.\n"
                "Nothing was embedded or written to Pinecone. Exiting.",
            )
    if not failures:
        return
    bodies = [_describe_integrity_failure(doc, chunk, position, len(chunks)) for position, chunk in failures[:3]]
    if len(failures) > 3:
        bodies.append(f"... and {len(failures) - 3} more failing chunks in this talk")
    bodies.append(f"checked {len(chunks)} of {len(chunks)} chunks for this talk; {len(failures)} failed.")
    bodies.append("Nothing was embedded or written to Pinecone. Exiting.")
    _abort(
        EXIT_TEXT_INTEGRITY,
        "RAIL-8",
        "A chunk's text does not come from the talk it is attributed to.",
        "\n\n".join(bodies),
    )


def _shard_is_reusable(ctx: Ctx, stem: str, doc: Document, fingerprint: str) -> bool:
    """Decide whether a cached split shard still describes this talk.

    A stage is done only when its output exists and the input it was derived from still
    hashes to what run.json says it was - never "the file exists, therefore skip".

    Args:
        ctx: the run context.
        stem: the shard's filename stem.
        doc: the talk the shard should have come from.
        fingerprint: the current pipeline code fingerprint.

    Returns:
        True when the shard on disk can be reused.
    """
    recorded = ctx.run.stage("split").get("shards", {}).get(stem)
    if not recorded or not (ctx.split_dir / f"{stem}.jsonl").exists():
        return False
    return bool(
        recorded.get("source_sha256") == _sha256(doc.page_content) and recorded.get("fingerprint") == fingerprint
    )


def _split_one_talk(ctx: Ctx, splitter: Any, doc: Document, stem: str, reuse: bool) -> list[Document]:
    """Produce the chunks of one talk, from cache when the cache is still valid.

    Per-talk splitting is exactly equivalent to one bulk call: transform_documents loops
    over documents with no cross-document state.

    Args:
        ctx: the run context.
        splitter: the splitter, constructed once.
        doc: the talk to split.
        stem: the shard's filename stem.
        reuse: whether the cached shard is valid.

    Returns:
        The chunks for this talk, in order.
    """
    path = ctx.split_dir / f"{stem}.jsonl"
    if reuse:
        return list(load_docs_from_jsonl(str(path)))
    chunks = list(splitter.transform_documents([doc]))
    ctx.split_dir.mkdir(parents=True, exist_ok=True)
    save_docs_to_jsonl(chunks, str(ctx.tmp_dir / f"{stem}.jsonl"))
    os.replace(ctx.tmp_dir / f"{stem}.jsonl", path)
    return chunks


def _warn_on_chunk_rate(docs: list[Document], chunks: list[Document]) -> float:
    """Warn when the chunks-per-talk rate is nothing like the measured one.

    Args:
        docs: the talks.
        chunks: the chunks they produced.

    Returns:
        The chunks-per-talk rate.
    """
    rate = len(chunks) / len(docs)
    if not MIN_CHUNKS_PER_TALK <= rate <= MAX_CHUNKS_PER_TALK:
        _warn(f"      {rate:.2f} chunks/talk is outside {MIN_CHUNKS_PER_TALK}-{MAX_CHUNKS_PER_TALK} (measured 8.7)")
    return rate


def stage_split(ctx: Ctx, docs: list[Document]) -> list[Document]:
    """Run stage 3: split each talk into the chunks that become vectors.

    The splitter is constructed with no arguments on purpose.
    tests/test_reproducibility.py pins split_threshold and max_chars separately, so
    passing them here would decouple this script from that pin.

    Args:
        ctx: the run context.
        docs: the loaded talks, url-sorted.

    Returns:
        The chunks, in url-sorted talk order.
    """
    from models.split_model import MarkdownSyntacticEmbeddingSplitter

    started = _header(ctx, "[3/4]", "split")
    fingerprint = _code_sha256()
    splitter: Any = None
    shards: dict[str, Any] = {}
    chunks: list[Document] = []
    reused = 0

    for position, doc in enumerate(docs, start=1):
        stem = talk_stem(str(doc.metadata["url"]))
        reuse = _shard_is_reusable(ctx, stem, doc, fingerprint)
        if not reuse and splitter is None:
            splitter = MarkdownSyntacticEmbeddingSplitter()
        talk_chunks = _split_one_talk(ctx, splitter, doc, stem, reuse)
        check_text_integrity(ctx, doc, talk_chunks)
        chunks.extend(talk_chunks)
        reused += 1 if reuse else 0
        shards[stem] = {
            "source_sha256": _sha256(doc.page_content),
            "fingerprint": fingerprint,
            "chunks": len(talk_chunks),
        }
        suffix = " (cached shard)" if reuse else ""
        _echo(
            f"      [{position:>2}/{len(docs)}] {stem.split('-', 2)[2]:<28}{suffix:<16}"
            f"{len(talk_chunks):>3} chunks  ({len(chunks)} total)"
        )

    save_docs_to_jsonl(chunks, str(ctx.tmp_dir / "split.jsonl"))
    os.replace(ctx.tmp_dir / "split.jsonl", ctx.data_dir / "split.jsonl")
    rate = _warn_on_chunk_rate(docs, chunks)
    elapsed = time.monotonic() - started
    ctx.run.finish_stage(
        "split",
        "completed",
        elapsed,
        docs_in=len(docs),
        chunks_out=len(chunks),
        chunks_per_talk=round(rate, 2),
        shards_computed=len(docs) - reused,
        shards_reused=reused,
        max_chunk_chars=max(len(chunk.page_content) for chunk in chunks),
        shards=shards,
    )
    _echo(f"      done in {_duration(elapsed)}: {len(docs)} docs -> {len(chunks)} chunks ({rate:.2f}/talk)")
    return chunks


# ---------------------------------------------------------------------------------------
# Stage 4 - embed and upsert.
# ---------------------------------------------------------------------------------------


class _CaptureIndex:
    """An index-shaped sink that records upsert batches instead of sending them.

    Driving the real index_documents through this is what makes the dry-run preview and
    the metadata assertions impossible to drift from a real run: the ids and the nine
    metadata keys are produced by index_documents itself, not re-derived here.
    """

    def __init__(self) -> None:
        """Start with no captured batches."""
        self.batches: list[list[Any]] = []

    def upsert(self, *, vectors: Iterable[Any], **kwargs: Any) -> None:
        """Record one batch.

        Keyword-only to match pinecone 10, which index_documents already calls correctly.

        Args:
            vectors: the (id, values, metadata) tuples of this batch.
            kwargs: accepted and ignored, as the real client's extra options would be.
        """
        self.batches.append(list(vectors))


def plan_upsert(chunks: list[Document]) -> list[list[Any]]:
    """Build exactly what a real run would send, without sending it.

    Args:
        chunks: the chunks to be indexed.

    Returns:
        The batches of (id, values, metadata) tuples, values all zero.
    """
    placeholder: list[Any] = [[0.0] * INDEX_DIM for _ in chunks]
    capture = _CaptureIndex()
    index_documents(capture, placeholder, chunks, batch_size=UPSERT_BATCH_SIZE)
    return capture.batches


def check_metadata_shape(batches: list[list[Any]]) -> None:
    """Refuse metadata the server could not read, before anything is paid for.

    A None metadata value is a 400 at the server, which would arrive after the
    embeddings are already bought. load_conf coerces its fields to "" so the current
    pipeline cannot produce one, but this must not depend on that staying true.

    Args:
        batches: the planned upsert batches.
    """
    for batch in batches:
        for vector_id, _values, metadata in batch:
            keys = set(metadata)
            bad = [name for name, value in metadata.items() if value is None]
            if keys == METADATA_KEYS and not bad:
                continue
            _abort(
                EXIT_GUARD,
                "RAIL-6",
                f"the metadata for {vector_id[:12]}... is not the shape the index expects.",
                f"expected keys: {sorted(METADATA_KEYS)}\n"
                f"actual keys:   {sorted(keys)}\n"
                f"None values:   {bad}\n"
                "\n"
                "server/server/main.py subscripts these keys unguarded over every match,\n"
                "and its middleware turns any exception into a blanket 500.\n"
                "Nothing was embedded or written to Pinecone. Exiting.",
            )


def write_manifest(ctx: Ctx, chunks: list[Document], batches: list[list[Any]]) -> dict[str, Any]:
    """Record the exact vector ids this run intends to write, before it writes any.

    get_doc_id depends on nothing from the embedder, so a --dry-run produces the
    byte-identical list the real run will use. The rollback manifest therefore exists in
    full before any money is spent and before any write is made.

    Args:
        ctx: the run context.
        chunks: the chunks to be indexed.
        batches: the planned upsert batches.

    Returns:
        The manifest that was written.
    """
    chunk_ids = [get_doc_id(chunk) for chunk in chunks]
    ctx.chunk_ids = chunk_ids
    manifest = {
        "recorded_at": _now(),
        "recorded_before_any_write": ctx.run.stage("upsert").get("status", "not_started")
        in ("not_started", "skipped_dry_run"),
        "chunk_count": len(chunk_ids),
        "unique_chunk_count": len(set(chunk_ids)),
        "duplicate_ids": len(chunk_ids) - len(set(chunk_ids)),
        "ids_sha256": _sha256("\n".join(chunk_ids)),
        "chunk_ids": chunk_ids,
        "batches": [
            {
                "index": position,
                "start": position * UPSERT_BATCH_SIZE,
                "end": position * UPSERT_BATCH_SIZE + len(batch),
                "first_id": batch[0][0],
                "last_id": batch[-1][0],
            }
            for position, batch in enumerate(batches)
        ],
    }
    ctx.run.data["planned_upsert"] = manifest
    ctx.run.data["rollback"] = {
        "index_host": INDEX_HOST,
        "namespace": NAMESPACE,
        "id_source": "planned_upsert.chunk_ids",
        "max_ids_per_delete_call": 1000,
        "note": (
            "Delete exactly these ids. Never roll back with a {year,month} metadata "
            "filter: the same filter would also match any pre-existing vector for this "
            "conference and, if the metadata shape were ever wrong, could match far "
            "more than this run wrote."
        ),
    }
    ctx.run.save()
    return manifest


def check_ids_absent(ctx: Ctx, chunk_ids: list[str]) -> list[str]:
    """Refuse when these exact chunks are already in the index, unless --force.

    fetch is an exact id lookup rather than an approximate search, so this is the
    authoritative form of the already-indexed guard; the metadata filter in stage 0 is a
    reliable positive but an unreliable negative.

    Args:
        ctx: the run context.
        chunk_ids: the ids this run plans to write.

    Returns:
        The ids that are already present.
    """
    present: list[str] = []
    for start, end in _batch_bounds(len(chunk_ids), UPSERT_BATCH_SIZE):
        present.extend(ctx.index.fetch(ids=chunk_ids[start:end], namespace=NAMESPACE).vectors)
    if not present:
        return present
    if ctx.force:
        _warn(
            f"      --force: {len(present)} of {len(chunk_ids)} chunk ids already present, "
            f"{len(chunk_ids) - len(present)} new. Continuing."
        )
        return present
    _abort(
        EXIT_ALREADY_INDEXED,
        "RAIL-6",
        f"{len(present)} of {len(chunk_ids)} chunk ids for {ctx.key} are already in the index.",
        f"already present: {len(present)}, new: {len(chunk_ids) - len(present)}\n"
        "\n"
        "This script is meant to be run once per conference. It has no --replace mode\n"
        "and does not handle revised talks: a talk whose text has changed since it was\n"
        "indexed produces new chunk ids, so re-running would ADD the new chunks and\n"
        "leave the old ones orphaned in the index rather than replacing them.\n"
        "\n"
        "If a previous run crashed part-way through and you are resuming it, re-run\n"
        "with --force. Re-upserting a chunk whose text is unchanged writes the same\n"
        "id and is harmless.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def check_embeddings(vectors: list[Any], expected: int) -> None:
    """Refuse embeddings that cannot be what the index holds. --force cannot reach this.

    Args:
        vectors: the embeddings.
        expected: how many there should be.
    """
    array = np.asarray(vectors, dtype=np.float32)
    problems = []
    if len(vectors) != expected:
        problems.append(f"got {len(vectors)} embeddings for {expected} chunks")
    if array.ndim != 2 or array.shape[1] != INDEX_DIM:
        problems.append(f"shape {array.shape} is not (n, {INDEX_DIM})")
    elif not bool(np.isfinite(array).all()):
        problems.append("some values are NaN or infinite")
    if not problems:
        return
    _abort(
        EXIT_BAD_EMBEDDINGS,
        "RAIL-4a",
        "the embeddings are not the shape the production index takes.",
        "\n".join(f"  {problem}" for problem in problems) + "\n"
        "\n"
        f"The index is {INDEX_DIM}-dimensional {EMBEDDING_MODEL}, and the live server embeds\n"
        "queries with the same model. A different model would be accepted by Pinecone\n"
        "and silently return nonsense. --force does not override this.\n"
        "Nothing was written to Pinecone. Exiting.",
    )


def _reuse_embeddings(ctx: Ctx, count: int, ids_sha256: str) -> Optional[list[Any]]:
    """Load cached embeddings when they still belong to this exact chunk-id plan.

    Args:
        ctx: the run context.
        count: how many chunks there are.
        ids_sha256: the digest of the current chunk-id plan.

    Returns:
        The cached embeddings, or None when the cache is absent or stale.
    """
    path = ctx.data_dir / "embeddings.npy"
    if not path.exists() or ctx.run.stage("embed").get("ids_sha256") != ids_sha256:
        return None
    array = np.load(path)
    if array.shape != (count, INDEX_DIM):
        return None
    return cast(list[Any], array.tolist())


def stage_embed(ctx: Ctx, chunks: list[Document], ids_sha256: str) -> list[Any]:
    """Run stage 4a: turn every chunk into a vector, reusing the cache when it is valid.

    Args:
        ctx: the run context.
        chunks: the chunks to embed.
        ids_sha256: the digest of the current chunk-id plan.

    Returns:
        One embedding per chunk, in chunk order.
    """
    started = _header(ctx, "[4a/4]", "embed")
    cached = _reuse_embeddings(ctx, len(chunks), ids_sha256)
    if cached is not None:
        _echo(f"      reusing {len(cached)} cached embeddings from embeddings.npy")
        vectors = cached
        cache_state = "reused"
    else:
        vectors = embed_documents(OpenAIEmbedder(), chunks, batch_size=EMBED_BATCH_SIZE, delay=EMBED_DELAY)
        cache_state = "computed"
    check_embeddings(vectors, len(chunks))
    if cache_state == "computed":
        array = np.asarray(vectors, dtype=np.float32)
        ctx.tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_path = ctx.tmp_dir / "embeddings.npy"
        np.save(tmp_path, array)
        os.replace(tmp_path, ctx.data_dir / "embeddings.npy")

    elapsed = time.monotonic() - started
    ctx.run.finish_stage(
        "embed",
        "completed",
        elapsed,
        vectors=len(vectors),
        dimension=INDEX_DIM,
        batches=len(_batch_bounds(len(chunks), EMBED_BATCH_SIZE)),
        ids_sha256=ids_sha256,
        cache=cache_state,
        artifact="embeddings.npy",
    )
    _echo(f"      done in {_duration(elapsed)}: {len(vectors)} vectors, dim {INDEX_DIM} ({cache_state})")
    return vectors


class _ResumableIndex:
    """Wraps a Pinecone Index so index_documents' upsert loop becomes resumable.

    index_documents builds ids and metadata; this only decides whether a batch is sent
    or skipped, and records how far the run got. Never re-derive metadata here - the
    nine-key shape must come from index_documents so it cannot drift from what the
    server reads.
    """

    def __init__(self, ctx: Ctx, total_batches: int) -> None:
        """Start at the batch the run record says is next.

        Args:
            ctx: the run context.
            total_batches: how many batches the plan has.
        """
        self.ctx = ctx
        self.total_batches = total_batches
        self.position = 0
        self.sent = 0
        self.upserted_count = 0
        self.done = int(ctx.run.stage("upsert").get("batches_done", 0))

    def upsert(self, *, vectors: Iterable[Any], **kwargs: Any) -> None:
        """Send one batch unless a previous invocation already sent it.

        Keyword-only to match pinecone 10; index_documents already calls it that way.

        Args:
            vectors: the (id, values, metadata) tuples of this batch.
            kwargs: accepted and ignored.

        Raises:
            _Abort: when Pinecone refuses the batch; some earlier batches may have landed.
        """
        batch = list(vectors)
        position = self.position
        self.position += 1
        if position < self.done:
            _echo(f"      batch {position + 1}/{self.total_batches}  {len(batch)} vectors  already sent, skipping")
            return
        started = time.monotonic()
        try:
            response = self.ctx.index.upsert(vectors=batch, namespace=NAMESPACE)
        except (ApiError, PineconeException) as error:
            raise _Abort(
                EXIT_PARTIAL_UPSERT,
                "RAIL-4b",
                f"Pinecone failed on batch {position + 1} of {self.total_batches}.",
                f"error:      {type(error).__name__}\n"
                f"status:     {getattr(error, 'status_code', None)}\n"
                f"request id: {getattr(error, 'request_id', None)}\n"
                f"message:    {getattr(error, 'message', None) or error}\n"
                "\n"
                f"{position} batch(es) already landed in production. The run record has\n"
                "stages.upsert.batches_done and planned_upsert.batches; re-run to resume\n"
                "from the first unsent batch. A {year,month} filter delete is also safe\n"
                "here: the already-indexed guard proved this conference was empty before\n"
                "the run, so the filter matches only what this run wrote.",
            ) from error
        self.upserted_count += int(getattr(response, "upserted_count", len(batch)) or 0)
        self.sent += len(batch)
        self.ctx.run.stage("upsert")["batches_done"] = position + 1
        self.ctx.run.stage("upsert")["vectors_sent"] = self.sent
        self.ctx.run.save()
        _echo(
            f"      batch {position + 1}/{self.total_batches}  {len(batch)} vectors  "
            f"ok ({_duration(time.monotonic() - started)})"
        )


def _settle(ctx: Ctx, before: int, expected_delta: int) -> dict[str, Any]:
    """Wait for the index's eventually-consistent stats to catch up, then report.

    A shortfall is reported, never raised: by this point the vectors are written, and
    upserted_count is the authoritative confirmation. A single post-upsert assertion
    would be a flaky false alarm.

    Args:
        ctx: the run context.
        before: the total vector count recorded in stage 0.
        expected_delta: how many new ids this run wrote.

    Returns:
        The before/after/delta record.
    """
    target = before + expected_delta
    deadline = time.monotonic() + SETTLE_TIMEOUT_SECONDS
    after = before
    settled = False
    while time.monotonic() < deadline:
        after = int(ctx.index.describe_index_stats().total_vector_count)
        if after >= target:
            settled = True
            break
        time.sleep(SETTLE_POLL_SECONDS)
    if not settled:
        _warn(
            f"      index count is {after:,}, expected ~{target:,} - serverless stats lag; "
            "the upsert responses are the authoritative confirmation"
        )
    return {
        "before": before,
        "after": after,
        "delta": after - before,
        "expected_delta": expected_delta,
        "settled": settled,
    }


def stage_upsert(ctx: Ctx, chunks: list[Document], vectors: list[Any], manifest: dict[str, Any]) -> dict[str, Any]:
    """Run stage 4b: write the vectors to production, resumably.

    Args:
        ctx: the run context.
        chunks: the chunks being indexed.
        vectors: their embeddings.
        manifest: the planned-upsert record.

    Returns:
        The index_stats before/after record.
    """
    started = _header(ctx, "[4b/4]", "upsert")
    stage = ctx.run.stage("upsert")
    recorded = stage.get("ids_sha256")
    if recorded and recorded != manifest["ids_sha256"] and not ctx.force:
        _abort(
            EXIT_PARTIAL_UPSERT,
            "RAIL-4b",
            "the chunk-id plan changed while an upsert was partly applied.",
            f"recorded: {recorded}\ncurrent:  {manifest['ids_sha256']}\n"
            f"batches already sent: {stage.get('batches_done', 0)}\n"
            "\n"
            "Continuing would interleave two different id sets in production. Inspect\n"
            "planned_upsert.chunk_ids before deciding, then re-run with --force.",
        )
    batches = _batch_bounds(len(chunks), UPSERT_BATCH_SIZE)
    stage.update({"status": "in_progress", "ids_sha256": manifest["ids_sha256"], "batches_total": len(batches)})
    ctx.run.data["planned_upsert"]["recorded_before_any_write"] = False
    ctx.run.save()

    sink = _ResumableIndex(ctx, len(batches))
    index_documents(sink, vectors, chunks, batch_size=UPSERT_BATCH_SIZE)
    elapsed = time.monotonic() - started
    ctx.run.finish_stage(
        "upsert",
        "completed",
        elapsed,
        batches_total=len(batches),
        batches_done=len(batches),
        vectors_sent=sink.sent,
        upserted_count=sink.upserted_count,
    )
    before = int(ctx.run.stage("preflight").get("index_total_before", 0))
    stats = _settle(ctx, before, manifest["chunk_count"] - len(manifest.get("already_present", [])))
    ctx.run.data["index_stats"] = stats
    ctx.run.save()
    _echo(f"      done in {_duration(elapsed)}: {sink.sent} vectors sent, {sink.upserted_count} confirmed")
    return stats


def print_dry_run(ctx: Ctx, manifest: dict[str, Any], batches: list[list[Any]]) -> None:
    """Print exactly what a real run would send, having sent nothing.

    Args:
        ctx: the run context.
        manifest: the planned-upsert record.
        batches: the planned upsert batches.
    """
    before = int(ctx.run.stage("preflight").get("index_total_before", 0))
    chunk_ids = cast(list[str], manifest["chunk_ids"])
    _echo("")
    _echo("DRY RUN -- nothing was embedded and nothing was sent to Pinecone.")
    _echo("")
    _echo(f"  would upsert:   {len(chunk_ids)} vectors in {len(batches)} batches of {UPSERT_BATCH_SIZE}")
    _echo(f"  unique ids:     {manifest['unique_chunk_count']}  ({manifest['duplicate_ids']} duplicate ids)")
    _echo(f"  index host:     {INDEX_HOST}")
    _echo('  namespace:      "" (reported by stats as __default__)')
    _echo(f"  total before:   {before:,}  ->  expected after ~{before + manifest['unique_chunk_count']:,}")
    _echo("")
    _echo("  sample ids (first 3, last 3):")
    for chunk_id in chunk_ids[:3] + ["..."] + chunk_ids[-3:]:
        _echo(f"    {chunk_id}")
    _echo("")
    _echo("  first chunk, full metadata as it would be upserted:")
    first_id, _values, metadata = batches[0][0]
    _echo(f"    {'id':<12}{first_id}")
    for name in sorted(metadata):
        value = metadata[name]
        shown = f"{value[:40]!r}   ({len(value):,} chars)" if name == "text" else repr(value)
        _echo(f"    {name:<12}{shown}")
    _echo(f"    -> {len(metadata)} metadata keys, matching the 2023-10+ convention the server reads")
    _echo("")
    _echo(f"  chunk ids written to {ctx.run.path} (planned_upsert.chunk_ids)")
    _echo("  Re-run without --dry-run to embed and upsert; stages 1-3 are now cached.")
    _echo("  --dry-run does not test write permission; the probe runs only on a real invocation.")


def print_summary(ctx: Ctx, manifest: dict[str, Any], stats: dict[str, Any]) -> None:
    """Print the closing summary the operator checks the run against.

    Args:
        ctx: the run context.
        manifest: the planned-upsert record.
        stats: the index_stats before/after record.
    """
    crawl = ctx.run.stage("crawl")
    load = ctx.run.stage("load")
    upsert = ctx.run.stage("upsert")
    ok = "ok" if stats["delta"] >= stats["expected_delta"] else "SHORT - see run.json"
    _echo("")
    _echo(f"{ctx.key} complete in {_duration(ctx.elapsed())}")
    _echo(
        f"  crawled {crawl.get('talk_urls_found', 0)}   loaded {load.get('docs_loaded', 0)}   "
        f"chunks {manifest['chunk_count']}   upserted {upsert.get('vectors_sent', 0)}"
    )
    _echo(
        f"  index {stats['before']:,} -> {stats['after']:,}  "
        f"(delta {stats['delta']}, expected {stats['expected_delta']})  {ok}"
    )
    _echo(f"  run record: {ctx.run.path}")
    _echo(
        f"  rollback:   delete the {manifest['chunk_count']} ids in planned_upsert.chunk_ids, "
        "or just the {year,month} filter -\n"
        "              this run indexed the whole conference into an empty slot, so the\n"
        "              filter matches exactly these vectors. The id list is only required\n"
        "              after a --force run over a conference that already had vectors."
    )
    _echo("  next: confirm the new talks answer a question only they can, then bump")
    _echo("        LATEST_CONFERENCE_YEAR in client/src/lib/coverage.ts (see README)")
    _warn_if_site_year_is_stale(ctx.year)


COVERAGE_CONSTANT = Path("client") / "src" / "lib" / "coverage.ts"
COVERAGE_PATTERN = re.compile(r"export const LATEST_CONFERENCE_YEAR\s*=\s*(\d{4})")


def _warn_if_site_year_is_stale(year: int) -> None:
    """Tell the operator to bump the site's coverage year, but only when it is behind.

    The home page claims a year range, and that claim must never run ahead of the
    index. Printing this on every run would train the operator to skip it, so it fires
    only when the committed constant is actually older than the conference just
    indexed.

    Args:
        year: the conference year that was just indexed.
    """
    path = REPO_ROOT.parent / COVERAGE_CONSTANT
    try:
        found = COVERAGE_PATTERN.search(path.read_text(encoding="utf-8"))
    except OSError:
        _echo(f"  site year:  check {COVERAGE_CONSTANT} still advertises through {year}")
        return
    if found is None:
        _echo(f"  site year:  check {COVERAGE_CONSTANT} still advertises through {year}")
        return
    current = int(found.group(1))
    if current >= year:
        return
    _echo("")
    _warn(f"  the site still advertises conferences through {current}, but {year} is now indexed.")
    _echo(f"      edit {path}")
    _echo(f"      export const LATEST_CONFERENCE_YEAR = {current}   ->   {year}")
    _echo("      then deploy the client, so the site stops under-claiming what it can answer.")


def _print_banner(ctx: Ctx, fingerprint: str, source: str) -> None:
    """Print what this invocation resolved, so run.json is not the only record.

    Args:
        ctx: the run context.
        fingerprint: the Pinecone key fingerprint.
        source: where the Pinecone key came from.
    """
    _echo(f"update_conference {ctx.key}")
    _echo(f"  delay          {ctx.delay}s         dry-run        {'yes' if ctx.dry_run else 'no'}")
    _echo(f"  allow-skips    {ctx.allow_skips}           force          {'yes' if ctx.force else 'no'}")
    _echo(f"  data dir       {ctx.data_dir}")
    _echo(f"  pinecone       {source} ({fingerprint}) -> {INDEX_NAME}")
    _echo(
        f"  embedding      {EMBEDDING_MODEL} ({INDEX_DIM})    splitter  "
        f"{PARAGRAPH_EMBEDDER} @ {SPLIT_THRESHOLD} / {MAX_CHARS}"
    )
    _echo(f"  write probe    {ctx.write_probe}")
    _echo("")


def _print_abort(abort: _Abort) -> None:
    """Print a rail refusal to stderr.

    Args:
        abort: the refusal.
    """
    click.secho(f"\nABORT [{abort.rail}] {abort.summary}\n", err=True, fg="red", bold=True)
    for line in abort.body.splitlines():
        click.secho(f"  {line}" if line else "", err=True, fg="red")
    click.secho("", err=True)


def _credentials_record(source: str, key: str) -> dict[str, Any]:
    """Describe which credentials this run used, without exposing any of them.

    Args:
        source: where the Pinecone key came from.
        key: the Pinecone key.

    Returns:
        A mapping of service to source and fingerprint.
    """
    record: dict[str, Any] = {"pinecone": {"source": source, "fingerprint": _fingerprint(key)}}
    for service, name in (("openai", "OPENAI_API_KEY"), ("voyage", "VOYAGE_API_KEY")):
        value = os.environ.get(name, "")
        record[service] = {
            "source": f"models/.env:{name}",
            "fingerprint": _fingerprint(value) if value else None,
        }
    return record


def _build_context(year: int, month: str, options: dict[str, Any], started: float) -> Ctx:
    """Create the conference directory and open its run record.

    Args:
        year: the conference year.
        month: the zero-padded conference month.
        options: the resolved command-line options.
        started: the monotonic clock reading when the run began.

    Returns:
        The run context.
    """
    data_dir = REPO_ROOT / "data" / "update" / f"{year}-{month}"
    tmp_dir = data_dir / ".tmp"
    for directory in (data_dir, data_dir / "raw", data_dir / "split", tmp_dir):
        directory.mkdir(parents=True, exist_ok=True)
    run = RunRecord(data_dir / "run.json", tmp_dir)
    return Ctx(year=year, month=month, data_dir=data_dir, run=run, started=started, **options)


def _record_invocation(ctx: Ctx, key: str, source: str) -> None:
    """Append this invocation to the run record and refresh its configuration block.

    Args:
        ctx: the run context.
        key: the production Pinecone key.
        source: where the key came from.
    """
    ctx.run.data["conference"] = {"year": ctx.year, "month": ctx.month, "key": ctx.key}
    ctx.run.data["config"] = {
        "delay": ctx.delay,
        "allow_skips": ctx.allow_skips,
        "force": ctx.force,
        "write_probe": ctx.write_probe,
        "listing_url": _listing_url(ctx.year, ctx.month),
        "data_dir": str(ctx.data_dir.relative_to(REPO_ROOT)),
        "index_host": INDEX_HOST,
        "namespace": NAMESPACE,
        "upsert_batch_size": UPSERT_BATCH_SIZE,
        "embed_batch_size": EMBED_BATCH_SIZE,
        "embed_delay": EMBED_DELAY,
        "min_talks": MIN_TALKS,
        "max_talks": MAX_TALKS,
    }
    ctx.run.data["credentials"] = _credentials_record(source, key)
    ctx.run.data["pipeline_fingerprint"] = pipeline_fingerprint()
    ctx.run.data["status"] = "in_progress"
    invocation = {"started_at": _now(), "argv": sys.argv[1:], "dry_run": ctx.dry_run}
    invocation.update(_git_state())
    cast(list[dict[str, Any]], ctx.run.data.setdefault("invocations", [])).append(invocation)
    ctx.run.save()


def _execute(ctx: Ctx, key: str, source: str) -> int:
    """Run every stage in order.

    Args:
        ctx: the run context.
        key: the production Pinecone key.
        source: where the key came from.

    Returns:
        The process exit code.
    """
    stage_preflight(ctx, key, source)
    talk_urls = stage_crawl(ctx)
    docs = stage_load(ctx, talk_urls)
    chunks = stage_split(ctx, docs)

    batches = plan_upsert(chunks)
    check_metadata_shape(batches)
    manifest = write_manifest(ctx, chunks, batches)
    _echo("")
    _echo(f"      chunk id manifest written: {manifest['chunk_count']} ids -> {ctx.run.path}")
    _echo("      everything after this point costs money or writes to production.")
    _echo("")

    if ctx.dry_run:
        for name in ("embed", "upsert"):
            ctx.run.finish_stage(name, "skipped_dry_run", 0.0)
        print_dry_run(ctx, manifest, batches)
        return EXIT_OK

    manifest["already_present"] = check_ids_absent(ctx, ctx.chunk_ids)
    ctx.run.save()
    vectors = stage_embed(ctx, chunks, cast(str, manifest["ids_sha256"]))
    stats = stage_upsert(ctx, chunks, vectors, manifest)
    print_summary(ctx, manifest, stats)
    return EXIT_OK


def _normalize_month(ctx: click.Context, param: click.Parameter, value: str) -> str:
    """Accept "4" as well as "04", and reject anything that is not a conference month.

    The option is typed str rather than click.Choice so that "4" survives to be padded;
    a Choice would reject it before this callback ever ran.

    Args:
        ctx: the click context.
        param: the parameter being converted.
        value: the raw option value.

    Returns:
        The zero-padded month.

    Raises:
        BadParameter: when the value is not 04 or 10.
    """
    normalized = str(value).strip().zfill(2)
    if normalized not in VALID_MONTHS:
        raise click.BadParameter("must be 04 or 10; General Conference is held twice a year")
    return normalized


def _sync_voyage_api_key() -> None:
    """Re-publish VOYAGE_API_KEY from the environment to the voyageai module global.

    voyageai reads os.environ["VOYAGE_API_KEY"] into a module-level global when it is
    first imported, and models.split_utils imports it at module scope - which happens
    before main() calls load_dotenv(). load_dotenv only writes os.environ, so without
    this the global stays None and the splitter raises AuthenticationError, after the
    whole five-minute crawl has already run.
    """
    key = os.environ.get("VOYAGE_API_KEY")
    if key:
        voyageai.api_key = key


@click.command(
    help="Add one General Conference to the production Pinecone index.\n\n"
    "Crawls the conference listing, loads and splits every talk, embeds the chunks with "
    "text-embedding-ada-002, and upserts them into conf-ada-002-svrless. Every stage caches to "
    "data/update/<year>-<month>/, so a crash resumes rather than restarts, and run.json records "
    "the exact vector ids written for rollback.\n\n"
    "Refuses any conference before 2023-10: those vectors have integer ids that a content hash "
    "cannot overwrite, so such a run would silently duplicate thousands of vectors.",
)
@click.option("--year", type=int, required=True, help="Conference year, e.g. 2025. Must be 2023-10 or later.")
@click.option(
    "--month",
    type=str,
    required=True,
    callback=_normalize_month,
    help="Conference month: 04 (April) or 10 (October). '4' and '10' are accepted.",
)
@click.option(
    "--delay",
    type=click.IntRange(min=8),
    default=10,
    show_default=True,
    help="Seconds to wait between churchofjesuschrist.org requests. Minimum 8. "
    "Threaded into crawl_utils.get_page, whose own default is 30.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Crawl, load, and split for real; print what would be upserted and stop. "
    "No OpenAI embedding call and no write to Pinecone.",
)
@click.option(
    "--allow-skips",
    type=click.IntRange(min=0),
    default=0,
    show_default=True,
    help="Tolerate at most N talks dropped by the loader for missing title or body. "
    "Default 0: any drop aborts before anything is embedded.",
)
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="Override the already-indexed guards only: a prior completed run.json, a {year,month} "
    "metadata hit, chunk ids already in the index, a changed talk-URL listing, or a changed "
    "chunk-id plan on resume. Does NOT override the pre-2023-10 refusal, the talk-count floor, "
    "--allow-skips, or the 1536-dim assertion.",
)
@click.option(
    "--write-probe",
    type=click.Choice(["update", "canary", "skip"]),
    default="update",
    show_default=True,
    help="How to prove the key may write, before the crawl. 'update' touches an id that cannot "
    "exist, so nothing is ever written. 'canary' writes a real vector into "
    "production for about a second, then deletes it. 'skip' tests nothing.",
)
@click.version_option()
def main(
    year: int,
    month: str,
    delay: int,
    dry_run: bool,
    allow_skips: int,
    force: bool,
    write_probe: str,
) -> None:
    """Add one General Conference to the production Pinecone index.

    Crawls the conference listing, loads and splits every talk, embeds the chunks with
    text-embedding-ada-002, and upserts them into conf-ada-002-svrless. Every stage
    caches to data/update/<year>-<month>/, so a crash resumes rather than restarts, and
    run.json records the exact vector ids written for rollback.

    Args:
        year: the conference year.
        month: the zero-padded conference month.
        delay: seconds between requests to churchofjesuschrist.org.
        dry_run: preview stage 4 instead of embedding and writing.
        allow_skips: how many loader drops to tolerate.
        force: override the already-indexed guards.
        write_probe: how to prove the key may write.
    """
    load_dotenv()
    _sync_voyage_api_key()
    started = time.monotonic()
    options = {
        "delay": delay,
        "dry_run": dry_run,
        "allow_skips": allow_skips,
        "force": force,
        "write_probe": write_probe,
    }
    ctx: Optional[Ctx] = None
    try:
        check_era(year, month)
        check_plausible_year(year)
        key, source = resolve_pinecone_key()
        ctx = _build_context(year, month, options, started)
        # Rail 6a must fire before _record_invocation overwrites a "completed" record.
        check_no_completed_run(ctx)
        _record_invocation(ctx, key, source)
        _print_banner(ctx, _fingerprint(key), source)
        code = _execute(ctx, key, source)
    except _Abort as abort:
        _print_abort(abort)
        if ctx is not None:
            ctx.run.close("failed", abort.code, time.monotonic() - started, f"{abort.rail}: {abort.summary}")
        sys.exit(abort.code)
    except Exception as error:  # noqa: B902
        traceback.print_exc()
        if ctx is not None:
            ctx.run.close("failed", EXIT_UNEXPECTED, time.monotonic() - started, f"{type(error).__name__}: {error}")
        sys.exit(EXIT_UNEXPECTED)
    ctx.run.close("dry_run_completed" if dry_run else "completed", code, time.monotonic() - started)
    sys.exit(code)


if __name__ == "__main__":
    main(prog_name="update_conference")  # pragma: no cover
