class MinHeap:

    def __init__(self, item=[]):
        self.items = item
        self.heapsize = len(self.items)

    def left(self,i):
        return 2*i + 1

    def right(self,i):
        return 2*i  + 2

    def parent(self,i):
        return (i - 1 )/2

    def min_heapfiy(self,i):
        l = self.left(i)
        r = self.right(i)

        if l < self.heapsize and self.items[l] < self.items[i]:
            smallest = l
        else:
            smallest = i

        if  r < self.heapsize and self.items[r] < self.items[smallest]:
            smallest = r

        if smallest != r:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.min_heapfiy(smallest)

    def build_min_heap(self):
        i = self.parent(len(self.items) - 1 )
        while i >= 0:
            self.min_heapfiy(i)
            i -= 1
