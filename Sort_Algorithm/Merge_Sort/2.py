# 2022.11.18

def merge_sort(list, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid + 1, end)

        merge(list, start, mid, end)


def merge(list, start, mid, end):
    # 这里需要 rlen + llen = end - start + 1
    llen = mid - start + 1
    rlen = end - mid

    L = [0] * llen
    R = [0] * rlen

    print(llen, rlen, mid)

    for i in range(0, llen):
        L[i] = list[start + i]

    for i in range(0, rlen):
        R[i] = list[mid + i + 1]

    i = 0
    j = 0
    k = start
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


if __name__ == '__main__':
    list = [2, 4, 5, 7, 11, 12, 3, 6, 9, 1]

    start = 0
    end = len(list) - 1
    merge_sort(list, start, end)

    print("merge sort result", list)
