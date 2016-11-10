import SocketServer
import socket
import threading
import time


class ProxyServerHandler(SocketServer.BaseRequestHandler):
    buffer = 4096
    listOfThreadsWaitingForResponse = []
    # Find way to acquire onion Address
    onionAddress = ('localhost', 9999)

    # TODO
    def validRequest(self,request):
            return True

    def sendToOnionProxy(self,data,OnionAddress):
        onionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        onionSocket.connect(OnionAddress)
        onionSocket.send(data)
        time.sleep(5 / 1000);  # something thread just delete before sending . Slowing the program down
        onionResponse = onionSocket.recv(self.buffer)
        # time.sleep(50.0 / 1000.0);
        self.request.send(onionResponse)

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

        else:
            error = "The format is not correct, please resend\n"
            self.request.send(error)

class ThreadedProxyServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
