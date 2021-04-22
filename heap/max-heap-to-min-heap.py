class HeapTransformer:
    
    def __init__(self, heap):
        self.heap = heap

    def transform(self):

        for i in range((len(self.heap)-2)//2, -1, -1):
            self.fix_down(i)

    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # in a heap the parent is always greater than the parent
        index_largest = index

        # looking for the min (parnet or left node)
        if index_left < len(self.heap) and self.heap[index_left] < self.heap[index]:
            index_largest = index_left

        # if the right child is smaller than the left child: min is the right child
        if index_right < len(self.heap) and self.heap[index_right] < self.heap[index_largest]:
            index_largest = index_right

        # if the parent is larger than the children: it is a valid heap so we terminate the
        # recursive function calls
        if index != index_largest:
            self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
            self.fix_down(index_largest)

if __name__ == "__main__":
    
    n = [210, 100, 23, 2, 5]
    heap_transform = HeapTransformer(n)
    heap_transform.transform()
    print(heap_transform.heap)