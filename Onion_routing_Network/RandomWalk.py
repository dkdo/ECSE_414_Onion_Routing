import networkx as nx
import random



def randomWalk( G , SRC , DEST ):

    minHops = 7
    maxHops = 2 * 11    #2 times total of nodes
    Length = random.randint(minHops, maxHops)   #Randomly select a route length

    LengthFromSrc = 0
    LengthFromDest = 0
    TotalNumberHops= 0

    X = SRC     #Last node visited from random walk starting at SRC
    Y = DEST    #Last node visited from random walk starting at DEST
    Z = -1      #Next node adjacent to X or Y depending on the fair coin

    Next = ""   #Will be used to hold a fair coin ( with p(RandWalkFromSrc) = 0.5, p(RandWalkFromDest) = 0.5)

    path = [SRC,DEST]
    shortest_path=[]
    while TotalNumberHops < Length:

        Next = random.choice(("RandWalkFromSrc", "RandWalkFromDest"))
        
        if (Next == "RandWalkFromSrc"):
            maxNeighbors = len(G.neighbors(X))
            Z = G.neighbors(X)[random.randint(0,maxNeighbors-1)]    # Randomly select an adjacent node from X
            shortest_path_ZtoY = nx.shortest_path(G,Z,Y)
            shortest_path = shortest_path_ZtoY[1:len(shortest_path_ZtoY)-1]
            TotalNumberHops = 1 + LengthFromSrc + LengthFromDest + len(shortest_path)

            if TotalNumberHops > Length:
                # print "BACK UP"
                shortest_path_ZtoY = nx.shortest_path(G,X,Y)
                # print shortest_path_ZtoY
                shortest_path = shortest_path_ZtoY[1:len(shortest_path_ZtoY)-1]
                break

            X = Z
            path.insert(LengthFromSrc+1,X)
            LengthFromSrc+=1

        else: # Next = RandWalkFromDest
            maxNeighbors = len(G.neighbors(Y))
            Z = G.neighbors(Y)[random.randint(0,maxNeighbors-1)]    # Randomly select an adjacent node from X
            shortest_path_ZtoX = nx.shortest_path(G,X,Z)
            shortest_path = shortest_path_ZtoX[1:len(shortest_path_ZtoX)-1]
            TotalNumberHops = 1 + LengthFromSrc + LengthFromDest + len(shortest_path)

            #Next step would have to many hops, so we backtrack
            if TotalNumberHops > Length:
                # print " BACK DOWN"
                shortest_path_ZtoX = nx.shortest_path(G,X,Y)
                # print shortest_path_ZtoX
                shortest_path = shortest_path_ZtoX[1:len(shortest_path_ZtoX)-1]
                break

            Y = Z
            path.insert(-(LengthFromDest+1),Y)
            LengthFromDest+=1

    #when shortest_path is empty, meaning that the route has correctly generated a path without the use of bfs, need to check no duplicates
    if (path[LengthFromSrc]==path[LengthFromSrc+1]):
        del path[LengthFromSrc+1]
    
    path[LengthFromSrc+1:LengthFromSrc+1] = shortest_path

    return path

# #missing path + simple path
# #print "Length : " + str(Length)
# print "Shortest path : " + str(shortest_path)
# print "Path : " + str(path)
# print "Path : " + str([0]*(LengthFromSrc+1))
# #print "Number of hops (from Path) : " + str(len(path)-1)

# print LengthFromSrc

# #before adding make sure that 
# print "Path : " + str(path)

# Constructing the graph
G = nx.Graph()
node=6 
nodes = (1,2,3,4,5,6,7,8,9,10,11)
edges = ((1,2),(2,3),(2,5),(3,4),(3,6),(5,8),(5,6),(4,7),(6,7),(6,9),(8,9),(7,10),(9,10),(10,11))
G.add_nodes_from(nodes)
G.add_edges_from(edges)

SRC = 1
DEST = 11

print randomWalk(G, SRC, DEST)

#print "Current nodes " + str(G.nodes()) + " length : " + str(len(G.nodes()))
#print "Current edges " + str(G.edges()) + " length : " + str(len(G.edges()))
# print("Neighbors of %d " + str(G.neighbors(node))) %node)