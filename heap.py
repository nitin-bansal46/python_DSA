capacity = 10
class Heap(object):

    def __init__(self):
        self.heap = [0]*capacity
        self.cur_position = 0

    def insert(self, item):

        if capacity == self.cur_position:
            return

        self.heap[self.cur_position] = item
        self.cur_position += 1
        self.fix_up(self.cur_position - 1)

    def fix_up(self, index):

        parent_index = int((index - 1)//2)

        while parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp
            index = parent_index
            parent_index = int((index-1)//2)

    def get_max(self):
        print(self.heap[0])


    def heap_sort(self):

        for i in range(0, self.cur_position):
            temp = self.heap[0]
            print(temp, "-->", end=" ")
            self.heap[0] = self.heap[self.cur_position - i-1]
            self.heap[self.cur_position - i-1] = temp
            self.fix_down(0, self.cur_position - i - 2)

    def fix_down(self, i, till):

        while i <= till:

            left_index = 2*i + 1
            right_index = 2*i + 2

            if left_index < till:
                swap = None

                if right_index > till:

                    swap = left_index

                else:
                    if self.heap[left_index] > self.heap[right_index]:
                        swap = left_index

                    else:
                        swap = right_index
                if self.heap[i] < self.heap[swap]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[swap]
                    self.heap[swap] = temp
                else:
                    break
                i = swap
            else:
                break


    def print_heap(self):
        for i in self.heap:
            print(i, "-->", end=" ")

heap = Heap()
heap.insert(20)
heap.insert(50)
heap.insert(1)
heap.insert(200)
heap.insert(5)
heap.insert(55)
heap.insert(-2)
heap.insert(30)
heap.insert(10)
heap.insert(40)

#heap.get_max()
heap.heap_sort()
#heap.print_heap()

