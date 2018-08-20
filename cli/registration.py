import click

from operator import itemgetter
from texttable import Texttable
from inspector import runner
from inspector import WAMPSession
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor
from utils import JOIN_TIMEOUT


@click.group()
def reg():
    """For inspecting registrations on crossbar"""
    pass

@reg.command()
def list():
    """ List all registrations.
    """
    session = WAMPSession()

    @inlineCallbacks
    def run():
        regs = yield session.get_regs()

        # Fetch detailed info about registrations
        _regs = []
        for reg_type in regs:
            for reg in regs[reg_type]:
                _reg = yield session.get_reg(reg)
                callees = yield session.get_reg_callees(reg)
                _reg["callees"] = callees
                _regs.append(_reg)
        # Sort by uri
        t = Texttable(max_width=150)
        t.header(["uri", "invoke", "match", "callees"])
        t.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
        regs = sorted(_regs, key=itemgetter('uri'))
        for _reg in regs:
            t.add_row([_reg["uri"], _reg["invoke"],
                       _reg["match"], _reg["callees"]])

        print(t.draw())
        session.leave()

    reactor.callLater(JOIN_TIMEOUT, run)
    runner.run(session)

@reg.command()
@click.argument('uri')
@click.argument('args', nargs=-1)
def call(uri, args):
    session = WAMPSession()
    @inlineCallbacks
    def run():
        try:
            ret = yield session.call(uri, *args)
        except Exception as e:
            print(e)
        else:
            print(ret)
        session.leave()

    reactor.callLater(JOIN_TIMEOUT, run)
    runner.run(session)