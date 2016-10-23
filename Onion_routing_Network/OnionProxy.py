import SocketServer
import OnionRoutingNetwork
import threading
import time
import socket

class onionProxyHandler(SocketServer.BaseRequestHandler):
    buffer = 1024
    #Find the funnel address
    entrySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    entryFunnelAddress = ('localhost',1)

	

    def waitingThreads(self):
        print  "Number of Waiting Threads currently :", len(self.listOfThreads), "\n"

    def validRequest(self, request):
        if (request.isdigit()):
            return True
        else:
            return False

    # TO DO
    def sendToEntryFunnel(self,data):
        print "Sending to entry funnel (1)"
        self.entrySocket.connect(self.entryFunnelAddress)
        self.entrySocket.send(data[1:])

        time.sleep(50.0 / 1000.0);  # something thread just delete before sending . Slowing the program down
        response = self.entrySocket.recv(1024)
        return response

     #TO DO
    def assembleOnion(self,request):
        return

    #To do
    def createPath(self):
        return

    def handle(self):
        data = self.request.recv(self.buffer)
        cur_thread = threading.current_thread()
        print "Received request from the Proxy Server\n"

        process = self.validRequest(data)
        if process:
            message = "SENDING THIS POTATO BACK"
            #self.request.send(message) # send back data to proxy
            #self.assembleOnion(data)
            #self.createPath()
            response =  self.sendToEntryFunnel(data)
            #response = "Sending the onion to the entry funnel\n"
            self.request.send(response)

        else:
            error = "The format of the message is not correct, please resend\n"
            self.request.send(error)

        return

class ThreadedProxyOnion(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass