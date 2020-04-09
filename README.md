# Python backend, HTML5+Javascript with Material Design Lite front-end sample

## Getting started

This code requires Python 3.7 and younger.

Before you start, you may want to setup the virtual environment for Python dependencies.

> Setting up Virtual environment:
>
> 1. `pip install virtualenv`
> 2. `python -m virtualenv venv`
> 3. execute `venv\Scripts\activate.bat` on windows or `venv/Scripts/activate` elsewhere

Install pre-requisites.

```bash
pip install -r requirements.txt
```

## Start service

```bash
python main.py
```

If using Visual Studio Code, just start the debugger. The `launch.json` contains configuration that starts the Python service and then opens the page in Chrome and attaches to the javascript debugger there.

## Initialize the page with observed data

Post this kind of message to `http://localhost:5000/update`:

```json
{
    "Atomics": {
        "water_is_rising": true,
        "water_level": 50
    }
}
```

e.g. using Postman.

Page should display input elements according to type (boolean vs numeric).

## Display a _process_

Post this kind of message to `http://localhost:5000/startstop`:

```json
{
    "Action": "run_checklist",
    "Params": [{ "Name": "Quickly"}],
    "IsStopped": false,
}
```

The template `index.html` includes cards for action named `run_checklist`
and `stay_safe`, but if you post any other action name, a dummy card is
created on the fly.

Post `"IsStopped": true` to complete the action without waiting for the user.

The page should display cards with buttons to end the process.
