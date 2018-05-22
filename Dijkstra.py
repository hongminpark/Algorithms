

class Graph:

    def __init__(self, graphs):
        self.distanceList = graphs

        # Making vertexList from the graph parameter
        self.vertexList = range(0, len(graphs))

        # Making edgeList from the graph parameter
        self.adjacencyList = []
        for node in graphs:
            tmp = []
            for idx, edge in enumerate(node):
                if edge is not None:
                    tmp.append(idx)
            self.adjacencyList.append(tmp)

    def minPath(self, fromVertex, toVertex):


        # set the adjacent nodes distance value as the default val


        #




if __name__ == "__main__":
    graphs = [[None, 7, 9, None, None, 14],
              [7, None, 10, 15, None, None],
              [9, 10, None, 11, None, 2],
              [None, 15, 11, None, 6, None],
              [None, None, None, 6, None, 9],
              [14, None, 2, None, 9, None]]
    graph = Graph(graphs)

