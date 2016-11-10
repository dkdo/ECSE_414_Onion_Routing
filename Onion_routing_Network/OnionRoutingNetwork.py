import threading
import SocketServer
import time
import socket
import json
from Encrypt import encrypt, decrypt

class OnionRouter():
    address =0
    onionRouterHandler = ()
    onionRouter = ()


    def __init__(self, address):
        self.address = address
        self.onionRouterHandler = OnionRouterHandler
        # Start onion router

        self.onionRouter = ThreadedOnionRouter(address,OnionRouterHandler)
        OnionRouterThread = threading.Thread(target=self.onionRouter.serve_forever)
        OnionRouterThread.setDaemon(True)  # close thread when it's done
        OnionRouterThread.start()

class OnionRouterHandler(SocketServer.BaseRequestHandler):
    key = ""
    buffer = 4096
    onionProxyPort = 9999

    def requestKey(self):
        # send key to node
        keySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        keySocket.connect(('localhost', self.onionProxyPort))
        requestForKey = "requestForKey"
        keySocket.send(json.dumps(requestForKey))
       # time.sleep(5 / 100);

        responseForKey = keySocket.recv(self.buffer)
        self.key = responseForKey
        keySocket.close()

    def handle(self):

        cur_thread = threading.current_thread()
        data = self.request.recv(self.buffer)

        if  self.key == "":
            self.requestKey()

        #print "Current Message:", data


        onion = decrypt(data, self.key)
        layers = onion.split("~")

        #If Still more nodes to traverse
        if len(layers) > 1:
        #Read information
            print "Sending to", layers[0]
            nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            nodeAddress = ("localhost", int(layers[0]))
            #print nodeAddress
            nodeSocket.connect(nodeAddress)

            nodeSocket.send("~".join(layers[1::]))

            time.sleep(50.0 / 1000.0) # something thread just delete before sending . Slowing the program down
            response = nodeSocket.recv(self.buffer)
            response = encrypt(response, self.key)
            self.request.send(response)
        #Message has reached destination
        else:
            print "----------------------------------------------------"
            print "Destination Reached, Going back"
            print "Received Message at Terminal Node:", onion
            response = encrypt("Data has reach dest node", self.key)
            self.request.send(response)


class ThreadedOnionRouter(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass