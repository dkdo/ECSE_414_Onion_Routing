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

    def handle(self):


        cur_thread = threading.current_thread()
        data = self.request.recv(self.buffer)

        if "key" in data:
            self.key = data["key"]
            self.request.send(self.key)
            return

        onion = json.loads(data)

        #How does each node know what key to use?
        onion = decrypt(onion, 1)

        #If Still more nodes to traverse
        if "IP" in onion:
        #Read information
            print "Sending to", onion["IP"]
            nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            nodeAddress = ("localhost", onion["IP"])
            nodeSocket.connect(nodeAddress)
            nodeSocket.send(onion["data"])

            time.sleep(50.0 / 1000.0) # something thread just delete before sending . Slowing the program down
            response = nodeSocket.recv(1024)
            # How does each node know what key to use?
            response = encrypt(response, 1)
            self.request.send(response)
        #Message has reached destination
        else:
            print "Destination Reached, Going back"
            response = "Data has reach dest node"
            self.request.send(response)


class ThreadedOnionRouter(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass