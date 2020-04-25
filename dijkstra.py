class Vertex:

    def __init__(self, node):
        self.node = node
        self.adjacent = {}

    def addConection(self, node, weight = 0):
        self.adjacent[node] = weight
    
    def getConection(self):
        return self.adjacent.keys()

    def getWeight(self, node):
        return self.adjacent[node]


class Graph:

    def __init__(self):
        self.vert_dict = {}
        self.num_vert = 0

    def addNode(self, node):
        new_vert = Vertex(node)
        self.vert_dict[node] = new_vert
        self.num_vert = self.num_vert + 1
        return new_vert

    def getNode(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            None

    def addEdge(self, init, end, weight = 0):
        if init not in self.vert_dict:
            self.addNode(init)
        if end not in self.vert_dict:
            self.addNode(end)

        self.vert_dict[init].addConection(self.vert_dict[end], weight)
        self.vert_dict[end].addConection(self.vert_dict[init], weight)

    def getNodes(self):
        return self.vert_dict.keys()

if __name__ == "__main__":
    
    g = Graph()

    g.addNode('a')
    g.addNode('b')
    g.addNode('c')
    g.addNode('d')
    g.addNode('e')
    g.addNode('f')

    g.addEdge('a', 'b', 7)  
    g.addEdge('a', 'c', 9)
    g.addEdge('a', 'f', 14)
    g.addEdge('b', 'c', 10)
    g.addEdge('b', 'd', 15)
    g.addEdge('c', 'd', 11)
    g.addEdge('c', 'f', 2)
    g.addEdge('d', 'e', 6)
    g.addEdge('e', 'f', 9)

