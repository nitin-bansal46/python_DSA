import sys

class Node(object):

    def __init__(self, name):
        self.name = name
        self.mindistance = sys.maxsize
        self.adjacentnodes = []
        self.parent = None

class Edge(object):

    def __init__(self, weight, startnode, endnode):
        self.weight = weight
        self.startnode = startnode
        self.endnode = endnode

class bellmanford(object):

    Has_Visited = False

    def calshortestpath(self, vertexlist, edgelist, startnode):

        startnode.mindistance = 0
        for i in range(len(vertexlist)-1):
            for edge in edgelist:
                u = edge.startnode
                v = edge.endnode
                newdistance = u.mindistance + edge.weight
                if newdistance <v.mindistance:
                    v.mindistance = newdistance
                    v.parent = u

        for edge in edgelist:
            if self.hasvisited(edge):
                print("!!! NEGATIVE CYCLE DETECTED !!!")
                bellmanford.Has_Visited = True
                return


    def hasvisited(self,edge):
        if edge.startnode.mindistance + edge.weight < edge.endnode.mindistance:
                return True
        else:
            return False


    def getshortestpath(self, endnode):

        if not bellmanford.Has_Visited:
            print("Shortest distance is = ", endnode.mindistance)

            node = endnode
            while node:

                print(node.name)
                node = node.parent

        else:
            print("!!! NEGATIVE CYCLE DETECTED !!!")


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5,node1,node2)
edge2 = Edge(8,node1,node8)
edge3 = Edge(9,node1,node5)
edge4 = Edge(15,node2,node4)
edge5 = Edge(12,node2,node3)
edge6 = Edge(4,node2,node8)
edge7 = Edge(7,node8,node3)
edge8 = Edge(6,node8,node6)
edge9 = Edge(5,node5,node8)
edge10 = Edge(4,node5,node6)
edge11 = Edge(20,node5,node7)
edge12 = Edge(1,node6,node3)
edge13 = Edge(13,node6,node7)
edge14 = Edge(3,node3,node4)
edge15 = Edge(11,node3,node7)
edge16 = Edge(9,node4,node7)


node1.adjacentnodes.append(edge1)
node1.adjacentnodes.append(edge2)
node1.adjacentnodes.append(edge3)
node2.adjacentnodes.append(edge4)
node2.adjacentnodes.append(edge5)
node2.adjacentnodes.append(edge6)
node8.adjacentnodes.append(edge7)
node8.adjacentnodes.append(edge8)
node5.adjacentnodes.append(edge9)
node5.adjacentnodes.append(edge10)
node5.adjacentnodes.append(edge11)
node6.adjacentnodes.append(edge12)
node6.adjacentnodes.append(edge13)
node3.adjacentnodes.append(edge14)
node3.adjacentnodes.append(edge15)
node4.adjacentnodes.append(edge16)


vertexlist = (node1,node2,node3, node4, node5, node6, node7, node8)
edgelist = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14,edge15,edge16)

algorithm = bellmanford()
algorithm.calshortestpath(vertexlist, edgelist, node1)
algorithm.getshortestpath(node7)