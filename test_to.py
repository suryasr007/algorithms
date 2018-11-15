from TopologicalOrdering import * 


to = TopologicalOrdering()
graph = list()

VERTEX0 = Vertex("0")
VERTEX1 = Vertex("1")
VERTEX2 = Vertex("2")
VERTEX3 = Vertex("3")
VERTEX4 = Vertex("4")
VERTEX5 = Vertex("5")

VERTEX2.neighbour_list.append(VERTEX3)
VERTEX3.neighbour_list.append(VERTEX1)
VERTEX4.neighbour_list.append(VERTEX0)
VERTEX4.neighbour_list.append(VERTEX1)
VERTEX5.neighbour_list.append(VERTEX0)
VERTEX5.neighbour_list.append(VERTEX2)


graph.append(VERTEX0)
graph.append(VERTEX1)
graph.append(VERTEX2)
graph.append(VERTEX3)
graph.append(VERTEX4)
graph.append(VERTEX5)

for vertex in graph:
    if not vertex.visited:
        # print(vertex.visited)
        to.dfs(vertex)

for v in to.vertices:
    print(v)