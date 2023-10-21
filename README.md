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

Install rtx: https://github.com/jdx/rtx

- when you cd to the project directory, rtx should install the correct version of python, poetry, and pipx

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

## Downloading data

`mkdir data`

`aws s3 sync s3://scripturecentralqa.data data --no-sign-request`

## Developing

Activate the poetry virtual environment: `poetry shell`

Periodically add the files you are working on to git and run `nox` to run all checks and tests as you develop.

If nox fails, you can run the individual checks and tests manually; e.g., `nox -s pre-commit`, `nox -s mypy-3.10`, or `nox -s tests-3.10`

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
