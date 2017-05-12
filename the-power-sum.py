f = open('the-power-sum.txt')
def input():
    return f.readline()

from math import floor, ceil


def count_decompositions(X, N):
    if X == 0:
        return 0

    max_r = floor(X ** (1 / N))
    min_r = ceil((X - max_r ** N) ** (1 / N)) + 1
    res = 0

    if max_r ** N == X:
        res += 1

    for r in range(min_r, max_r + 1):
        res += count_decompositions(X - r ** N, N)

    return res


X = int(input().strip())
N = int(input().strip())

print(count_decompositions(X, N))
