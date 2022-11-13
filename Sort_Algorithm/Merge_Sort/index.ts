/**
 *  使用哨兵
 * @param list
 * @param start
 * @param pivot
 * @param end
 */
function merge(list: Array<number>, start: number, pivot: number, end: number) {
    const lindex = pivot - start + 1
    const rindex = end - pivot

    const l: number[] = []
    const r: number[] = []

    for (let i = 1; i <= lindex; i++) {
        l[i] = list[start + i - 1]
    }

    for (let i = 1; i <= rindex; i++) {
        r[i] = list[pivot + i]
    }

    l[lindex + 1] = Infinity
    r[rindex + 1] = Infinity

    let i = 1
    let j = 1
    let k = start

    while (k <= end) {
        l[i] < r[j] ? (list[k] = l[i++]) : (list[k] = r[j++])

        k += 1
    }
}

function mergeSort(list: Array<number>, start: number, end: number) {
    if (start < end) {
        const pivot = Math.floor((start + end) / 2)

        mergeSort(list, start, pivot)
        mergeSort(list, pivot + 1, end)

        merge(list, start, pivot, end)
    }
}

const list = [2, 4, 5, 7, 1, 2, 3, 6]

mergeSort(list, 0, list.length - 1)

console.log('merge sort result ', list)

export {}
