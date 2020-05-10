class Node(object):

    def __init__(self, name):

        self.name = name
        self.visited = False
        self.adjacencyList = []

class DepthFirstSearch(object):

    def dfs(self, node):

        node.visited = True
        print(node.name)

        for i in node.adjacencyList:
            if not i.visited:
                self.dfs(i)

test1 = Node("a")
test2 = Node("b")
test3 = Node("c")
test4 = Node("d")
test5 = Node("e")
test6 = Node("f")

test1.adjacencyList.append(test2)
test1.adjacencyList.append(test3)
test2.adjacencyList.append(test4)
test4.adjacencyList.append(test5)
test3.adjacencyList.append(test6)

test = DepthFirstSearch()
test.dfs(test1)