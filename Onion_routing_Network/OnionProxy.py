import SocketServer
import OnionRoutingNetwork

class onionProxyHandler(SocketServer.BaseRequestHandler):
    buffer = 1024
    #Find the funnel address
    entryFunnelAddress = ()

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
        print "Received request\n"

        if self.validRequest(data):
            self.assembleOnion(data)
            self.createPath()
            self.sendToEntryFunnel(self.entryFunnelAddress)

        else:
            error = "The format of the message is not correct, please resend"
            data = self.request.send(error)

        return
