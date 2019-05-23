#!/bin/python3

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedTo = set()
        self.distance = 0
        self.parent = None
        self.color = 'white'

    def addNeighbor(self, nbr):
        if nbr not in self.connectedTo:
            self.connectedTo.add(nbr)
        if self not in nbr.connectedTo:
            nbr.connectedTo.add(self)

    def __repr__(self):
        return str(self.key)

class Graph:
    def __init__(self):
        self.vertList = {}
    
    def addVertex(self, key):
        if key not in self.vertList:
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
    
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        return None

    def update(self, node, edge_list):
        for i in range(node):
            self.addVertex(i + 1)
        for edge in edge_list:
            self.vertList[edge[0]].addNeighbor(self.vertList[edge[1]])

    def reset(self):
        for vert in self:
            vert.color = 'white'
            vert.parent = None
            vert.distance = 0

    def __iter__(self):
        return iter(self.vertList.values())


def shortest_path(graph, start, end):
    queue = [start]
    while queue:
        curr_vert = queue.pop(0)
        if curr_vert == end:
            ct = curr_vert.distance * 6
            graph.reset()
            return ct
        for nbr in curr_vert.connectedTo:
            if nbr.color == 'white':
                nbr.color = 'gray'
                nbr.parent = curr_vert
                nbr.distance = curr_vert.distance + 1
                queue.append(nbr)
        curr_vert.color = 'black'
    graph.reset()    
    return -1

def bfs(n, m, edges, s):
    graph = Graph()
    lis = []
    graph.update(n, edges)
    start = graph.getVertex(s)
    for i in range(1, n + 1):
        if i != s:
            end = graph.getVertex(i)
            lis.append(shortest_path(graph, start, end))
    return lis

if __name__ == '__main__':
    read = open('BFS_shortest_path_test_2.txt', 'r')
    number_test = 0
    start = 1
    edges = []
    m = 0
    n = 0
    s = 0
    # check_list = [[6, 6, -1], [-1, 6], [6, 6, 12, -1], [6, 12, 18, 6], [6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]]
    result_list = []
    check_list = [int(x) for x in "6 6 6 6 12 6 12 6 12 12 6 6 6 6 6 12 12 6 6 6 6 12 6 12 6 12 6 12 12 12 12 6 12 12 6 12 12 6 12 6 12 6 12 12 6 6 12 6 6 6 6 12 12 12 12 6 6 6 12 6 6 12 12 12 12 12 12 6 6".split()]
    for line in read:
        temp = line.split()
        if len(temp) == 1:
            s = int(temp[0])
            result = bfs(n, m, edges, s)
            result_list.append(result)
            n = 0
            m = 0
            edges = []
            s = 0
            start = 1
        elif start:
            n = int(temp[0])
            m = int(temp[1])
            start = 0
        else:
            edges.append([int(temp[0]), int(temp[1])])
    read.close()
    print(check_list)
    print(result_list[0])
    print(result == result_list[0])
            