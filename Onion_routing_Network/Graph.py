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
def shortest_path1(graph, src, dest, path=[],counter=0):
    path = path + [src]

    if src == dest:
        return path
    
    if not graph.has_key(src):
        return None

    shortest = None

    for node in graph[src]:
        if node not in path:
            # print path 
            newpath = shortest_path(graph, node, dest, path)
            # print "after" + str(newpath)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
                    # print "Shortest " + str(shortest)

    return shortest




def shortest_path(graph, src, dest):
  visited = {src: 0}
  path = {}

  nodes = set(graph)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph[min_node]:
      weight = current_weight + 1 #assume weight of 1 per edge
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node


  curNode = dest
  shortest = [curNode]
  while curNode != src:
    curNode = path[curNode]
    shortest.insert(0, curNode)


  return shortest

   
