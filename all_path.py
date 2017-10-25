class Graph:
    def __init__(self, node_count):
        self.data = [[] for x in range(node_count)]

    def add_edge(self, n_from, n_to):
        self.data[n_from].append(n_to)
        #self.data[n_from].append(n_to)


def DFS(G, root, dest, path):
    path.append(root)
    if root == dest:
        print(path)
        path.pop()
    else:
        for n in G.data[root]:
            if n not in path:
                DFS(G, n, dest, path)


#DAG = no reverse adges
G = Graph(4)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(0, 3)
G.add_edge(2, 3)
G.add_edge(1, 3)

path = []
DFS(G, 0, 3, path)




