# 2022.11.17

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


def merge(list, left, mid, right):
    llen = mid - left + 1
    rlen = right - mid

    L = [0] * llen
    R = [0] * rlen

    for i in range(0, llen):
        L[i] = list[left + i]

    for j in range(0, rlen):
        R[j] = list[mid + j + 1]

    i = 0
    j = 0
    k = left

    while i < llen and j < rlen:
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    while i < llen:
        list[k] = L[i]
        i += 1
        k += 1

    while j < rlen:
        list[k] = R[j]
        j += 1
        k += 1


def merge_sort(list, start, right):
    if (start < right):
        mid = start + (right - start) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid + 1, right)

        merge(list, start, mid, right)


if __name__ == '__main__':
    list = [2, 4, 5, 7, 1, 2, 3, 6, 9, 1]

    start = 0
    end = len(list) - 1
    merge_sort(list, start, end)

    print("merge sort result", list)
