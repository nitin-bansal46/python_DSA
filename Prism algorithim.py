import heapq

class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacencyList = []

class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

    def __lt__(self, otherEdge):
        selfPriority = self.weight
        otherEdgePriority = otherEdge.weight
        return selfPriority < otherEdgePriority

class PrimsJarnik(object):

    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.edgeHeap = []
        self.fullCost = 0
        self.spanningTree = []

    def calspanningtree(self, vertex):

        self.unvisitedList.remove(vertex)

        while self.unvisitedList:

            for edge in vertex.adjacencyList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge)

            minEdge = heapq.heappop(self.edgeHeap)

            if minEdge.targetVertex in self.unvisitedList:
                self.spanningTree.append(minEdge)
                print(minEdge.startVertex.name, "-->", minEdge.targetVertex.name)
                self.fullCost += minEdge.weight
                vertex = minEdge.targetVertex
                self.unvisitedList.remove(vertex)

 

    def getcost(self):
        return self.fullCost



# Driver code

vertexA = Vertex("A")
vertexB = Vertex("B")
vertexC = Vertex("C")
vertexD = Vertex("D")
vertexE = Vertex("E")
vertexF = Vertex("F")
vertexG = Vertex("G")

edgeAB = Edge(2, vertexA, vertexB)
edgeBA = Edge(2, vertexB, vertexA)
edgeAE = Edge(5, vertexA, vertexE)
edgeEA = Edge(5, vertexE, vertexA)
edgeAC = Edge(6, vertexA, vertexC)
edgeCA = Edge(6, vertexC, vertexA)
edgeAF = Edge(10, vertexA, vertexF)
edgeFA = Edge(10, vertexF, vertexA)
edgeBE = Edge(3, vertexB, vertexE)
edgeEB = Edge(3, vertexE, vertexB)
edgeBD = Edge(3, vertexB, vertexD)
edgeDB = Edge(3, vertexD, vertexB)
edgeCD = Edge(1, vertexC, vertexD)
edgeDC = Edge(1, vertexD, vertexC)
edgeCF = Edge(2, vertexC, vertexF)
edgeFC = Edge(2, vertexF, vertexC)
edgeDE = Edge(4, vertexD, vertexE)
edgeED = Edge(4, vertexE, vertexD)
edgeDG = Edge(5, vertexD, vertexG)
edgeGD = Edge(5, vertexG, vertexD)
edgeFG = Edge(3, vertexF, vertexG)
edgeGF = Edge(3, vertexG, vertexF)

unvisitedList = []
unvisitedList.append(vertexA)
unvisitedList.append(vertexB)
unvisitedList.append(vertexC)
unvisitedList.append(vertexD)
unvisitedList.append(vertexE)
unvisitedList.append(vertexF)
unvisitedList.append(vertexG)

vertexA.adjacencyList.append(edgeAB)
vertexA.adjacencyList.append(edgeAC)
vertexA.adjacencyList.append(edgeAE)
vertexA.adjacencyList.append(edgeAF)
vertexB.adjacencyList.append(edgeBA)
vertexB.adjacencyList.append(edgeBD)
vertexB.adjacencyList.append(edgeBE)
vertexC.adjacencyList.append(edgeCA)
vertexC.adjacencyList.append(edgeCD)
vertexC.adjacencyList.append(edgeCF)
vertexD.adjacencyList.append(edgeDB)
vertexD.adjacencyList.append(edgeDC)
vertexD.adjacencyList.append(edgeDE)
vertexD.adjacencyList.append(edgeDG)
vertexE.adjacencyList.append(edgeEA)
vertexE.adjacencyList.append(edgeEB)
vertexE.adjacencyList.append(edgeED)
vertexF.adjacencyList.append(edgeFA)
vertexF.adjacencyList.append(edgeFC)
vertexF.adjacencyList.append(edgeFG)
vertexG.adjacencyList.append(edgeGD)
vertexG.adjacencyList.append(edgeGF)

algorithm = PrimsJarnik(unvisitedList)
algorithm.calspanningtree(vertexD)
print(algorithm.getcost())
