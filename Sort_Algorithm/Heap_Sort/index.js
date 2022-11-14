"use strict";
exports.__esModule = true;
/**
 *  1. 堆化 max-heapify
 *  2. 建堆 build-heap
 *  3. 堆排序 heapSort
 *  4. 优先级队列 priority queue
 */
var swap_1 = require("../../lib/swap");
var left = function (i) { return 2 * i + 1; };
var right = function (i) { return 2 * i + 2; };
var parent = function (i) { return Math.floor(i / 2); };
function maxHeapify(A, i, s) {
    var l = left(i);
    var r = right(i);
    var max = i;
    if (l < s) {
        A[l] > A[max] && (max = l);
    }
    if (r < s) {
        A[r] > A[max] && (max = r);
    }
    if (max !== i) {
        (0, swap_1.swap)(A, i, max);
        maxHeapify(A, max, s);
    }
}
function buildMax(A) {
    var mid = Math.floor(A.length / 2);
    var size = A.length;
    for (var i = mid; i >= 0; i--) {
        maxHeapify(A, i, size);
    }
}
function heapSort(A) {
    buildMax(A);
    var s = A.length;
    while (s > 1) {
        (0, swap_1.swap)(A, 0, --s);
        maxHeapify(A, 0, s);
    }
}
var A = [
    3, 1, 9, 4, 7,
    8, 2, 10, 14, 16
];
heapSort(A);
console.log("A: ", A);
