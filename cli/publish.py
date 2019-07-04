import click

from operator import itemgetter
from texttable import Texttable
from inspector import runner
from inspector import WAMPSession
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor
from utils import JOIN_TIMEOUT


@click.command('publish')
@click.argument('uri')
@click.argument('args', nargs=-1)
def publish(uri, args):
    """ List all registrations.
    """
    session = WAMPSession()

    @inlineCallbacks
    def run():
        print("publish to: %s" % uri)
        yield session.publish(uri, *args)
        session.leave()

    reactor.callLater(JOIN_TIMEOUT, run)
    runner.run(session)