import threading
import SocketServer

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
    def handle(self):
        return

class ThreadedOnionRouter(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass





