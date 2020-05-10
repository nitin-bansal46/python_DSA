class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacencyList = []


class BreadthFirstSearch(object):

    def bfs(self, start_node):

        queue = []

        queue.append(start_node)
        start_node.visited = True

        while queue:

            actual_node = queue.pop(0)
            print(actual_node.name)

            for i in actual_node.adjacencyList:
                if not i.visited:
                    i.visited = True
                    queue.append(i)


test1 = Node("a")
test2 = Node("b")
test3 = Node("c")
test4 = Node("d")
test5 = Node("e")
test6 = Node("f")

test1.adjacencyList.append(test2)
test1.adjacencyList.append(test3)
test2.adjacencyList.append(test4)
test3.adjacencyList.append(test5)
test4.adjacencyList.append(test6)

test = BreadthFirstSearch()
test.bfs(test1)