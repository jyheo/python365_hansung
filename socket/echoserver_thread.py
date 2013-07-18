import select 
import socket 
import sys 
import threading 

class Server: 
    def __init__(self): 
        self.host = '' 
        self.port = 8123
        self.backlog = 5 
        self.size = 1024 
        self.server = None 

    def open_socket(self): 
        try: 
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            self.server.bind((self.host,self.port)) 
            self.server.listen(self.backlog) 
        except socket.error, (value,message): 
            if self.server: 
                self.server.close() 
            print "Could not open socket: ", value, message 
            sys.exit(1) 

    def run(self): 
        self.open_socket()
        while 1: 
            # handle the server socket 
            c = Client(self.server.accept()) 
            c.start() 

class Client(threading.Thread): 
    def __init__(self,(client,address)): 
        threading.Thread.__init__(self) 
        self.client = client 
        self.address = address 
        self.size = 1024
        print 'Connected with ' + address[0] + ':' + str(address[1])

    def run(self):
        while 1: 
            data = self.client.recv(self.size) 
            if data: 
                self.client.send(data) 
            else: 
                self.client.close() 
                break
        print 'Connection closed ' + self.address[0] + ':' + str(self.address[1])

if __name__ == "__main__": 
    s = Server() 
    s.run()
