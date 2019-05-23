
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.parent = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connected to ' +\
                str([x.id for x in self.connectedTo])

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

wordFile = "word.txt"
def buildGraph(wordFile):
    d = {}
    g = Graph() 
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

graph = buildGraph(wordFile)

start = graph.getVertex('fool')
end = graph.getVertex('sage')
def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in (vertex.connectedTo.keys()) - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, end):
    try:
        return next(bfs(graph, start, end))
    except StopIteration:
        return None

lis = shortest_path(graph, start, end)
for l in lis:
    print (l.id)