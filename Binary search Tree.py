class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, cur_node):

        if data < cur_node.data:
            if cur_node.leftChild is None:
                cur_node.leftChild = Node(data)
            else:
                self.insertNode(data, cur_node.leftChild)
        else:
            if cur_node.rightChild is None:
                cur_node.rightChild = Node(data)
            else:
                self.insertNode(data, cur_node.rightChild)


#                                   ----->VERY VERY IMPORTANT PART<----------


    def getminvalue(self):

        if self.root:                        #If root node is not empty
            return self.getmin(self.root)


    def getmin(self, cur_node):

        if cur_node.leftChild:               #Till cur_node.leftchild is not none, search recurssively
            return self.getmin(cur_node.leftChild)
                                            #Ultimately return the node value
        return cur_node.data


    def getmaxvalue(self):

        if self.root:                         #If root node is not empty
            return self.getmax(self.root)

    def getmax(self, cur_node):

        if cur_node.rightChild:               #Till cur_node.rightchild is not none, search recurssively
            return self.getmax(cur_node.rightChild)
                                              # Ultimately return the node value
        return cur_node.data

    def deleteNode(self, data):

        if self.root:
            self.root = self.Deletion(self.root, data)

    def Deletion(self, cur_node, data):

        if not cur_node:
            return cur_node

        if data > cur_node.data:
            cur_node.rightChild = self.Deletion(cur_node.rightChild, data)

        elif data < cur_node.data:
            cur_node.leftChild = self.Deletion(cur_node.leftChild, data)


        else:

            if not cur_node.leftChild and not cur_node.rightChild:

                print("leaf node is deleted")
                del cur_node
                return None

            elif not cur_node.rightChild:

                temp = cur_node.leftChild
                print("Deleting Node with single left child")
                del cur_node
                return temp

            elif not cur_node.leftChild:

                temp = cur_node.rightChild
                print("deleting node with single right child")
                del cur_node
                return temp



            print("Deleting node with two children")
            temp = self.getPredecessor(cur_node.leftChild)
            cur_node.data = temp.data
            cur_node.leftChild = self.Deletion(cur_node.leftChild, temp.data)

        return cur_node

    def getPredecessor(self, cur_Node):

        if cur_Node.rightChild:
            return self.getPredecessor(cur_Node.rightChild);

        return cur_Node;

    def traverseIn(self):
        if self.root:
            self.inordertraverse(self.root)

    def inordertraverse(self, cur_node):

        if cur_node.leftChild:
             self.inordertraverse(cur_node.leftChild)
        print(cur_node.data, end=" ")

        if cur_node.rightChild:
             self.inordertraverse(cur_node.rightChild)

    def traversePre(self):

        if self.root:
            self.PreOrderTraverse(self.root)

    def PreOrderTraverse(self, cur_Node):

        print(cur_Node.data, end=" ")

        if cur_Node.leftChild:
            self.PreOrderTraverse(cur_Node.leftChild)
        if cur_Node.rightChild:
            self.PreOrderTraverse(cur_Node.rightChild)

    def traversePost(self):

        if self.root:
            self.PostOrderTraverse(self.root)

    def PostOrderTraverse(self, cur_Node):

        if cur_Node.leftChild:
            self.PreOrderTraverse(cur_Node.leftChild)

        if cur_Node.rightChild:
            self.PostOrderTraverse(cur_Node.rightChild)

        print(cur_Node.data, end=" ")



bst = BinarySearchTree()

bst.insert(20)
bst.insert(55)
bst.insert(100)
bst.insert(1)
bst.insert(11)
bst.insert(790)
bst.traverseIn()
print("\n")
#bst.deleteNode(20)
#bst.deleteNode(1)
bst.traversePre()
print("\n")
bst.traversePost()

