import socket
import sys

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg :
    print ("Failed to create socket")
    sys.exit();

print ("socket created")

server_address = (socket.gethostname(), 10000)
print('connecting to %s port %s' % server_address)
clientSocket.connect(server_address)

try:
    message = 'This is the message. It will be repeated.'  #send message
    print('sending %s' % message)
    clientSocket.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = clientSocket.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    clientSocket.close()

