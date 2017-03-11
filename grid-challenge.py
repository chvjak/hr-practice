file = open('grid-challenge.txt')


def input():
    return file.readline()


def cols_sorted(A):
    N = len(A)
    for k in range(N):
        for j in range(N - 1):
            if A[j][k] > A[j + 1][k]:
                return False
    else:
        return True

T = int(input())
for i in range(T):
    N = int(input())
    A = [None] * N
    for j in range(N):
        A[j] = list(input().strip())
        A[j].sort()

    if cols_sorted(A):
        print('YES')
    else:
        print('NO')

