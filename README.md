# LLM Notebooks

Jupyter Notebooks for experimenting with LLM.

## Setup

Install pyenv:

- Windows: [pyenv-win](https://github.com/pyenv-win/pyenv-win)
- WSL: https://gist.github.com/monkut/35c2ef098b871144b49f3f9979032cee

Environment:

1. Create a virtual environment: `python -m venv venv`
2. Activate virtualenv: `.\venv\Scripts\activate` (Windows), `source venv/bin/activate` (Linux)
3. Install packages from requirements.txt: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and populate variables

### Vertex AI

1. Enable `Vertex AI API` in Google Cloud Console
2. Create a service account with `Vertex AI User` role
3. Download service account key and save as `service-account.json` in root of this project

## Run

Run Jupyter Notebook in VS Code using virtualenv, be sure to select the right Python Interpreter and Notebook Kernel. In Windows, select env\Scripts\python.exe

## Sniff HTTP Requests

### Windows

Use [2. Old Solution (Not recommended)](https://docs.proxyman.io/debug-devices/python#2.-old-solution-not-recommended).

1. Download cert from Proxyman: Certificate -> Export -> Root Certificate as PEM...
2. Save that file to certs folder
3. Inside venv: `python proxyman.py add`
4. Paste relative path to cert file

To disable proxyman proxy:

1. Inside venv: `python proxyman.py remove`

### Mac

Use [1. New Automatic Solution (v4.7.0 or later)](https://docs.proxyman.io/debug-devices/python#1.-new-automatic-solution-v4.7.0-or-later).

When new Terminal launches, open vscode from there:

```
cd projects/llm-notebooks
code .
```
