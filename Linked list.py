class Node():

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.size = 0
        self.size1 = self.size

    def insertStart(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        cur_Node = self.head
        while cur_Node.nextNode != None:
            cur_Node = cur_Node.nextNode

        cur_Node.nextNode = newNode

    def size(self):
        return self.size()

    def traverseList(self):
        cur_Node = self.head
        while cur_Node is not None:
            print(" ---> ", cur_Node.data, end = "")
            cur_Node = cur_Node.nextNode

    def middleTerm(self):
        i = 0
        mid_Node = self.head
        if (self.size % 2 == 0):
            for i in range(((self.size//2))):
                mid_Node = mid_Node.nextNode
            print("Even is executed ", mid_Node.data)
        else:
            for i in range((self.size)//2):
                mid_Node = mid_Node.nextNode
            print("odd is executed ",mid_Node.data)




mylist = LinkedList()
mylist.insertStart(5)
mylist.insertStart(2)
mylist.insertStart(3)
mylist.insertStart(4)
mylist.insertEnd(0)
mylist.insertEnd(-1)
mylist.insertEnd(10)
print(mylist.size)
mylist.traverseList()
print("\n")
mylist.middleTerm()
