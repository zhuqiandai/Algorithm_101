import {swap} from "../../lib/swap";

function QuickSort(A: number[], s: number, e: number) {
    if (s < e) {
        const pivot = partition(A, s, e)

        QuickSort(A, s, pivot - 1)
        QuickSort(A, pivot + 1, e)
    }
}


const A = [0, 2, 8, 7, 1, 3, 5, 6, 4]
QuickSort(A, 1, A.length)

console.log("quick sort a", A)

function partition(A: number[], s: number, e: number): number {
    const pivot = A[e]

    let i = s - 1

    for (let j = s; j <= e - 1; j++) {
        if (A[j] <= pivot) {
            i += 1
            swap(A, i, j)
        }
    }

    const pidx = i + 1
    swap(A, pidx, e)

    return pidx
}
