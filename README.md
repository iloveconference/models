# Models

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Overview

Models and code to process data for [I Love Conference](https://iloveconference.org).

Can be repurposed to create models and process data for any semantic search project.

## Requirements

- OpenAI API account: https://platform.openai.com/
- Pinecone account: https://www.pinecone.io/

## Installation

Requires Python 3.12.

Install dependencies using poetry: `poetry install`

Install nox: `poetry run pipx install nox && poetry run pipx inject nox nox-poetry`

Install pre-commit as a git hook: `poetry run pre-commit install`

Install spacy model: `poetry run python -m spacy download en_core_web_sm`

Create a `.env` file with the following variables:

```console
OPENAI_KEY=your_openai_api_key (found on API keys page)
OPENAI_ORG=your_openai_org (found on Settings page)
PINECONE_KEY=your_pinecone_api_key (found on API keys page)
PINECONE_ENV=your_pinecone_environment_name (found on API keys page)
```

## Adding a new conference

General Conference happens twice a year, in April and October. A week or so after it
ends, add it to the search index with one command per conference:

```console
poetry run python -m models.update_conference --year 2026 --month 10
```

That is the whole routine. No environment setup is needed — the script loads
`models/.env` itself and reads the **production** Pinecone key from `../server/.env`.
It never uses `models/.env`'s `PINECONE_API_KEY`, which points at an empty dev project.

It runs four stages, each writing to `data/update/<year>-<month>/` so a crash resumes
instead of restarting:

| Stage  | What it does                                                              |
| ------ | ------------------------------------------------------------------------- |
| crawl  | fetches the listing page and each talk, politely (`--delay`, default 10s) |
| load   | converts the HTML to markdown and extracts title, author, url, anchors    |
| split  | chunks each talk with the trained splitter (voyage-01, threshold 0.83)    |
| upsert | embeds each chunk with `text-embedding-ada-002` and writes to Pinecone    |

Expect roughly 6-10 minutes for a 35-talk conference, almost all of it the crawl delay.

### Before you write to production

Do a dry run first. It performs the crawl, load, and split for real, then prints
exactly what it would upsert without spending an embedding token or writing anything:

```console
poetry run python -m models.update_conference --year 2026 --month 10 --dry-run
```

Because stages are cached, the real run afterwards reuses that work and finishes in
under a minute.

### Useful flags

| Flag              | Why you would use it                                       |
| ----------------- | ---------------------------------------------------------- |
| `--dry-run`       | stages 1-3 for real, stage 4 preview only                  |
| `--delay N`       | seconds between site requests; minimum 8, default 10       |
| `--allow-skips N` | tolerate N talks the loader drops; default 0 aborts on any |
| `--force`         | override the already-indexed guards only                   |

### Guard rails

The script refuses rather than guesses. It will stop if the conference is earlier than
2023-10 (those vectors use a different, incompatible id scheme), if the listing yields
fewer than 30 talks (a half-published conference), if the loader drops any talk, if the
conference is already in the index, or if it cannot find the production key.

Before writing anything it records every chunk id it is about to upsert into
`data/update/<year>-<month>/run.json`. If a run goes wrong, roll back by deleting
exactly those ids — never by a `{year, month}` metadata filter, which would also delete
vectors from an earlier good run.

### Afterwards

Check the new talks are live, then bump the year range shown on the site
(`client/src/routes/+page.svelte`):

```console
curl -sG https://www.iloveconference.org/api/search --data-urlencode "q=<a question only the new talks answer>"
```

## Developing

Activate the poetry virtual environment: `poetry shell`

Periodically add the files you are working on to git and run `nox` to run all checks and tests as you develop.

If nox fails, you can run the individual checks and tests manually; e.g., `nox -s pre-commit`, `nox -s mypy-3.12`, or `nox -s tests-3.12`

Run `nox` before creating a pull request to ensure that all checks pass.

### Running notebooks

After running `poetry shell`, you need to install the poetry virtual environment as a jupyter kernel.

Let's name it "models": `python -m ipykernel install --user --name models`
You only need to do this once.

You can run notebooks either in VS Code, or in your browser.
To run notebooks in the browser, you run

`` env PYTHONPATH=`pwd` jupyter notebook ``

or (if you have fish shell)

`env PYTHONPATH=(pwd) jupyter notebook`

### Running Label Studio

`docker run -it -p 8080:8080 -v ~/iloveconference/labelstudio-data:/label-studio/data heartexlabs/label-studio:latest`

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Models_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/iloveconference/models/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/iloveconference/models/blob/main/LICENSE
[contributor guide]: https://github.com/iloveconference/models/blob/main/CONTRIBUTING.md
