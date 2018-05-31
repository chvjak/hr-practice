#TODO: code chef

def neighbors(A):
    res = []
    R = len(A)
    C = len(A[0])

    for r in range(R):
        new_A = [row[:] for row in A]
        for i in range(C):
            new_A[r][i] += 1
        res.append(new_A)

    for c in range(C):
        new_A = [row[:] for row in A]
        for i in range(R):
            new_A[i][c] += 1
        res.append(new_A)

    return res


def bfs_transform(A, B):
    Q = Queue()

    Q.enq((A, B, 0))
    while len(Q):
        A, B, level = Q.deq()

        for next_A in neighbors(A):
            if next_A == B:
                return level + 1

            Q.enq(next_A, B, level + 1)

            for next_B in neighbors(B):
                if next_B == next_A:
                    return level + 1

                Q.enq(next_A, next_B, level + 1)






T = int(input())

for t in range(T):
    M, N = int(input())

    A = []
    for m in range(M):
        row = [int(x) for x in input().strip().split(' ')]
        A.append(row)


    B = []
    for m in range(M):
        row = [int(x) for x in input().strip().split(' ')]
        B.append(row)

    res = bfs_transform(A, B)

    print(res)


