from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.internet import reactor
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp import auth

from utils import WAMP_URL
from utils import CRA_USERNAME
from utils import CRA_SECRET
from utils import WAMP_REALM

class WAMPSession(ApplicationSession):

    def onConnect(self):
        self.log.info('transport connected')
        self.join(WAMP_REALM, [u"wampcra"], CRA_USERNAME)

    def onChallenge(self, challenge):
        self.log.info('authentication challenge received')
        if challenge.method == u"wampcra":
            if u'salt' in challenge.extra:
                self.log.error("we are out of salt")
            else:
                signature = auth.compute_wcs(CRA_SECRET,
                                             challenge.extra['challenge'])
                return signature
        else:
            raise Exception("Invalid authmethod {}".format(challenge.method))

    # @inlineCallbacks
    def onJoin(self, details):
        self.log.info("Successfully joined")

    @inlineCallbacks
    def get_regs(self):
        registrations = yield self.call("wamp.registration.list")
        returnValue(registrations)

    @inlineCallbacks
    def get_reg(self, reg):
        registration = yield self.call("wamp.registration.get", reg)
        returnValue(registration)

    @inlineCallbacks
    def get_reg_callees(self, reg):
        callees = yield self.call("wamp.registration.count_callees", reg)
        returnValue(callees)

    def onLeave(self, details):
        self.log.info('session left: {}'.format(details))
        self.disconnect()

    def onDisconnect(self):
        self.log.info('transport disconnected')
        reactor.stop()

runner = ApplicationRunner(WAMP_URL, WAMP_REALM)

if __name__ == '__main__':
    runner.run(WAMPSession)