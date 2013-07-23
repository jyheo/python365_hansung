from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

### Protocol Implementation

# This is just about the simplest possible protocol
class Echo(Protocol):
    def dataReceived(self, data):
        """
        As soon as any data is received, write it back.
        """
        print data
        self.transport.write(data)

class EchoFactory(Factory):
    def __init__(self, proto):
        self.protocol = proto

    


def main():
    f = ServerFactory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()

def main2():
    endpoint = TCP4ServerEndpoint(reactor, 8000)
    endpoint.listen(EchoFactory(Echo))
    reactor.run()

if __name__ == '__main__':
    main2()
