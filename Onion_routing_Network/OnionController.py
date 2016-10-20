import threading
import SocketServer
import OnionProxy
import ProxyServer
import Application
import OnionRoutingNetwork

#Need capability to write raw input into functions (later)

#Put this in functions laters

# create proxy server
proxyHandler = ProxyServer.ProxyServerHandler
proxyServerPort = 150
proxyServerAddress = ('localhost', proxyServerPort)
proxyServer = SocketServer.TCPServer(proxyServerAddress, proxyHandler)

# create onion proxy
proxyOnionHandler = OnionProxy.onionProxyHandler
proxyOnionPort = 200
proxyOnionAddress = ('localhost', proxyOnionPort)
proxyOnion = SocketServer.TCPServer(proxyOnionAddress, proxyOnionHandler)


proxyServerThread = threading.Thread(target = proxyServer.serve_forever)
proxyOnionThread = threading.Thread(target = proxyOnion.serve_forever)

#Start proxy server
proxyServerThread.setDaemon(True)  #  close thread when it's done
proxyServerThread.start()

#Start proxy onion
proxyOnionThread.setDaemon(True)
proxyOnionThread.start()

# create Client
clientPort = 300
client = Application.Application(clientPort)
client.connectToServerSocket(proxyServerAddress)

#sending message Client to Proxy Server

message = "1"
client.displayClientAddress()
client.sendMessage(message)
client.receivedMessage()
