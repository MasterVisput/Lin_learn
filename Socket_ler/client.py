import socket

addr_and_port = ('localhost', 8888)
my_socket = socket.socket()
my_socket.connect(addr_and_port)
data = my_socket.send(b'Hello net!')
print('Send ', data, 'bytes')

my_socket.close()

