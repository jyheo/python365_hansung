from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s\n" % msg)

        
def gotProtocol(proto):
    proto.sendMessage("Hello")
    reactor.callLater(1, proto.sendMessage, "This is sent in a second")
    reactor.callLater(2, proto.transport.loseConnection)

        
point = TCP4ClientEndpoint(reactor, "localhost", 8000)
deferred = connectProtocol(point, Greeter())
deferred.addCallback(gotProtocol)
reactor.run()
