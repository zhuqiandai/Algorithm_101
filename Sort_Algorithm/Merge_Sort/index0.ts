function merge(l: number[], r: number[]): number[] {
    const result: number[] = []

    let i = 0
    let j = 0

    while (i < l.length && j < r.length) {
        l[i] < r[j] ? result.push(l[i++]) : result.push(r[j++])
    }

    return result.concat(i < l.length ? l.slice(i) : r.slice(j))
}

function mergeSort(list: number[]) {
    if (list.length > 1) {
        const { length } = list

        const pivot = Math.floor(length / 2)

        const l = mergeSort(list.slice(0, pivot))
        const r = mergeSort(list.slice(pivot, length))

        list = merge(l, r)
    }

    return list
}

const list = [2, 4, 5, 7, 1, 2, 3, 6]

const result = mergeSort(list)

console.log('merge sort result ', result)

export {}
