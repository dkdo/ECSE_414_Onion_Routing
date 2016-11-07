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

        onion = decrypt(data, self.key)
        print data
        layer = json.loads(data)

        #If Still more nodes to traverse
        if "IP" in layer:
        #Read information
            print "Sending to", layer["IP"]
            nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            nodeAddress = ("localhost", layer["IP"])
            nodeSocket.connect(nodeAddress)
            nodeSocket.send(json.dumps(layer["data"]))

            time.sleep(50.0 / 1000.0) # something thread just delete before sending . Slowing the program down
            response = nodeSocket.recv(self.buffer)
            response = encrypt(response, self.key)
            self.request.send(response)
        #Message has reached destination
        else:
            print "Destination Reached, Going back"
            response = "Data has reach dest node"
            self.request.send(response)


class ThreadedOnionRouter(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass