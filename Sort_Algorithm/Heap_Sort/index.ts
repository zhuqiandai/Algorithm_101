/**
 *  1. 堆化 max-heapify
 *  2. 建堆 build-heap
 *  3. 堆排序 heapSort
 *  4. 优先级队列 priority queue
 */
import {swap} from "../../lib/swap";

const left = (i: number) => 2 * i + 1
const right = (i: number) => 2 * i + 2
const parent = (i: number) => Math.floor(i / 2)

function maxHeapify(A: number[], i: number, s: number) {
    const l = left(i)
    const r = right(i)

    let max = i

    if (l < s) {
        A[l] > A[max] && (max = l)
    }

    if (r < s) {
        A[r] > A[max] && (max = r)
    }

    if (max !== i) {
        swap(A, i, max)
        maxHeapify(A, max, s)
    }
}

function buildMax(A: number[]) {
    const mid = Math.floor(A.length / 2)
    const size = A.length

    for (let i = mid; i >= 0; i--) {
        maxHeapify(A, i, size)
    }
}

function heapSort(A: number[]) {
    buildMax(A)
    let s = A.length

    while (s > 1) {
        swap(A, 0, --s)
        maxHeapify(A, 0, s)
    }
}

const A = [
    3, 1, 9, 4, 7,
    8, 2, 10, 14, 16
]
heapSort(A)

console.log("A: ", A)
