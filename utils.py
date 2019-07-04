import os

WAMP_URL = u"ws://crossbar/ws/"
WAMP_URL = os.getenv('WAMP_URL', WAMP_URL)

WAMP_REALM = "realm1"
WAMP_REALM = os.getenv('WAMP_REALM', WAMP_REALM)

CRA_USERNAME = "backend"
CRA_USERNAME = os.getenv('CRA_USERNAME', CRA_USERNAME)

CRA_SECRET = "quartabiz"
CRA_SECRET = os.getenv('CRA_SECRET', CRA_SECRET)

JOIN_TIMEOUT = 2