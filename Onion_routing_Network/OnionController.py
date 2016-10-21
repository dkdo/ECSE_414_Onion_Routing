import threading
import SocketServer
import OnionProxy
import ProxyServer
import Application
import OnionRoutingNetwork
import random

#Need capability to write raw input into functions (later)

#Put this in functions laters

# create proxy server
proxyHandler = ProxyServer.ProxyServerHandler
proxyServerPort = 150
proxyServerAddress = ('localhost', proxyServerPort)
proxyServer = ProxyServer.ThreadedProxyServer(proxyServerAddress, proxyHandler)

# create onion proxy
proxyOnionHandler = OnionProxy.onionProxyHandler
proxyOnionPort = 200
proxyOnionAddress = ('localhost', proxyOnionPort)
proxyOnion = OnionProxy.ThreadedProxyOnion(proxyOnionAddress, proxyOnionHandler)


proxyServerThread = threading.Thread(target = proxyServer.serve_forever)
proxyOnionThread = threading.Thread(target = proxyOnion.serve_forever)

#Start proxy server
proxyServerThread.setDaemon(True)  #  close thread when it's done
proxyServerThread.start()

#Start proxy onion
proxyOnionThread.setDaemon(True)
proxyOnionThread.start()

#create nodes for the network graphic


#Generate nodes for the graph

portList = []
for i in range(100):
    portList.append(i)

for i in range(20):
    address = ('localhost', portList[i])
    OnionRoutingNetwork.OnionRouter(address)

# create Client
clientPort = 300
message = "7"
client = Application.Application(clientPort,proxyServerAddress,message)
client.connectToServer()

print threading.active_count()

#client2 = Application.Application(clientPort,proxyServerAddress,message)
#client2.connectToServer()


