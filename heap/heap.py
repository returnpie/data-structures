
CAPACITY = 10

# maximum heap (root node will be the largest item)


class Heap:

    def __init__(self):
        # this is the actual number of items in the data structure
        self.heap_size = 0
        # the underlying list data structure
        self.heap = [0] * CAPACITY

    def insert(self, item):

        # when the heap is full
        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap properties
        self.fix_up(self.heap_size - 1)

    # starting with the actual node we have inserted up to root node
    # we have to compare the values whether to make swap operations
    # logN it has O(logN) running time complexity
    def fix_up(self, index):

        parent_index = (index-1)//2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    # peek return with the max item in O(1)
    def get_max(self):
        return self.heap[0]

    # return the max and removes it as well
    # return the root node of the heap
    def poll(self):

        max_item = self.get_max()

        # swap the root node with the last item and "heapify"
        self.heap[0], self.heap[self.heap_size -
                                1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1

        # make sure the heap is "heapify"
        self.fix_down(0)

        return max_item

    # starting with the root node downwards until the heap properties are no longer
    def fix_down(self, index):

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # in a max heap the parent is always greater than the children
        largest_index = index

        # looking for the largest (parent or left node)
        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        # if the right child is greater than the left child: largest is the right child
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):

        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


if __name__ == "__main__":

    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(4)
    heap.insert(21)
    heap.insert(16)

    heap.heap_sort()

    # print(heap.heap)
