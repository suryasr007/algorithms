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

