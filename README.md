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

## Run

Run Jupyter Notebook in VS Code using virtualenv, be sure to select the right Python Interpreter and Notebook Kernel. In Windows, select env\Scripts\python.exe

## Sniff HTTP Requests

To sniff HTTP requests in Fiddler, we need to get http requests in Python to use the Windows Certificate Store. Installing the [pip_system_certs](https://pypi.org/project/pip-system-certs/) package does just that:

```
pip install pip_system_certs
```

This package is already listed in requirements.txt

Open Fiddler, enable `Capturing`, and requests (even the ones running in Jupyter Notebook) will appear in Fiddler.

### pip_system_certs

It seems that pip_system_certs doesn't work immediately after it's installed (http requests with Fiddler capturing results in cert error). Only when venv gets recreated and pip_system_certs installed via `pip install -r requirements.txt` does it seem to work properly.
