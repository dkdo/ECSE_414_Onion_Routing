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
    def validRequest(self, request):
            return True

    def sendToOnionProxy(self, data, OnionAddress):
        onion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        onion_socket.connect(OnionAddress)
        onion_socket.send(data)
        # something thread just delete before sending. Slowing the program down
        time.sleep(5 / 1000)
        onion_response = onion_socket.recv(self.buffer)
        # time.sleep(50.0 / 1000.0);
        self.request.send(onion_response)

    def waitingThreads(self):
        print ('Number of Waiting Threads currently:', len(self.listOfThreads),
               '\n')

    def handle(self):
        print 'Received request from client\n'
        cur_thread = threading.current_thread()
        data = self.request.recv(self.buffer)
        self.listOfThreadsWaitingForResponse.append(cur_thread)
        # if message was a string then proceed to sending it to onion proxy
        process = self.validRequest(data)

        if (process):
            print 'The message is being transmitted to the onion proxy\n'
            self.sendToOnionProxy(data, self.onionAddress)

        else:
            error = 'The format is not correct, please resend\n'
            self.request.send(error)


class ThreadedProxyServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
