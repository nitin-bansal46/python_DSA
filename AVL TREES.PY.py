class Node(object):

    def __init__(self, data):   # Making constructor
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.Height = 0

class AVL(object):

    def __init__(self):                     # Initializing root node as null/none
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, cur_node):

        if cur_node is None:
            return Node(data)

        if data < cur_node.data:
            cur_node.leftChild = self.insertNode(data, cur_node.leftChild)
        else:
            cur_node.rightChild = self.insertNode(data, cur_node.rightChild)

        cur_node.Height = max(self.Calc_Height(cur_node.rightChild),self.Calc_Height(cur_node.leftChild)) + 1

        return self.violation(data, cur_node)

    def violation(self, data, cur_node):

        balance = self.Balance_Factor(cur_node)

        if balance > 1 and data < cur_node.leftChild.data:

            print("LL case: Doing right rotation ")
            return self.rightRotation(cur_node)

        if balance > 1 and data > cur_node.leftChild.data:

            print("LR case : Doing left-->right rotations")
            cur_node.leftChild = self.leftRotation(cur_node.leftChild)
            return self.rightRotation(cur_node)

        if balance < -1 and data > cur_node.rightChild.data:

            print("RR case : Doing right rotations ")
            return self.leftRotation(cur_node)

        if balance < -1 and data < cur_node.rightChild.data:
            print("RL case : Doing Right-->Left rotations ")
            cur_node.rightChild = self.rightRotation(cur_node.rightChild)
            return self.leftRotation(cur_node)

        return cur_node

    def Calc_Height(self, cur_Node):        # function for calculating height

        if cur_Node is None:               # Base case if root is null return -1
            return -1

        return cur_Node.Height

    def Balance_Factor(self, Cur_Node):      # function for calc. Balance factor which should
                                             # be atmost 1
        if not Cur_Node:
            return 0
        else:
            return self.Calc_Height(Cur_Node.leftChild) - self.Calc_Height(Cur_Node.rightChild)

    def rightRotation(self, cur_node):

        print("Right rotation on --> ", cur_node.data)

        temp_Node_1 = cur_node.leftChild
        temp_Node_2 = temp_Node_1.rightChild

        cur_node.leftChild = temp_Node_2
        temp_Node_1.rightChild = cur_node

        cur_node.Height = max(self.Calc_Height(cur_node.leftChild), self.Calc_Height(cur_node.rightChild)) + 1
        temp_Node_1.Height = max(self.Calc_Height(temp_Node_1.leftChild), self.Calc_Height(temp_Node_1.rightChild)) + 1

        return temp_Node_1

    def leftRotation(self, cur_node):

        print("Left rotation on --> ", cur_node.data)

        temp_Node_1 = cur_node.rightChild
        temp_Node_2 = temp_Node_1.leftChild

        cur_node.rightChild = temp_Node_2
        temp_Node_1.leftChild = cur_node

        cur_node.Height = max(self.Calc_Height(cur_node.leftChild), self.Calc_Height(cur_node.rightChild)) + 1
        temp_Node_1.Height = max(self.Calc_Height(temp_Node_1.leftChild), self.Calc_Height(temp_Node_1.rightChild)) + 1

        return temp_Node_1

    def traverseIn(self):

        if self.root:
            self.inorderTraverse(self.root)

    def inorderTraverse(self, cur_node):

        if cur_node.leftChild:
            self.inorderTraverse(cur_node.leftChild)

        print(cur_node.data, end=" ")

        if cur_node.rightChild:
            self.inorderTraverse(cur_node.rightChild)

    def delete(self, data):
        if self.root:
            self.delete_node(self.root, data)

    def delete_node(self, cur_node, data):

        if cur_node is None:
            return None

        if data < cur_node.data:
            cur_node.leftChild = self.delete_node(cur_node.leftChild, data)
        if data > cur_node.data:
            cur_node.rightChild = self.delete_node(cur_node.rightChild, data)
        else:
            if not cur_node.rightChild and cur_node.leftChild:
                print("\ndeleting node with no child ")
                del cur_node
                return None

            elif cur_node.rightChild is None:
                print("\nDeleting node with leftchild ")
                tempnode = cur_node.leftChild
                del cur_node
                return tempnode
            elif cur_node.leftChild is None:
                print("\nDeleting node with rightchild")
                tempnode = cur_node.rightChild
                del cur_node
                return tempnode

            print("\nDeleting node with both child ")
            temp_1 = self.getpredesessor(cur_node.leftChild)
            cur_node.data = temp_1
            cur_node.leftChild = self.delete_node(cur_node.leftChild, temp_1)

        if not cur_node:
            return cur_node

        cur_node.Height = max(self.Calc_Height(cur_node.leftChild), self.Calc_Height(cur_node.rightChild)) + 1

        balance = self.Balance_Factor(cur_node)

        if balance > 1 and self.Balance_Factor(cur_node.leftChild) >= 0:
            return self.rightRotation(cur_node)

        if balance > 1 and self.Balance_Factor(cur_node.rightChild) > 0:
            cur_node.leftChild = self.leftRotation(cur_node.leftChild)

        if balance < -1 and self.Balance_Factor(cur_node.rightChild) >=0:
             return self.leftRotation(cur_node)

        if balance < -1 and self.Balance_Factor(cur_node.leftChild) > 0:
            cur_node.rightChild = self.rightRotation(cur_node.rightChild)
            return self.leftRotation(cur_node)

        return cur_node

    def getpredesessor(self, cur_node):
        if cur_node.rightChild:
            return self.getpredesessor(cur_node.rightChild)
        return cur_node.data











myavl = AVL()
myavl.insert(10)
myavl.insert(20)
myavl.insert(5)
myavl.insert(6)
myavl.insert(15)
myavl.insert(0)
myavl.insert(-1)
myavl.insert(-2)

myavl.traverseIn()

myavl.delete(10)
print("\n")
myavl.traverseIn()