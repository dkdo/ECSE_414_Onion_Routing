import random

#return the all path between 2 nodes in a graph
def findPaths (graph , start, end, path =[]):
    path = path + [start]
    longest = None;

    if start == end:
        return [path]
    if start not in graph:
        return None;

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findPaths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


#Generate graph with n node each with atleast v vertex each
def generateGraph (nodes, vertex):

    graph = {}
    #Instantiate Graph
    for i in range (1, nodes + 1):
        graph[i] = []

    #Randomly Connect graph
    for i in range (1, nodes + 1):
        while len(graph[i]) < vertex:
            x = random.randint (1, nodes)
            if not x == i and x not in graph[i]:
                graph[i].append(x)
                graph[x].append(i)

    return graph

#find the shortest path between 2 nodes in the graph
def shortest_path(graph, src, dest, path=[],counter=0):
    path = path + [src]

    if src == dest:
        return path
    
    if not graph.has_key(src):
        return None

    shortest = None

    for node in graph[src]:
        if node not in path:
            print path 
            newpath = shortest_path(graph, node, dest, path)
            print "after" + str(newpath)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
                    print "Shortest " + str(shortest)

    return shortest
    

   
