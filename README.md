# Python backend, HTML5+Javascript with Material Design Lite front-end sample

## Getting started

This code requires Python 3.7 and younger.

Before you start, you may want to setup the virtual environment for Python dependencies.

> Setting up Virtual environment:
> 0. `pip install virtualenv`
> 1. `python -m virtualenv venv`
> 2. execute `venv\Scripts\activate.bat` on windows or `venv/Scripts/activate` elsewhere

Install pre-requisites.

```bash
pip install -r requirements.txt
```

## Start service

```bash
python main.py
```

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
    "Action": "Pump_you_moron",
    "Params": [{ "Name": "Quickly"}],
    "IsStopped": false,
}
```

The page should display cards with buttons to end the process.
