class Vertex(object):
    """
    Vertex object has data, visited and neighbour list
    """
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.neighbour_list = list()

    def __str__(self):
        return str(self.data)

class TopologicalOrdering(object):
    def __init__(self):
        self.vertices = list()
    
    def dfs(self, vertex):
        vertex.visited = True

        for v in vertex.neighbour_list:
            if not v.visited:
                self.dfs(v)
        self.vertices.append(vertex)
