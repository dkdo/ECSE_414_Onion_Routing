import socket
import json
import time


class Application:
    port = 0
    clientAddress = ()
    serverAddress =()
    message = ""
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buffer = 1024

    def __init__(self,port,serverAddress,message):
        self.port = port
        self.serverAddress = serverAddress
        self.message = message
        self.clientAddress = ('localhost',port)

    def connectToServer(self):

        start_time = time.time()
        self.clientSocket.connect(self.serverAddress)
        try:
            self.clientSocket.sendall(self.message)
            response = self.clientSocket.recv(1024)
            response = json.loads(response)
            print "Received: {}".format(response)
        finally:
            self.clientSocket.close()
            print "Closed socket\n"
            elapsed_time = time.time() - start_time
            print "Time elapsed: ", elapsed_time
