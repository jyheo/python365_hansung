import socket
import sys

host = 'localhost'
port = 8123
size = 1024
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
except socket.error, (value,message): 
    if s: 
        s.close() 
    print "Could not open socket: ", value, message 
    sys.exit(1)
    
while 1:
    text = raw_input('>>>')
    if text == 'exit':
        break;
    sent = s.send(text)
    print 'Sent %d bytes' % (sent)
    data = s.recv(size)
    print 'Received:', len(data), 'bytes, Contents:', data
    
s.close()
