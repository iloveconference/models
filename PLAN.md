# Plan: `models/update_conference.py`

One command to add a new General Conference to the live index, replacing the
four-notebook sequence (05 → 15 → 25 → 35).

```console
poetry run python -m models.update_conference --year 2025 --month 10
poetry run python -m models.update_conference --year 2026 --month 04
poetry run python -m models.update_conference --year 2026 --month 10
```

Three conferences are currently missing, not one — see [Why](#why).

## Why

The prod index `conf-ada-002-svrless` currently holds talks through **2025-04**
(35,454 vectors). A conference-by-conference scan of every slot from 1971 to
2026 found exactly three gaps:

| Missing     | Talks on site |
| ----------- | ------------- |
| **2025-10** | 35            |
| **2026-04** | 37            |
| **2026-10** | 38            |
|             | **110 total** |

Everything from 1980-04 through 2025-04 is present and continuous — no
interior holes. Pre-1980 is absent by design (the crawler starts at 1980).
2025-10 was confirmed missing by exact-URL lookup, not just a metadata filter,
so it is genuinely unindexed rather than indexed under a different shape.

The notebooks still produce correct output, but their pinned libraries can no
longer reach a serverless index (see
[Library upgrade](#library-upgrade-do-this-first)), and
`s3://scripturecentralqa.data` — the documented way to get the intermediate
data — no longer exists, so local `data/` stops at 2023-04 and cannot be
refreshed. **The index is now the only reliable record of what has been
published**, which is also why the gap went unnoticed: nothing was watching.

## Verified facts this plan rests on

Checked against the live site and live index on 2026-10-13:

| Claim                                | Evidence                                                                                                                                                                                     |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conference listing pages still parse | `2026/04` and `2026/10` both return 200; `_is_talk_url` extracts 37 and 38 talk URLs                                                                                                         |
| Talk slugs changed shape             | Now short (`2026/10/11christofferson`), formerly descriptive. Path-component logic is unaffected                                                                                             |
| Loader selectors still match         | `load_conference_talk` on a real 2026-10 talk returned correct title, author, author_role, and 2.6KB of markdown with `<a name=...>` anchors                                                 |
| Prod index identity                  | `GET api.pinecone.io/indexes` with `server/.env` `PINECONE_KEY` → exactly one index, `conf-ada-002-svrless`, host matches `server/main.py:46`, serverless us-east-1, cosine, dim 1536, ready |
| Dev key is the wrong one             | `models/.env` `PINECONE_API_KEY` lists **zero** indexes                                                                                                                                      |
| OpenAI creds already shared          | `models/.env` `OPENAI_API_KEY` == `server/.env` `OPENAI_KEY` (identical SHA-256), same `OPENAI_ORG`                                                                                          |
| Legacy OpenAI SDK still works        | `openai` 0.27.10 `Embedding.create(engine="text-embedding-ada-002")` → dim 1536                                                                                                              |
| Upgraded OpenAI SDK is equivalent    | `openai` 2.16.0 (server venv) → same model, dim 1536, **L2 norm 1.0**                                                                                                                        |
| ~~Upgrades are conflict-free~~       | **WRONG — retracted.** `langchain` 0.0.306 requires `anyio<4.0`; `pinecone` 10.0.0 requires `anyio>=4.0`. Hard `ResolutionImpossible`. See [Library upgrade](#library-upgrade-do-this-first) |
| Index has two eras                   | pre-2023/10: integer IDs, 7 metadata keys, embedded on **text only** (cosine 0.99986 vs 0.97698 for title+text). 2023/10+: sha256 IDs, 9 keys, title+text                                    |
| Gold split labels still exist        | `data/split/labeled/2023-09-24.json`, 75 labeled talk sections — threshold is re-tunable with no new labeling                                                                                |
| Trainer metrics are gone             | all 76 cells of notebook 22 have outputs stripped by `nbstripout`                                                                                                                            |
| `voyage-01` is alive                 | responds, dim 1024, norm 1.0, reproducible, near-orthogonal to voyage-2/3/3.5 — not an alias                                                                                                 |
| Pipeline is byte-reproducible        | re-split of indexed talk `2025/04/43runia` regenerated **8/8** existing chunk IDs exactly                                                                                                    |
| Gap scan is exhaustive               | every year/month slot 1971-2026 queried: only 2025-10, 2026-04, 2026-10 missing; 1980-04 → 2025-04 continuous                                                                                |
| 2025-10 really is absent             | 6 of its 35 talk URLs looked up by exact `url` filter — zero hits, so not a metadata-shape problem                                                                                           |
| Nothing automated reads `.rtx.toml`  | no rtx/mise/asdf on PATH, no `.tool-versions`; CI uses `actions/setup-python`                                                                                                                |
| ada-002 is not bit-deterministic     | Same input twice → max abs diff 1.8e-4. Irrelevant to cosine ranking                                                                                                                         |

## Embedding compatibility (non-negotiable)

Queries and chunks must land in the same vector space. That is a property of
the **model**, not the API key:

- Server embeds queries with `text-embedding-ada-002` (`server/main.py:42`).
- The script must embed chunks with the identical model string.
- Index is dim 1536 — `text-embedding-3-small` (1536) would be accepted by
  Pinecone and silently return nonsense; `text-embedding-3-large` (3072) would
  hard-fail. Neither is a safe swap without a full reindex.

The script hardcodes `EMBEDDING_MODEL = "text-embedding-ada-002"` and asserts
`len(vector) == 1536` before the first upsert.

> Migrating to a newer embedding model is a separate project: build a new
> index, backfill all ~35K vectors, then repoint `server/main.py`. Out of scope.

## Library upgrade (do this first)

The pins in `pyproject.toml` are the actual blocker, and they are safe to lift.

### The naive bump does not resolve — two hard conflicts

My earlier claim that these upgrades were conflict-free was wrong. I checked
only whether langchain _named_ openai and pinecone, and ignored the version
bounds on its other core deps. Verified against PyPI metadata:

```
langchain 0.0.306  requires  anyio (<4.0),  numpy (>=1,<2),  langsmith (>=0.0.38,<0.1.0)
pinecone  10.0.0   requires  anyio>=4.0
→ ERROR: ResolutionImpossible
```

A second, independent chain blocks the voyageai bump: `voyageai 0.5.0` pulls
`langchain-text-splitters >=0.3.8` → `langchain-core >=0.3.51` → `langsmith

> =0.1.125`, contradicting langchain 0.0.306's `langsmith <0.1.0`. There is no
> escape version.

**So `langchain` 0.0.306 is the blocker, and it gates both upgrades.** It must
be dealt with first — it is not the "separate cleanup" I previously filed
under open questions.

### Yes — langchain can be dropped, and it is cheaper than expected

Audited every usage in the repo. It is doing almost nothing.

| Where                                                               | What it imports                                                            | Replaceable?                                                                                                                                                  |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `load_utils.py`, `load_conf.py`, `split_model.py`, `index_utils.py` | `Document`, `BaseLoader`                                                   | **Trivially.** `Document` is a pydantic v1 model with exactly two fields, `page_content` and `metadata`. `BaseLoader` is an ABC subclassed for structure only |
| `split_model.py`, `split_markdown.py`                               | `BaseDocumentTransformer`                                                  | ABC, same                                                                                                                                                     |
| **`split_markdown.py`**                                             | `Language`, `MarkdownHeaderTextSplitter`, `RecursiveCharacterTextSplitter` | **This is the only real langchain functionality in the repo — and the module is dead code, imported nowhere.** Delete the file                                |
| `notebooks/35`                                                      | `OpenAIEmbeddings`, `Pinecone` vectorstore                                 | Replaced by this script                                                                                                                                       |
| `notebooks/55`                                                      | `ChatOpenAI`, `RetrievalQA*`, `PromptTemplate`, `Pinecone`                 | **The one real casualty** — the RAG teaching demo                                                                                                             |
| `server/`                                                           | nothing                                                                    | Already langchain-free                                                                                                                                        |

The serialization format is preserved for free: `save_docs_to_jsonl` writes
`doc.json()`, and existing `.jsonl` files contain exactly
`{"page_content": …, "metadata": …}` — which a two-field dataclass reproduces
byte-identically. Verified against `data/split/output/2023-11-26.jsonl`.

So the work is: a ~10-line `Document` dataclass, drop two ABCs, `git rm models/split_markdown.py`. The actual cost is **notebook 55**, the RAG demo
used for teaching. It either keeps a pinned langchain in a separate notebook
env, or gets rewritten against the raw OpenAI + Pinecone SDKs — which is
arguably better teaching material anyway, since it stops hiding the mechanics
behind a chain abstraction.

**Decision: drop langchain.** That unblocks `pinecone ^10` and, if ever wanted,
`voyageai ^0.5` — and removes a years-stale dependency from the critical path
rather than working around it.

### Targets

| Package                 | Pinned now          | Target                               | Why                                                                                                                                                 |
| ----------------------- | ------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `openai`                | `^0.27.2` (0.27.10) | `^2.16.0`                            | Already proven in `server`                                                                                                                          |
| `pinecone-client[grpc]` | `^2.2.1` (2.2.4)    | **`pinecone` `^10.0.0`** (no extras) | v2 cannot reach serverless. Note `pinecone` 10 has **no `grpc` extra** — `pinecone.grpc` ships in the base wheel, so `extras = ["grpc"]` is invalid |
| `voyageai`              | `^0.1.3` (0.1.7)    | **leave at 0.1.7** for now           | 0.1.x works today (verified end-to-end). Optional once langchain is gone; no reason to churn it                                                     |
| `langchain`             | `^0.0.306`          | **removed**                          | See above. It is the only thing blocking the other bumps                                                                                            |

Both repos move together — see [Server upgrade](#server-upgrade).

### Code the upgrade touches

- **`split_utils.get_openai_embedder`** — `openai.Embedding.create(engine=...)`
  → `OpenAI(...).embeddings.create(model=...)`, and `res["data"][n]["embedding"]`
  → `res.data[n].embedding`. Verified on the server venv: openai 2.16.0 returns
  ada-002 at dim 1536, **L2 norm 1.0**, so the dot-product threshold assumption
  still holds.
- **`split_utils.get_voyageai_embedder`** — module-level
  `voyageai.get_embeddings(...)` is gone; 0.5.0 uses a client object
  (`voyageai.Client().embed(...).embeddings`). **The model string stays
  `voyage-01`** — only the call shape changes. Verify with the 8/8
  reproducibility test immediately after.
- **Notebooks 25, 35, 55** — openai and pinecone call sites.
- **`notebooks/35_conference_indexer.ipynb`** — also still calls
  `index(index, embedder, docs, batch_size)`, which `index_utils` no longer
  exports (it has `embed_documents` + `index_documents`).
- **Python version** — see [Removing rtx](#removing-rtx).

### Sequence

0. Land the 8/8 reproducibility test **first**, against the current pinned
   libraries, so there is a green baseline to upgrade against.
1. Settle the Python version; bump the three pins; `poetry lock && poetry install`.
2. `poetry run python -m spacy download en_core_web_sm` — **already done**; the
   model was missing (`spacy.load` raised `E050`) and is now installed in
   `.venv`. Add it to the nox/CI setup so it is not a manual step.
3. Port `get_openai_embedder` and `get_voyageai_embedder`; confirm both still
   return unit-norm vectors. Re-run the reproducibility test after each.
4. Run the pipeline at voyage-01@0.83.

Upgrade one library per commit, with the reproducibility test green between
each, so a regression is attributable.

## Chunking drift: resolved, there is none

The earlier concern was that `voyage-01` had been retired, forcing a fallback
embedder and an unvalidated threshold. With the fresh key in `models/.env`,
that turns out to be wrong.

### `voyage-01` is still served, and it is still the same model

| Check                | Result                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `voyage-01` responds | yes, echoes `"model": "voyage-01"`, dim 1024                                                                        |
| Unit-normalized      | L2 norm 1.000000 — the raw `np.dot` threshold is still a cosine                                                     |
| Reproducible         | identical vectors across calls (dot = 1.000000)                                                                     |
| Not a silent alias   | vs `voyage-2` dot = 0.012, `voyage-3` 0.029, `voyage-3.5` −0.064 — near-orthogonal, i.e. genuinely different spaces |

So **threshold 0.83 carries over unchanged.** No re-tuning, no fallback, no
corpus non-uniformity. Keep
`MarkdownSyntacticEmbeddingSplitter(split_threshold=0.83, max_chars=2000)`
exactly as `notebooks/22_split_model_trainer.ipynb` cell 47 left it.

### Proven end-to-end, not just argued

I re-ran the real pipeline — crawl → load → split at voyage-01@0.83 — against
`2025/04/43runia`, a talk already in the index, and compared
`get_doc_id` (sha256 of `url + "~" + text`) against the vectors Pinecone
already holds for that URL:

```
chunks in index for this talk: 8
regenerated chunks:            8
matched:                       8 / 8
missing from index:            []
in index but not regenerated:  []
```

Byte-for-byte. The pipeline reproduces 2025's chunk boundaries exactly today.
Crawl, loader selectors, splitter, and threshold are all unchanged in effect.

### Keep this as the upgrade regression test

That 8/8 check is the most valuable artifact to come out of this. It exercises
every stage at once and fails loudly on any semantic change — a moved chunk
boundary, a changed embedder, an altered markdown conversion. Ship it as
`tests/test_reproducibility.py` (network-marked, skipped by default) and run it:

- after each of the three library upgrades below,
- before every conference run,
- any time `load_conf.py` or the splitter changes.

If it still returns 8/8 after the upgrades, the upgrades changed nothing that
matters. That is a far stronger guarantee than the stripped notebook metrics
could ever have given.

> Still worth doing once, cheaply: run `split_model_eval.evaluate` over
> `data/split/labeled/2023-09-24.json` (75 labeled sections, still in the repo)
> at voyage-01@0.83 and **commit the Pk / WindowDiff numbers to a file**. The
> trainer's own outputs were eaten by `nbstripout`, so the project currently
> has no recorded baseline. This restores one.

## The index already has two eras

Verified by sampling and by re-embedding stored vectors:

| Era                         | IDs                       | Metadata keys                    | Embedding input |
| --------------------------- | ------------------------- | -------------------------------- | --------------- |
| 1980-04 → 2023-04 (~34,300) | integer (`31191`, `5936`) | 7                                | **text only**   |
| 2023-10 → 2025-04 (~1,150)  | sha256 of `url~text`      | 9 (adds `author_role`, `source`) | `title\n\ntext` |

Proof on a 1995 vector: cosine against a fresh ada-002 embedding of `text`
alone is **0.999860**; against `title\n\ntext` it is **0.976982**.

Consequences:

- Retrieval is already biased between eras, and has been since 2023-10. New
  talks will match the _recent_ convention, so this plan does not make it worse.
- **Idempotency only protects the sha256 era.** Content-hash IDs cannot collide
  with integer IDs, so any future run over pre-2023/10 material would silently
  duplicate rather than overwrite. Never point this script at those years
  without a delete-first step.

## Server upgrade

`server/` is on `pinecone-client` 3.2.2 — serverless-capable, so not broken,
but on the package PyPI has deprecated and renamed. Both repos should land on
`pinecone` 10 so there are not two divergent SDKs pointed at one index.

The surface is small — four lines in `server/server/main.py`:

| Line | Now                                                        | After                                                                                                                               |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 18   | `from pinecone.grpc import PineconeGRPC`                   | unchanged (still shipped under the `grpc` extra)                                                                                    |
| 48   | `pc = PineconeGRPC(api_key=pinecone_key)`                  | unchanged                                                                                                                           |
| 49   | `index = pc.Index(host=index_host)`                        | unchanged                                                                                                                           |
| 122  | `index.query(embedding, top_k=..., include_metadata=True)` | `index.query(vector=embedding, top_k=..., include_metadata=True)` — the positional vector was deprecated in v3 and is removed later |

`openai` is already at 2.16.0 there, so nothing to do on that side. Steps:

1. Swap `pinecone-client = {extras = ["grpc"], version = "^3.0.0"}` for
   `pinecone = {extras = ["grpc"], version = "^10.0.0"}` in `server/pyproject.toml`.
2. Make the `index.query` call keyword-args.
3. Run `server`'s own test suite (`tests/test_main.py`, `test_search_utils.py`),
   then hit `/search` against the live index and confirm results and deep links.
4. Deploy before the conference run, so a search regression is not discovered
   at the same time as an indexing one.

Do this **after** the models-side upgrade and the conference run, or on a
separate branch — changing the reader and the writer simultaneously makes a
failure ambiguous.

## Removing rtx

Yes, `.rtx.toml` can go. It is referenced by nothing automated:

- `rtx`, `mise`, and `asdf` are all absent from PATH (`asdf` resolves to a bare
  shell alias, and there is no `.tool-versions`).
- CI never consults it — `.github/workflows/tests.yml` sets up Python with
  `actions/setup-python@v4.5.0` and an explicit matrix.
- Only `README.md` lines 22 and 24 mention it.

So: `git rm .rtx.toml` and delete those two README lines.

**But it is masking a real inconsistency, so fix that in the same commit.**
Five sources disagree about the Python version:

| Source                            | Says                     |
| --------------------------------- | ------------------------ |
| `.rtx.toml`                       | 3.10                     |
| `noxfile.py:26` `python_versions` | `["3.10"]`               |
| CI matrix (7 sessions)            | 3.10                     |
| `pyproject.toml`                  | `^3.10.0` (permits 3.12) |
| **Actual `.venv`**                | **3.12.4**               |

Local development has silently been on 3.12 while every check targets 3.10.
Since you are upgrading libraries anyway, align on **3.12**: bump
`python_versions` in `noxfile.py`, the CI matrix, and `python = "^3.12"` in
`pyproject.toml` — and do the same for `server/pyproject.toml` (also `^3.10`).
Otherwise nox and CI keep testing an interpreter nobody runs.

## Credentials

| Need              | Source                                        | Note                                            |
| ----------------- | --------------------------------------------- | ----------------------------------------------- |
| OpenAI            | `models/.env` `OPENAI_API_KEY` + `OPENAI_ORG` | already correct                                 |
| Pinecone **prod** | `server/.env` `PINECONE_KEY`                  | **not** `models/.env`                           |
| Voyage            | `models/.env` `VOYAGE_API_KEY`                | refreshed; verified working against `voyage-01` |

Resolution order for the Pinecone key: `PINECONE_PROD_KEY` env var →
`../server/.env` `PINECONE_KEY` → abort with an explicit message. Never fall
back to `models/.env` `PINECONE_API_KEY` — that silently targets an empty dev
project. Do not copy the prod key into `models/.env`; read it where it lives.

## Pipeline

Each stage writes to disk, so a crash resumes rather than restarts. All paths
are under `data/update/<year>-<month>/`, kept separate from `data/load/raw/`
so the loader never re-processes the 3,268 archived talks (which would mean
re-embedding and re-upserting the entire corpus).

### Stage 1 — crawl

- Listing URL: `{HOST}/study/general-conference/{year}/{month}?lang=eng`
- Reuse `crawl_utils.get_page` / `save_page` and the notebook's `_is_talk_url`
  (6 path components, last not ending in `-session`).
- Skip files already on disk; `--delay` seconds between requests, default 10.
- Output: `data/update/<year>-<month>/raw/<year>-<month>-<slug>.json`
- **Abort the month unless the listing yields ≥30 talk URLs** (observed: 35,
  37, 38). "Abort if zero" is not enough — a half-published conference
  returning 14 talks would pass every other guard, index 14, and report
  success.
- A 200 response carrying a JS-rendered shell produces zero `div.body-block`
  matches, which the loader currently treats as skippable. Combined with the
  stage-2 guard below, that now fails loudly instead of silently indexing
  nothing.

### Stage 2 — load

- `ConferenceTalkLoader(raw_dir).load(verbose=True)` → markdown + metadata.
- Loader skips docs missing title or content (`load_conf.py:93-96`) and warns
  on missing author. **Abort on any skip unless `--allow-skips=N`** — printing
  the list is not a guard, since nothing reads it.
- Output: `data/update/<year>-<month>/load.jsonl` via `save_docs_to_jsonl`.

### Stage 3 — split

- `MarkdownSyntacticEmbeddingSplitter(split_threshold=0.83, max_chars=2000)` —
  the stock default, which uses `get_voyageai_embedder()` / `voyage-01`. No
  fallback embedder and no `--embedder` flag: the tuned configuration works, so
  the script should not offer a second, worse one.
- `max_chars=2000`, `anchor="anchor"` (defaults; the `anchor` metadata is what
  lets the server deep-link into a talk — `server/main.py:157-160`).
- Output: `data/update/<year>-<month>/split.jsonl`.
- Expect roughly 10-12 chunks per talk (~400 chunks per conference).

### Stage 4 — upsert

- `index_utils.embed_documents(embedder, docs, batch_size=100, delay=1.0)`
  embeds `f"{title}\n\n{page_content}"`. **Keep that shape** — but note the
  justification I gave earlier was wrong: only the ~1,150 vectors from 2023/10
  onward use it (see [Two eras](#the-index-already-has-two-eras)). Matching the
  recent convention is still correct.
- **`embedder` here is NOT `split_utils.get_openai_embedder`.** That returns a
  bare function; `embed_documents` calls `embedder.embed_documents(...)`, a
  langchain `Embeddings` object. Notebook 35 uses
  `langchain.embeddings.openai.OpenAIEmbeddings`, which binds
  `openai.Embedding` and raises `APIRemovedInV1` under openai 2.x. Write a
  small adapter exposing `.embed_documents()` over
  `OpenAI().embeddings.create(...)`. Verified safe: re-embedding stored
  vectors through the raw SDK gives cosine 0.999996+ against what is indexed.
- IDs from `index_utils.get_doc_id` — `sha256(url + "~" + text)`. Re-running is
  idempotent: unchanged chunks upsert onto themselves. **Edited** talks produce
  new IDs and leave the old chunk orphaned (see Open questions).
- Metadata per vector, matching what the server reads: `title`, `text`,
  `author`, `author_role`, `year`, `month`, `url`, `anchor`, `source`.
- Upsert batches of 100 via the `pinecone` 10 SDK (`Pinecone(api_key=...).Index(host=...)`),
  retrying on 429/5xx with backoff. Before the upgrade lands, the same thing
  works as a plain POST to `{INDEX_HOST}/vectors/upsert` with an `Api-Key`
  header — that is how the index was inspected for this plan.

#### Write-permission canary

The prod key has only ever been used read-only, so it may be scoped
`ReadOnly`. Before embedding anything, upsert a single throwaway vector under
id `__canary__` into namespace `""`, confirm 200, then delete it. A 403 here
aborts the run before a cent is spent on embeddings.

## Safety rails

- `--dry-run` runs stages 1-3 and prints what _would_ be upserted (count, ID
  samples, metadata of the first chunk) without touching Pinecone or spending
  embedding tokens on stage 4.
- Pre-flight `describe_index_stats`; print `totalVectorCount` before and after
  and report the delta. A delta far below the chunk count means IDs collided
  with existing vectors — expected on a re-run, suspicious on a first run.
- Refuse to run if a `{year, month}` filter query already returns matches,
  unless `--force`. Guards against double-indexing a conference.
- Log an `update_conference` run summary (counts per stage, elapsed, delta) to
  `data/update/<year>-<month>/run.json`.

## Verification

1. `totalVectorCount` grew by approximately the new-chunk count.
2. Filter query on the new `{year, month}` returns the expected talks.
3. Hit the live `/search` endpoint with a question answerable only from the new
   conference and confirm a new-conference result ranks in the top 3 with a
   working deep link.
4. Only after 1-3 pass, update the frontend year range (see
   [Frontend copy](#frontend-copy)) and deploy the client.

## Status — COMPLETE

All three missing conferences are indexed (2026-10-13). The index holds **36,237
vectors**, up from 35,454, and a slot-by-slot scan of every April and October from
1980 to 2026 now reports **no gaps**.

| Conference | Talks   | Chunks  | Index after |
| ---------- | ------- | ------- | ----------- |
| 2025-10    | 35      | 282     | 35,736      |
| 2026-04    | 37      | 239     | 35,975      |
| 2026-10    | 38      | 262     | 36,237      |
|            | **110** | **783** |             |

Verified for each: every planned chunk id present in production (783/783), the
observed delta equal to the expected delta, all 9 metadata keys intact, and stored
vectors matching fresh embeddings at cosine >= 0.999996. Live production retrieval
confirmed through `https://www.iloveconference.org/api/search` — a question answerable
only from the new talks returns them at ranks 1-3 with a working deep link.

## Run order

Three conferences, oldest first, so that if something goes wrong it goes wrong
on the oldest and least-visited content:

```console
poetry run python -m models.update_conference --year 2025 --month 10   # DONE 2026-10-13
poetry run python -m models.update_conference --year 2026 --month 04   # 37 talks
poetry run python -m models.update_conference --year 2026 --month 10   # 38 talks
```

No environment setup is needed. The script calls `load_dotenv()` itself and resolves
every credential: OpenAI and Voyage from `models/.env`, and the **prod** Pinecone key
from `server/.env` (never `models/.env`'s dev key). Verified by running it with
`OPENAI_API_KEY`, `VOYAGE_API_KEY`, `PINECONE_PROD_KEY`, `PINECONE_API_KEY` and
`PINECONE_KEY` all unset.

Run them as three separate invocations, not one batch, and run the
[Verification](#verification) steps after each. 2025-10 doubles as the
rehearsal: if the metadata shape, chunk IDs, or vector count come out wrong,
you find out on one conference instead of three.

## Cost

**110 talks** (35 + 37 + 38). Measured rate on 2025-04 is **8.7 chunks/talk**
(296 chunks across 34 talks), so roughly **960 chunks** — the earlier
"10-12 per talk / ~1,200 chunks" was high.

Embeddings happen on two different services, which the earlier estimate
conflated:

- **Voyage (`voyage-01`)** — called by the splitter to score paragraph-group
  adjacency. Larger call count than the chunk total, but cheap enough to
  disregard.
- **OpenAI (ada-002)** — called once per final chunk at index time, ~900
  embeddings of ≤2000 chars. Genuinely pennies.

Wall-clock is dominated by crawl politeness: 113 requests at `--delay 10` is
~19 minutes of sleeping alone, so budget **~25-30 minutes**, plus splitter
time. Note `crawl_utils.get_page`'s `delay_seconds` **defaults to 30**
(`models/crawl_utils.py:12`) — if `--delay` is not threaded through, the run
silently takes ~57 minutes.

## Frontend copy

The site advertises its coverage in one place —
`client/src/routes/+page.svelte:16`:

```
from 1980-2025 of The Church of Jesus Christ of Latter-day Saints
```

Change `1980-2025` to `1980-2026`. It is the only year reference in
`client/src` or `client/static`; there is no constant, config value, or build
artifact carrying the range, so one string edit is the whole change.

**Order matters: do this last.** The claim must trail the data, never lead it.
If the copy says 2026 before the vectors are live, every visitor who searches
for a 2026 talk gets a confidently wrong answer assembled from older talks —
worse than the site simply not claiming the year yet. Sequence:

1. Upsert and verify (below).
2. Confirm a 2026-specific query returns 2026 sources on the live site.
3. Only then change the copy and deploy the client.

Note the range is hand-maintained and will be stale again in six months. If
this script becomes the twice-yearly routine, deriving the upper bound from
the index — a `max(year)` the server exposes, or simply bumping it as a step
in this runbook — is worth the small effort. For now, a checklist item.

## Decisions

All settled. Recorded here so the reasoning is not re-litigated.

| #   | Question                      | Decision                                                                                                                                                                                                                            |
| --- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | langchain                     | **Drop it.** Dead-code module deleted, `Document` becomes a dataclass, notebook 55 rewritten or env-pinned. Unblocks `pinecone ^10`                                                                                                 |
| 2   | `--replace` for revised talks | **Not building it.** The script is never re-run over an indexed conference. The "refuse if `{year, month}` already has matches" rail stays as a mistake-guard, not a feature                                                        |
| 3   | Fix the two-era index split   | **Won't fix.** Retrieval bias between pre- and post-2023/10 is accepted. The hard constraint stands: never point this script at pre-2023/10 years, since content-hash IDs cannot overwrite integer IDs and would silently duplicate |
| 4   | Crawl guards                  | **Add them.** Abort unless the listing yields ≥30 talks; abort stage 2 on any loader skip unless `--allow-skips=N`                                                                                                                  |
| 5   | `_is_talk_url` hardening      | **Add it** — two conditions, below                                                                                                                                                                                                  |
| 6   | Server upgrade timing         | **After** the conference run, on its own branch                                                                                                                                                                                     |
| —   | Voyage cost                   | Cheap enough to ignore                                                                                                                                                                                                              |
| —   | Scheduled runs                | **No.** Manual script, run twice a year                                                                                                                                                                                             |

### The `_is_talk_url` fix (decision 5)

Current predicate checks only segment count and a `-session` suffix. Add:

```python
path.startswith(f"/study/general-conference/{year}/{month}/")
and parse_qs(urlparse(url).query).get("lang") == ["eng"]
```

Without the first, a 6-segment scripture URL like `/study/scriptures/bofm/alma/5`
matches and indexes as `year="bofm", month="alma"`. Without the second, a
`?lang=spa` link maps to the same filename as the English talk and whichever is
crawled first wins. Neither is currently triggered — all 88 links across the
four listing pages were English general-conference URLs — so this is hardening
against a latent bug, not fixing a live one.
