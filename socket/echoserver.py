import socket

host = ''
port = 8123
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
	# client is an instance of socket
    data = client.recv(size)
    if data:
        print 'Received:', len(data), 'bytes, Contents:', data
        client.send(data)
    client.close()

# Never here! ;-)
s.close()
