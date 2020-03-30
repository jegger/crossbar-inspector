import click

from operator import itemgetter
from texttable import Texttable
from inspector import runner
from inspector import WAMPSession
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor
from utils import JOIN_TIMEOUT


@click.group()
def sub():
    """For inspecting subscriptions on crossbar"""
    pass


@sub.command()
def fastlist():
    """List subscriptions without details"""
    session = WAMPSession()

    @inlineCallbacks
    def run():
        subs = yield session.get_subs()

        print("exact:", len(subs['exact']))
        print("prefix:", len(subs['prefix']))
        print("wildcard:", len(subs['wildcard']))

        session.leave()

    reactor.callLater(JOIN_TIMEOUT, run)
    runner.run(session)


@sub.command()
def list():
    """ List all subscriptions.
    """
    session = WAMPSession()

    @inlineCallbacks
    def run():
        subs = yield session.get_subs()

        _subs = []
        for sub_type in subs:
            for sub in subs[sub_type]:
                _sub = yield session.get_sub(sub)
                count = yield session.get_sub_count(sub)
                _sub["count"] = count
                _subs.append(_sub)

        t = Texttable(max_width=150)
        t.header(["uri", "match", "count"])
        t.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
        subs = sorted(_subs, key=itemgetter('uri'))
        for _sub in subs:
            t.add_row([_sub["uri"], _sub["match"], _sub["count"]])
        print(t.draw())
        session.leave()

    reactor.callLater(JOIN_TIMEOUT, run)
    runner.run(session)
