import click

from operator import itemgetter
from texttable import Texttable
from inspector import runner
from inspector import WAMPSession
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor
from utils import JOIN_TIMEOUT


@click.group()
def sessions():
    """For inspecting sessions on crossbar"""
    pass

@sessions.command()
def count():
    """ Count number of sessions
    """
    session = WAMPSession()

    @inlineCallbacks
    def run():
        count = yield session.get_session_count()
        print(f"Session count: {count}")
        session.leave()

    reactor.callLater(JOIN_TIMEOUT, run)
    runner.run(session)
