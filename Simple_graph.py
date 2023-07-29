class Graph:
    def __init__(self):
       self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []


    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)



    def print_graph(self):
        return self.graph



# Example usage:
if __name__ == "__main__":
    graph = Graph()

    # Adding vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Adding edges
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    graph.add_edge("D", "A")

    # Printing the graph
    print(graph.print_graph())
