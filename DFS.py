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


class DFS(object):
    def __init__(self):
        self.vertices = list()

    def dfs(self, vertex_list):
        for vertex in vertex_list:
            if not vertex.visited:
                # print(vertex)
                vertex.visited = True
                self.dfs_recursive(vertex)

    def dfs_recursive(self, vertex):
        print(vertex)

        for v in vertex.neighbour_list:
            # print(v)
            if not v.visited:
                v.visited = True
                self.dfs_recursive(v)

    # def dfs_stack(self, root_vertex):
    #     # print(root_vertex)
    #     self.vertices.append(root_vertex)
    #     root_vertex.visited = True

    #     while not len(self.vertices):
    #         vertex = self.vertices.pop()
    #         print(vertex)

    #         for v in vertex.neighbour_list:
    #             if not v.visited:
    #                 v.visited = True
    #                 self.vertices.append(v)