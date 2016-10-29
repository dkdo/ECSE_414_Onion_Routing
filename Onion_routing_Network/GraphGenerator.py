def generate_graph(brite_file):
    with open(brite_file) as f:
        content = f.readlines()

    edge_reading = False
    graph = {}

    for line in content:
        if 'Nodes:' in line:
            for token in line.split():
                # the wanted line will be similar to Nodes: ( 5 )
                if token.isdigit():
                    for i in range(0, int(token)):
                        graph[i] = []
                    break
        if edge_reading:
            # the edges are stored as:
            # edgeid from_node to_node etc...
            tokens = line.split()
            graph[int(tokens[1])].append(int(tokens[2]))
            graph[int(tokens[2])].append(int(tokens[1]))
        if 'Edges:' in line:
            edge_reading = True
        if '\n' == line:
            edge_reading = False

    return graph
