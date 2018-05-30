import queue

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

def bfs(root):
    """
    Functionality
    load the root
    While the queue is not empty
    for each element extract its children and load them into queue and mark them as visited.

    """
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current_vertex = q.get()
        print(current_vertex)

        for vertex in current_vertex.neighbour_list:
            if not vertex.visited:
                 vertex.visited = True
                 q.put(vertex)
