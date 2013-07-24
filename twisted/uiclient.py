from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from Tkinter import *
import threading
import sys

class uiThread(threading.Thread):
    
    def initUI(self):

        def sendMessage(msg):
            print 'Send: ' + msg
            self.client_obj.sendLine(msg)
        
        def buttonPressed():
            reactor.callFromThread(sendMessage, self.textvar.get())

        ##### Bad! cause Race Condition ################
        def buttonPressed2(): 
            print 'Send: ' + self.textvar.get()
            self.client_obj.sendLine(self.textvar.get())
            
        self.textvar = StringVar()
        widgets = [
            Label(self.app, text="Input Anything:"),
            Entry(self.app, textvariable=self.textvar),
            Button(self.app, text='Send', command = buttonPressed) ]

        for wdg in widgets:
            wdg.pack()

        self.textvar.set("Ready")

    def setClientObj(self, client):
        self.client_obj = client

    def connected(self):
        self.textvar.set("Connected")
        
    def run(self):
        self.app = Tk()
        self.initUI()

        self.app.mainloop()

        reactor.stop()

class EchoClient(LineReceiver):
    end="Bye-bye!"
    def connectionMade(self):
        self.sendLine("Hello, world!")
        self.sendLine("What a fine day it is.")
        #self.sendLine(self.end)
        
        self.factory.uit.connected()

    def lineReceived(self, line):
        print "receive:", line
        if line==self.end:
            self.transport.loseConnection()  
            # loseConnection:close gracefully(send all data in buffer), abortConnection(): close right now!

class EchoClientFactory(ClientFactory):
    #protocol = EchoClient

    def __init__(self):
        self.uit = uiThread()
        self.uit.start()

    def buildProtocol(self, addr):
        print addr
        client_obj = EchoClient()
        client_obj.factory = self
        self.uit.setClientObj(client_obj)
        return client_obj

    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        #reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        #reactor.stop()


    
def main():
    factory = EchoClientFactory()
    reactor.connectTCP('localhost', 8000, factory)
    reactor.run()

if __name__ == '__main__':
    main()
