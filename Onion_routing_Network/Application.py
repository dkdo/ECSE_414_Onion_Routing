import socket

class Application:
    port = 0
    clientAddress = ()
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buffer = 1024

    def __init__(self,port):
        self.port = port
        self.clientAddress = ('localhost',port)

    def displayClientAddress(self):
        print 'The client address is %s, port : %s\n' % self.clientAddress

    def connectToServerSocket(self,serverAddress):
        print('connecting to %s port %s\n' % serverAddress)
        self.clientSocket.connect(serverAddress)

    def sendMessage(self,message):
        print 'Preparing to send message :' + message +"\n"
        self.clientSocket.send(message)
        print 'Message sent\n'

    def receivedMessage(self):
        data = self.clientSocket.recv(self.buffer)
        print 'The received message : %s\n' % data