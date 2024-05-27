class Vertex:
    def __init__(self):
        self.edges = {}

    def add_edge(self, vertex):
        # vertex buffer
        if vertex in self.edges:
            self.edges[vertex] += 1
        else:
            self.edges[vertex] = 1


class Graph:
    def __init__(self, num_vertices):
        self.vertices = {i: Vertex() for i in range(num_vertices)}

    def add_edge(self, start, end):
        self.vertices[start].add_edge(end)
        self.vertices[end].add_edge(start)


n, m = map(int, input().split())
graph = Graph(n)

for i in range(m):
    start, end = map(int, input().split())
    graph.add_edge(start, end)

for vertex, data in graph.vertices.items():
    line = [0]*n
    for connected_vertex, weight in data.edges.items():
        line[vertex] += weight
        line[connected_vertex] -= weight
    print(*line)
