import socket

host = 'localhost'
port = 8123
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
sent = s.send('Hello, world')
print 'Sent %d bytes' % (sent)
data = s.recv(size)
s.close()
print 'Received:', len(data), 'bytes, Contents:', data
