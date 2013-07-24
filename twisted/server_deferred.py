from twisted.internet import protocol, reactor, defer
from twisted.protocols import basic
from twisted.python.failure import Failure

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        d = defer.succeed(self.factory.getUser(user))
        #d = defer.succeed(self.factory.getUserFailure(user))

        def onError(err): # this is NOT method
            return 'Internal error in server'
        d.addErrback(onError)

        def writeResponse(message): # this is NOT method
            self.transport.write(message + '\r\n')
            self.transport.loseConnection()
        d.addCallback(writeResponse)

class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, **kwargs):
        self.users = kwargs

    def getUser(self, user):
        return self.users.get(user, 'No such user')

    def getUserFailure(self, user):
        # for test purpose!!!!
        return Failure()

reactor.listenTCP(8000, FingerFactory(moshez='Happy and well'))
reactor.run()
