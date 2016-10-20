import SocketServer
import socket

class ProxyServerHandler(SocketServer.BaseRequestHandler):
    buffer = 1024
    # Find way to acquire onion Address
    onionAddress = ('localhost', 200)

    # testing a valid message
    def validRequest(self,request):
        if (request.isdigit()):
            return True
        else:
            return False

    def sendToOnionProxy(self,data,OnionAddress):
        onionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        onionSocket.connect(OnionAddress)
        onionSocket.send(data)
        print "Sent a message to %s, %s" % self.onionAddress

    def handle(self):
        print "Received request\n"

        data = self.request.recv(self.buffer)
        process = self.validRequest(data) # if message was a string then proceed to sending it to onion proxy

        if (process):
            self.sendToOnionProxy(data, self.onionAddress)

        else:
            error = "The format is not correct, please resend"
            self.request.send(error)

        return