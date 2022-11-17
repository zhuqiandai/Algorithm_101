# 2022.11.17

def quick_sort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot - 1)
        quick_sort(list, pivot + 1, end)


def partition(list, start, end):
    pivot = list[end]

    i = start - 1

    for j in range(start, end):
        if list[j] <= pivot:
            i += 1
            swap(list, i, j)

    swap(list, i + 1, end)

    return i + 1


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


if __name__ == '__main__':
    list = [2, 3, 7, 1, 5, 4, 8, 6]

    quick_sort(list, 0, len(list) - 1)

    print("quick sort:", list)
