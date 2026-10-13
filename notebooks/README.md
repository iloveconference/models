# Notebooks

Indexing a new conference is **not** done here — use the guarded CLI:

```console
poetry run python -m models.update_conference --year 2026 --month 10
```

See the repo README. The notebooks that used to perform the crawl / load / split /
index stages by hand (`05_conference_crawler`, `15_conference_loader`,
`25_conference_splitter`, `35_conference_indexer`) were removed when that CLI landed:
they had no era guard, no crawl floor, no loader-skip guard and no rollback manifest,
and keeping an unguarded second path to the production index was the larger risk.
`05_magazine_crawler` went at the same time — a second pipeline with no inputs on
disk and a `# TODO remove break` that had truncated it since 2023.

Most of these read a `data/` directory that is not in git:

```console
aws s3 sync s3://iloveconference.data data
```

## What is here

### Splitter training — how the production chunking was chosen

| Notebook                         | Purpose                                                                                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `20_split_tolabel_data_gatherer` | samples talk sections and prepares them for labelling in Label Studio                                                                                                       |
| `21_split_labeled_data_gatherer` | turns the Label Studio export into `data/split/labeled/`                                                                                                                    |
| `22_split_model_trainer`         | the bake-off: compares OpenAI / MPNet / BGE / Voyage embeddings and thresholds, and is the record of why production splits at **voyage-01, threshold 0.83, max_chars 2000** |

`22` is the provenance for the splitter settings that `tests/test_reproducibility.py`
now pins. It needs `scikit-learn` and `pandas`, which are not project dependencies —
install them into the kernel yourself.

### Retrieval evaluation

| Notebook                                     | Purpose                                                  |
| -------------------------------------------- | -------------------------------------------------------- |
| `40_rank_eval_tolabel_results_gatherer`      | finds queries and results needing labels                 |
| `41_rank_eval_labeled_results_gatherer`      | processes labelled results into evaluation format        |
| `45_rank_eval_evaluator`                     | scores embedders with NDCG@3/5/10                        |
| `46_rank_eval_more_tolabel_results_gatherer` | generates more unlabelled results by comparing embedders |

### Other

| Notebook               | Purpose                                                                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `16_load_analyzer`     | inspect loaded documents                                                                                                                                                |
| `55_question_answerer` | the RAG demo — embed the question, query the index, build a prompt, answer with sources. Uses the raw OpenAI and Pinecone SDKs; langchain was dropped from this project |

## A warning about the index

`55` and `45` read the production index. Nothing here should ever write to it —
`models/index_utils.py` holds the only `upsert`, and the only supported caller is
`update_conference.py`. If you point a notebook at Pinecone, use the development key
in `models/.env`, never the production key (which lives in `../server/.env`).
