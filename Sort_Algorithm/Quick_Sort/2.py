def quick_sort(list, start, end):
    if start < end:
        p = partition(list, start, end)

        quick_sort(list, start, p - 1)
        quick_sort(list, p + 1, end)


def partition(list, start, end):
    pivot = list[end]

    i = start - 1
    j = start

    while j < end:
        if list[j] >= pivot:
            i += 1
            swap(list, i, j)
        j += 1

    n_pivot = i + 1
    swap(list, end, n_pivot)

    return n_pivot


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


if __name__ == '__main__':
    list = [2, 3, 7, 1, 5, 4, 8, 6]

    quick_sort(list, 0, len(list) - 1)

    print("quick sort:", list)
