# for graph which we are making
class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.node = None

class Edge(object):
    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

    def __cmp__(self, othervertex):
        return self.cmp(self.weight, othervertex.weight)

    def __lt__(self, other):
        selfpriority = self.weight
        otherpriority = other.weight
        return selfpriority < otherpriority
# for disjoint set
class Node(object):

    def __init__(self, height, nodeid, parent):
        self.nodeid = nodeid
        self.parent = parent
        self.height = height

class Disjointset(object):

    def __init__(self, vertexlist):
        self.vertexlist = vertexlist  # Contains all the nodes/vertices present in the graph
        self.rootNode = []            # this list keep track of root nodes in the disjoint set
        self.setcount = 0             # initially set count will be zero
        self.nodecount = 0            # ''        node count will be zero
        self.makesets(vertexlist)     # here we are creating disjoint set with all the vertex present in the graph

    def makesets(self, vertexlist):   # to make disjoint set nodes
        for v in vertexlist:          # for every vertex in the graph there is one
            self.makeset(v)           # set in disjoint set initially

    def makeset(self, vertex):
        node = Node(0, len(self.rootNode), None)
        vertex.node = node
        self.rootNode.append(node)
        self.setcount = self.setcount + 1
        self.nodecount = self.nodecount + 1


    def find(self, node):    # here we are finding the node in the disjoint set

        currentnode = node

        while currentnode.parent != None:
            currentnode = currentnode.parent

        root = currentnode

        # for path compression
        currentnode = node

        while currentnode != root:
            temp = currentnode.parent
            currentnode.parent = root
            currentnode = temp

        return root.nodeid

    def merge(self, node1, node2):

        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

        root1 = self.rootNode[index1]
        root2 = self.rootNode[index2]

        if root1.height < root2.height:
            root1.parent = root2
        elif root2.height < root1.height:
            root2.parent = root1
        else:
            root2.parent = root1
            root1.height = root1.height + 1

class Kruskalalgorithm(object):

    def spanningtree(self, vertexlist, edgelist):

        disjointset = Disjointset(vertexlist)
        spanningtree = []

        edgelist.sort()

        for edge in edgelist:
            u = edge.startvertex
            v = edge.targetvertex


            if disjointset.find(u.node) is not disjointset.find(v.node):
                spanningtree.append(edge)
                disjointset.merge(u.node, v.node)

        for edge in spanningtree:
            print(edge.startvertex.name, "---", edge.targetvertex.name, edge.weight)


vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)
vertexList.append(vertex7)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)
edgeList.append(edge11)

algorithm = Kruskalalgorithm()
algorithm.spanningtree(vertexList, edgeList)








