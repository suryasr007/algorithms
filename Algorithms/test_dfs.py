from DFS import *

# Defining vertexes
VERTEX1 = Vertex(1)
VERTEX2 = Vertex(2)
VERTEX3 = Vertex(3)
VERTEX4 = Vertex(4)
VERTEX5 = Vertex(5)

# Defining Neighbours for those vertexes
VERTEX1.neighbour_list.append(VERTEX2)
VERTEX1.neighbour_list.append(VERTEX3)
VERTEX3.neighbour_list.append(VERTEX4)
VERTEX4.neighbour_list.append(VERTEX5)

vertex_list = list()

vertex_list.append(VERTEX1)
vertex_list.append(VERTEX2)
vertex_list.append(VERTEX3)
vertex_list.append(VERTEX4)
vertex_list.append(VERTEX5)

dfs = DFS()
dfs.dfs(vertex_list)