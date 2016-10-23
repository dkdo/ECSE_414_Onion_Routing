import threading
import SocketServer
import OnionProxy
import ProxyServer
import Application
import OnionRoutingNetwork
import random
from Graph import generateGraph, findPaths

#Need capability to write raw input into functions (later)

#Put this in functions laters

#Create Graph
network = generateGraph(9,4)

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
for key in network:
    address = ('localhost', key)
    OnionRoutingNetwork.OnionRouter(address)

# create Client
clientPort = 300
#Choose a random port as destination and add it to the message (default start is 0)
dest = random.randint(2,len(network))

path = findPaths(network, 1, dest)
print "Sending message through", max(path)

message = ''.join(str(w) for w in max(path))

client = Application.Application(clientPort,proxyServerAddress,message)
client.connectToServer()

print threading.active_count()

#client2 = Application.Application(clientPort,proxyServerAddress,message)
#client2.connectToServer()




