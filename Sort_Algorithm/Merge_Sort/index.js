"use strict";
// /**
//  *  使用哨兵
//  */
// function merge(list: Array<number>, start: number, pivot: number, end: number) {
//     const lindex = pivot - start + 1
//     const rindex = end - pivot
exports.__esModule = true;
//     const l: number[] = []
//     const r: number[] = []
//     for (let i = 1; i <= lindex; i++) {
//         l[i] = list[start + i - 1]
//     }
//     for (let i = 1; i <= rindex; i++) {
//         r[i] = list[pivot + i]
//     }
//     l[lindex + 1] = Infinity
//     r[rindex + 1] = Infinity
//     let i = 1
//     let j = 1
//     let k = start
//     while (k <= end) {
//         l[i] < r[j] ? (list[k] = l[i++]) : (list[k] = r[j++])
//         k += 1
//     }
// }
// function mergeSort(list: Array<number>, start: number, end: number) {
//     if (start < end) {
//         const pivot = Math.floor((start + end) / 2)
//         mergeSort(list, start, pivot)
//         mergeSort(list, pivot + 1, end)
//         merge(list, start, pivot, end)
//     }
// }
// const list = [2, 4, 5, 7, 1, 2, 3, 6]
// mergeSort(list, 0, list.length - 1)
// console.log('merge sort result ', list)
// export {}
/**
 *  使用哨兵
 */
function merge(list, start, pivot, end) {
    var lindex = pivot - start + 1;
    var rindex = end - pivot;
    var l = [];
    var r = [];
    for (var i_1 = 1; i_1 <= lindex; i_1++) {
        l[i_1] = list[start + i_1 - 1];
    }
    for (var i_2 = 1; i_2 <= rindex; i_2++) {
        r[i_2] = list[pivot + i_2];
    }
    l[lindex + 1] = Infinity;
    r[rindex + 1] = Infinity;
    var i = 1;
    var j = 1;
    var k = start;
    while (k <= end) {
        l[i] < r[j] ? (list[k] = l[i++]) : (list[k] = r[j++]);
        k += 1;
    }
    console.log(l, '', r);
}
function mergeSort(list, start, end) {
    if (start < end) {
        var pivot = Math.floor((start + end) / 2);
        mergeSort(list, start, pivot);
        mergeSort(list, pivot + 1, end);
        merge(list, start, pivot, end);
    }
}
var list = [2, 4, 5, 7, 1, 2, 3, 6];
mergeSort(list, 0, list.length - 1);
console.log('merge sort result ', list);
