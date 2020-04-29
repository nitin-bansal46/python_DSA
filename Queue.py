# Making Queue abstract Data  type
# It follows FIFO structure
# IT can be made with dyanamic Arrays or linked list
class Queue():

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        data = self.queue[0]
        return data

    def queueSize(self):
        return len(self.queue)

Myqueue = Queue()

Myqueue.enQueue(10)
Myqueue.enQueue(20)
Myqueue.enQueue(30)

print(Myqueue.queueSize())

Myqueue.deQueue()

print(Myqueue.queueSize())
