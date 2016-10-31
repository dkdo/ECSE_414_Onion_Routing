import GraphGenerator as GG
import Graph as G
import RandomWalk

graph = GG.generate_graph("ok.brite")
src = 0
dest = 4
print graph
print "src : " + str(src)
print "dest : " + str(dest)



print RandomWalk.randomWalk(graph,src,dest)