#!/bin/python3

class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = 'white'
        self.parent = None
        self.distance = 0
        self.connectedTo = {}
        self.weight = 0

    def add_neighbor(self, nbr, weight):
        self.connectedTo[nbr] = weight
        nbr.connectedTo[self] = weight

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.key)
        # return str(self.key) + ' connected to ' +\
        #         str([x.key for x in self.connectedTo.keys()])

class Graph:
    def __init__(self):
        self.vert_list = {}

    def get_vertex(self, key):
        return self.vert_list[key]

    def update(self, node, edge_list):
        for key in range(node):
            vertex = Vertex(key + 1)
            self.vert_list[key + 1] = vertex
        for edge in edge_list:
            self.vert_list[edge[0]].add_neighbor(self.vert_list[edge[1]], 2 ** edge[2])

    def __iter__(self):
        return iter(self.vert_list.values())

def dfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        connections = set(vertex.connectedTo.keys())
        for next in (connections - set(path)):
            if next == end:
                yield (path + [next])
            else:
                queue.append((next, path + [next]))

def min_distance(graph, start, end):
    lis = list(dfs(graph, start, end))
    cost = -1
    temp = 0
    for route in lis: 
        for i in range(0, len(route) - 1):
            temp += route[i].get_weight(route[i + 1])
        if cost < 0 or cost > temp:
            cost = temp
    return cost


def roadsInHackerland(n, roads):
    graph = Graph()
    graph.update(n, roads)
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            start = graph.get_vertex(i)
            end = graph.get_vertex(j)
            count += min_distance(graph, start, end)
    return bin(count)

if __name__ == '__main__':
    read = open('road_in_hackerland_test.txt', 'r')
    number_test = 0
    start = 1
    roads = []
    n = 0
    result_list = []
    for line in read:
        temp = line.split()
        if len(temp) == 2:
            n = int(temp[0])
        elif len(temp) > 2:
            roads.append([int(temp[0]), int(temp[1]), int(temp[2])])
    read.close()
    ret = roadsInHackerland(n, roads)