import socket
import sys
import httplib


try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg :
    print ("Failed to create socket")
    sys.exit();

print ("socket created")

host = 'www.google.com'
port = 80

try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Hostname could not be solve, Exiting"
    sys.exit()

print 'IP address of ' + host + ' is ' + ip

clientSocket.connect((ip,port))
print('Connected to %s' % host)


#Send Data to server

message = "GET / HTTP/1.1\r\n\r\n" # get main page of site

try:
    #Set the whole string
    clientSocket.sendall(message)

except  socket.error:
    print 'send failed'
    sys.exit()

print 'Message is sent'

received_data = clientSocket.recv(8192)

print received_data

