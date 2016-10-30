import GraphGenerator as GG
import Graph as G

graph = GG.generate_graph("ok.brite")
print graph
print G.shortest_path(graph,0,4)
if graph:
    print "hello"