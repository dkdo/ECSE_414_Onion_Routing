import threading
import SocketServer
import OnionProxy
import ProxyServer
import Application
import OnionRoutingNetwork
import random
import RandomWalk
from Graph import generateGraph,shortest_path, findPaths
from GraphGenerator import generate_graph
import json

#Need capability to write raw input into functions (later)

#Put this in functions laters

#Create Graph
#network = generateGraph(20,4)
network = generate_graph("twenty_nodes.brite")

print  "This is the network: ", network

# create proxy server
proxyHandler = ProxyServer.ProxyServerHandler
proxyServerPort = 150
proxyServerAddress = ('localhost', proxyServerPort)
proxyServer = ProxyServer.ThreadedProxyServer(proxyServerAddress, proxyHandler)

proxyServerThread = threading.Thread(target = proxyServer.serve_forever)

#Start proxy server
proxyServerThread.setDaemon(True)  #  close thread when it's done
proxyServerThread.start()


#create nodes for the network graphic

#Generate nodes for the graph
for key in network:
    address = ('localhost', key)
    OnionRoutingNetwork.OnionRouter(address)

# create Client
clientPort = 300
client2Port = 500

#Choose a random port as destination and add it to the message (default start is 1)
dest = random.randint(2,len(network))

randomPath = RandomWalk.randomWalk(network, 1, dest)
print "Sending message through", randomPath

message = "Is this a potato?"

data = {"Path" : randomPath , "Message" : message}

send = json.dumps(data);

client = Application.Application(clientPort,proxyServerAddress,send)
client.connectToServer()

shortestPath = shortest_path(network, 1, dest)
print "Sending message with shortest path : ", len(randomPath)

#client2 = Application.Application(client2Port,proxyServerAddress,send)
#client2.connectToServer()



#client2 = Application.Application(clientPort,proxyServerAddress,message)
#client2.connectToServer()
