"use strict";
exports.__esModule = true;
function merge(l, r) {
    var result = [];
    var i = 0;
    var j = 0;
    while (i < l.length && j < r.length) {
        l[i] < r[j] ? result.push(l[i++]) : result.push(r[j++]);
    }
    return result.concat(i < l.length ? l.slice(i) : r.slice(j));
}
function mergeSort(list) {
    if (list.length > 1) {
        var length_1 = list.length;
        var pivot = Math.floor(length_1 / 2);
        var l = mergeSort(list.slice(0, pivot));
        var r = mergeSort(list.slice(pivot, length_1));
        list = merge(l, r);
    }
    return list;
}
var list = [2, 4, 5, 7, 1, 2, 3, 6];
var result = mergeSort(list);
console.log('merge sort result ', result);
