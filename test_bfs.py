from BFS import *

# Defining vertexes
VERTEX1 = Vertex(1)
VERTEX2 = Vertex(2)
VERTEX3 = Vertex(3)
VERTEX4 = Vertex(4)
VERTEX5 = Vertex(5)

# Defining Neighbours for those vertexes
VERTEX1.neighbour_list.append(VERTEX2)
VERTEX1.neighbour_list.append(VERTEX4)
VERTEX4.neighbour_list.append(VERTEX5)
VERTEX2.neighbour_list.append(VERTEX3)

bfs(VERTEX4)
