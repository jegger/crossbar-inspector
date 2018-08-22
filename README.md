What is this?
=============
This is some sort of cli-tool to interact with a crossbar instance.
You can as e.g. list all registered procedures on crossbar. Or call a procedure.


How to install
==============
This is a python3 app.
1. virtualenv -p python3 venv
2. venv/bin/pip install -r requirements.txt


How to use
==========
venv/bin/python main.py

Use the following evnironment variables for configuration:
- WAMP_URL (default to "crossbar")
- WAMP_REALM (default to "realm1")
- CRA_USERNAME (the username for the CRA authentication, default to "backend")
- CRA_SECRET (the secret for the CRA authentication)


### How to list registrations
WAMP_URL=ws://my-crossbar.com/ws venv/bin/python main.py reg list
