# Code from https://github.com/minsuk-heo/problemsolving/blob/master/graph/bfs.py

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current = queue.pop()

        # visit the adjacents of the current
        for neighbor in adjacencyList[current]:
            if neighbor not in visitedVertex:
                queue.insert(0, neighbor)

        # After visiting the popped node,
        # insert that node into the visitedVertex list
        visitedVertex.append(current)

    return visitedVertex



# Unit Test
vertexList = [0, 1, 2, 3, 4, 5, 6]
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
graphs = (vertexList, edgeList)

print(bfs(graphs, vertexList[0]))
