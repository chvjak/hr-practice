#!/bin/python3
#https://www.hackerrank.com/challenges/largest-permutation/problem

f = open('largest_permuatation.txt')
def input():
    return f.readline()

import sys


def largestPermutation(k, arr):
    # Complete this function


    N = len(arr)
    ix_dict = dict(zip([i for i in range(1, N + 1)], [arr.index(i) for i in range(1, N + 1)]))

    for i, n in enumerate(reversed(range(1, N + 1))):
        ix = ix_dict[n]
        if i != ix:
            arr[i], arr[ix] = arr[ix], arr[i]
            ix_dict[arr[i]], ix_dict[arr[ix]] = ix_dict[arr[ix]], ix_dict[arr[i]]
            k -= 1

            if k == 0:
                break

    return arr



if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = largestPermutation(k, arr)
    print(" ".join(map(str, result)))


