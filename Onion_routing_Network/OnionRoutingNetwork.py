import threading
import SocketServer
import time
import socket

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

    buffer = 1024

    def handle(self):
        cur_thread = threading.current_thread()
        data = self.request.recv(self.buffer)

        #If Still more nodes to traverse
        if (data != "EMPTY"):
        #Read information
            print "Sending to", data[:1]
            nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            nodeAddress = ("localhost", int(data[:1]))
            nodeSocket.connect(nodeAddress)
            if (len(data[1:]) == 0):
                data = "IEMPTY"
            nodeSocket.send(data[1:])

            time.sleep(50.0 / 1000.0) # something thread just delete before sending . Slowing the program down
            response = nodeSocket.recv(1024)
            self.request.send(response)

        #Message has reached destination
        else:
            print "Destination Reached, Going back"
            response = "Data has reach dest node"
            self.request.send(response)


class ThreadedOnionRouter(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
