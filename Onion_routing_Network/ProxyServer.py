import SocketServer
import socket
import threading
import time


class ProxyServerHandler(SocketServer.BaseRequestHandler):
    buffer = 1024
    listOfThreadsWaitingForResponse = []
    onionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Find way to acquire onion Address
    onionAddress = ('localhost', 200)

    # testing a valid message
    def validRequest(self,request):
        if (request.isdigit()):
            return True
        else:
            return False

    def sendToOnionProxy(self,data,OnionAddress):
        self.onionSocket.connect(OnionAddress)
        self.onionSocket.send(data)

    def waitingThreads(self):
        print "Number of Waiting Threads currently :",len(self.listOfThreads), "\n"


    def handle(self):
        print "Received request from client\n"
        cur_thread = threading.current_thread()
        data = self.request.recv(self.buffer)


        self.listOfThreadsWaitingForResponse.append(cur_thread)

        process = self.validRequest(data) # if message was a string then proceed to sending it to onion proxy

        if (process):
            print "The message is being transmitted to the onion proxy\n"
            self.sendToOnionProxy(data, self.onionAddress)
            time.sleep(50.0 / 1000.0); # something thread just delete before sending . Slowing the program down
            onionResponse = self.onionSocket.recv(1024)
            #time.sleep(50.0 / 1000.0);
            self.request.send(onionResponse)


        else:
            error = "The format is not correct, please resend\n"
            self.request.send(error)

class ThreadedProxyServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
