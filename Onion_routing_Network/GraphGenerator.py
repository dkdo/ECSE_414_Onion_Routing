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
                    for i in range(1, int(token) + 1):
                        graph[i] = {'nodes': [],
                                    'length': []}
                    break
        if edge_reading:
            # the edges are stored as:
            # edgeid from_node to_node etc...
            tokens = line.split()
            graph[int(tokens[1]) + 1]['nodes'].append(int(tokens[2]) + 1)
            graph[int(tokens[1]) + 1]['length'].append(float(tokens[3]))
            graph[int(tokens[2]) + 1]['nodes'].append(int(tokens[1]) + 1)
            graph[int(tokens[2]) + 1]['length'].append(float(tokens[3]))
        if 'Edges:' in line:
            edge_reading = True
        if '\n' == line:
            edge_reading = False

    return graph
