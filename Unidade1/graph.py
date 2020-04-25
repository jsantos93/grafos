class Graph:
    
    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertice(self, vertice):
        if vertice not in self.__graph_dict:
            self.__graph_dict[vertice] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertice in self.__graph_dict:
            for neibour in self.__graph_dict[vertice]:
                if {neibour, vertice} not in edges:
                    edges.append({vertice, neibour})
        return edges

    # def opposite(self, v, e):
    #     if v in e:
    #         for vertice in e:
    #             if vertice != v:
    #                 target = vertice
    #         for edge in self.__graph_dict[v]:
    #             print(edge)
    #             if edge == target:
    #                 print("oi")
    #                 return target
    #             else:
    #                 return print("Error f")
    #     else:
    #         return print("Error")

    def incidentEdges(self, vertice):
        if vertice in self.__graph_dict:
            return self.__graph_dict[vertice]

    def areAdajacent(self, v, w):
        if v in self.__graph_dict and w in self.__graph_dict:
            if w in self.__graph_dict[v]:
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertice("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    print("Incident Edges")
    print(graph.incidentEdges("c"))

    print("Are Adjacents?")
    print(graph.areAdajacent("c", 'b'))

    # print("Opposite")
    # print(graph.opposite("c", {"c", "f"}))