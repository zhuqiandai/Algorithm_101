class Heap():
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

    def max_heapify(self, i, pointer):
        lidx = self.left(i)
        ridx = self.right(i)

        max = 0
        d = self.data

        if lidx < pointer and d[lidx] > d[i]:
            max = lidx
        else:
            max = i

        if ridx < pointer and d[ridx] > d[max]:
            max = ridx

        if max != i:
            swap(d, i, max)
            self.max_heapify(max, pointer)

    def build_max_heap(self):
        node = self.size() // 2

        i = node
        p = self.size() - 1
        while i >= 0:
            self.max_heapify(i, p)
            i -= 1

    def heap_sort(self):
        self.build_max_heap()

        d = self.data
        p = self.size() - 1

        while p > 0:
            swap(d, 0, p)
            self.max_heapify(0, p)
            p -= 1


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

    heap.heap_sort()

    print("build max heap", heap.data)
