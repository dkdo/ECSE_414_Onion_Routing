import GraphGenerator as GG
import Graph as G
import RandomWalk

graph = GG.generate_graph("twenty_nodes.brite")
#graph = G.generateGraph(100,5)
src = 1
dest = 4
print graph
print "src : " + str(src)
print "dest : " + str(dest)



print RandomWalk.randomWalk(graph,src,dest)