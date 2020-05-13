import sys
import heapq

class Edge(object):

    def __init__(self, weight, start_vertex, target_vertex):
        self.target_vertex = target_vertex
        self.start_vertex = start_vertex
        self.weight = weight

class Node(object):

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.visited = False
        self.adjacent_node = []
        self.min_distance = sys.maxsize

    # this function will decide what will be compared
    # for going to heap, some value must be needed so that heap can be formed
    def __cmp__(self, other_vertex):
        return self.cmp(self.min_distance, other_vertex.min_distance)

    # Now how we will decide which node is greator or smaller,
    # on what basis ---> min_distance
    def __lt__(self, other):

        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority

class ShortestPathAlgorithm(object):

    def calc_shortest_path(self, target_vertex_list, start_vertex):

        q = []
        start_vertex.min_distance = 0
        heapq.heappush(q, start_vertex)

        while q:
            actual_vertex = heapq.heappop(q)

            for edge in actual_vertex.adjacent_node:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    v.parent = u
                    heapq.heappush(q, v)

    def getshortestpath(self, target_node):


        print("Minimum distance is --> ", target_node.min_distance)
        print("And shortest path will be ")
        node = target_node

        while node:
            print(node.name, "<--", end=" ")
            node = node.parent



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

node1.adjacent_node.append(edge1)
node1.adjacent_node.append(edge2)
node1.adjacent_node.append(edge3)
node2.adjacent_node.append(edge4)
node2.adjacent_node.append(edge5)
node2.adjacent_node.append(edge6)
node8.adjacent_node.append(edge7)
node8.adjacent_node.append(edge8)
node5.adjacent_node.append(edge9)
node5.adjacent_node.append(edge10)
node5.adjacent_node.append(edge11)
node6.adjacent_node.append(edge12)
node6.adjacent_node.append(edge13)
node3.adjacent_node.append(edge14)
node3.adjacent_node.append(edge15)
node4.adjacent_node.append(edge16)


vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)

algorithm = ShortestPathAlgorithm()
algorithm.calc_shortest_path(vertexList, node1)
algorithm.getshortestpath(node7)


