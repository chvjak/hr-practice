#!/bin/python3
#https://www.hackerrank.com/challenges/largest-permutation/problem

f = open('largest_permuatation.txt')
def input():
    return f.readline()

import sys


def largestPermutation0(k, arr):
    # Complete this function

    arr_cpy = arr[:]
    arr_cpy.sort(reverse=True)

    for i, n in enumerate(arr_cpy):
        ix = arr.index(n)
        if i != ix:
            arr[i], arr[ix] = arr[ix], arr[i]
            k -= 1

            if k == 0:
                break

    return arr

def largestPermutation(k, arr):
    N = len(arr)

    old_ix_of_sorted = [i for i in range(N)]
    old_ix_of_sorted.sort(key=lambda i: arr[i], reverse=True)

    res = arr[:]
    for i in range(k):
        res[i] = N - i

    # TODO: Not decrease k if on its place
    # TODO: if old_ix_of_sorted[i] < k => corrupts res

    for i in range(k):
        res[old_ix_of_sorted[i]] = arr[i]

    return res


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = largestPermutation(k, arr)
    print(" ".join(map(str, result)))


