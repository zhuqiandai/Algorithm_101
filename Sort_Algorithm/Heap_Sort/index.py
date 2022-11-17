# 2022.11.17

class Heap(object):

    def __init__(self) -> None:
        self.data = []

    def size(self):
        return len(self.data)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return i // 2

    def maxHeapify(self, i, pointer):
        lidx = self.left(i)
        ridx = self.right(i)

        max = 0

        if lidx < pointer and self.data[lidx] > self.data[i]:
            max = lidx
        else:
            max = i

        if ridx < pointer and self.data[ridx] > self.data[max]:
            max = ridx

        if max != i:
            swap(self.data, max, i)
            self.maxHeapify(max, pointer)

    def insert(self, ele):
        pass

    def build_max_heap(self):
        pointer = self.size()
        non_leaf = len(self.data) // 2

        i = non_leaf
        while i >= 0:
            self. maxHeapify(i, pointer)
            i -= 1

    def heap_sort(self, pointer):
        self.build_max_heap()

        i = pointer
        while i > 0:
            swap(self.data, 0, i)
            self.maxHeapify(0, i)
            i -= 1

    def priority_queue():
        pass


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


if __name__ == '__main__':
    heap = Heap()

    heap.data.append(4)
    heap.data.append(1)
    heap.data.append(3)
    heap.data.append(2)
    heap.data.append(16)
    heap.data.append(9)
    heap.data.append(10)
    heap.data.append(14)
    heap.data.append(8)
    heap.data.append(7)

    pointer = heap.size() - 1
    heap.heap_sort(pointer)

    print("build max heap", heap.data)
