import socket
s1 = socket.socket()  
s1.connect(('127.0.0.1',5125))
s1.send('101010'.encode())