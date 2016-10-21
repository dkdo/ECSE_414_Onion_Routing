import SocketServer
import OnionRoutingNetwork
import threading

class onionProxyHandler(SocketServer.BaseRequestHandler):
    buffer = 1024
    #Find the funnel address
    entryFunnelAddress = ()

    def waitingThreads(self):
        print  "Number of Waiting Threads currently :", len(self.listOfThreads), "\n"

    def validRequest(self, request):
        if (request.isdigit()):
            return True
        else:
            return False

    # TO DO
    def sendToEntryFunnel(self,request,Address):
        return

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
            self.assembleOnion(data)
            self.createPath()
            self.sendToEntryFunnel(data,self.entryFunnelAddress)
            response = "Sending the onion to the entry funnel\n"
            self.request.send(response)

        else:
            error = "The format of the message is not correct, please resend\n"
            self.request.send(error)

        return

class ThreadedProxyOnion(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass