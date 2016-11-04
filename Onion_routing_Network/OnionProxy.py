import SocketServer
import OnionRoutingNetwork
import threading
import time
import socket
from Encrypt import encrypt, decrypt, generateKeys
import json

class onionProxyHandler(SocketServer.BaseRequestHandler):
    buffer = 1024
    #Find the funnel address
    entrySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    keySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def waitingThreads(self):
        print  "Number of Waiting Threads currently :", len(self.listOfThreads), "\n"

    #TODO
    def validRequest(self, request):
       return True

    def sendToEntryFunnel(self,data):
        print "Sending to entry funnel", data["IP"]
        entryFunnelAddress = ('localhost', data["IP"])
        self.entrySocket.connect(entryFunnelAddress)
        self.entrySocket.send(data["data"])

        time.sleep(50.0 / 1000.0);  # something thread just delete before sending . Slowing the program down
        response = self.entrySocket.recv(1024)
        return response

    def assembleOnion(self,request):
        onion = request ["Message"]
        keys = generateKeys (len (request["Path"]))[::-1]

        for i, IP in request["Path"][1::-1]:
            self.keySocket.connect ("localhost", IP)
            self.keySocket.send(keys[i])#KEY)
            time.sleep(5/100);
            if (self.keySocket(1024) != keys[i]):
                error = "The format of the message is not correct, please resend!\n"
                self.request.send(error)
                return
            onion = encrypt(json.dumps({"IP" : IP, "data": onion}), keys[i])
        onion = json.dumps({"IP" : request["Path"][0], "data": onion}
        return onion

    def peelOnion (self, request, onion):
        for key in request["Path"]:
            onion = decrypt(onion, key)
        return onion

    def handle(self):
        data = self.request.recv(self.buffer)
        cur_thread = threading.current_thread()
        print "Received request from the Proxy Server\n"

        message = json.loads(data)

        process = self.validRequest(message)
        if process:
            onion = self.assembleOnion(message)
            response =  self.sendToEntryFunnel(onion)
            response = self.peelOnion(message, response)
            self.request.send(json.dumps(response))

        else:
            error = "The format of the message is not correct, please resend!\n"
            self.request.send(error)

        return

class ThreadedProxyOnion(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
