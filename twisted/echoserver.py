from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

### Protocol Implementation

# This is just about the simplest possible protocol
class Echo(Protocol):
    def connectionMade(self):
        # Echo object has a factory attribute.
        self.factory.client_num += 1

    def connectionLost(self, reason):
        self.factory.client_num -= 1
    
    def dataReceived(self, data):
        print self.factory.client_num, data
        self.transport.write(data)

class EchoFactory(ServerFactory):
    protocol = Echo  # protocl is a Class attribute

    def __init__(self):
        self.client_num = 0


def main():
    f = EchoFactory()
    reactor.listenTCP(8000, f) # Low-level API
    reactor.run()

def main2():
    endpoint = TCP4ServerEndpoint(reactor, 8000) # High-level API
    endpoint.listen(EchoFactory())
    reactor.run()

if __name__ == '__main__':
    main()
