import socket
import json
import time


class Application:
    port = 0
    clientAddress = ()
    serverAddress =()
    message = ""
    buffer = 4096

    def __init__(self,port,serverAddress,message):
        self.port = port
        self.serverAddress = serverAddress
        self.message = message
        self.clientAddress = ('localhost',port)

    def connectToServer(self):

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start_time = time.time()
        clientSocket.connect(self.serverAddress)
        try:
            clientSocket.sendall(self.message)
            response = clientSocket.recv(self.buffer)
            response = json.loads(response)
            print "Received Message at Application: {}".format(response)
        finally:
            clientSocket.close()
            print "Closed socket\n"
            elapsed_time = time.time() - start_time
            print "Time elapsed: ", elapsed_time
