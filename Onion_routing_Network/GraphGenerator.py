def generate_graph():
    with open('test.brite') as f:
        content = f.readlines()
    node_reading = False
    edge_reading = False
    graph = {}
    for line in content:
        if 'Nodes:' in line:
            for token in line.split():
                if token.isdigit():
                    for i in range(0, int(token)):
                        graph[i] = []
                    break
        if edge_reading:
            tokens = line.split()
            print '\nin edge reading'
            for token in tokens:
                print token
            graph[int(tokens[1])].append(int(tokens[2]))
            graph[int(tokens[2])].append(int(tokens[1]))
        if 'Edges:' in line:
            edge_reading = True
        if '\n' == line:
            edge_reading = False

    print '\ngraph'
    print graph
    for node, edges in graph.items():
        if node == 0:
            print node
            print ': '
            print edges

generate_graph()
