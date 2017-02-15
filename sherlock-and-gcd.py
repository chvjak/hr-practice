f = open('sherlock-and-gcd1.txt')
def input():
    return f.readline()

def combinations(N = 4, M = 3):
    # w.o repetitions
    # for subsets there should be a loop for M = 1..N
    # for permutations M = N, NOT QUITE: REPETITIONS SHOULD BE ALLOWED

    indexes = [0] * M
    i = 1
    res = []
    while N - indexes[0] >= M - 1 :
        #distibute the indexes
        for i in range(i, M):
            indexes[i] = indexes[i - 1] + 1

        for j in range(indexes[-1], N):
            res += [indexes[:]]
            indexes[-1] += 1

        # there should be enough indexes to distribute through M - i remaining elements 'indexes'
        i = M - 1 # go back form last index
        while N - indexes[i] <= M - 1 - i:
            if i > 0:
                i -= 1
            else:
                # we are done : N - indexes[0] <= M - 1
                break
        else:
            indexes[i] += 1
            i += 1
    return res

def subsets(A):
    N = len(A)
    res = []
    for i in range(2, N + 1):
        for ssi in combinations(N, i):
            res += [set([A[j] for j in ssi])]

    return res
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def is_there_mut_prime_subset(A):
    N = len(A)

    for ss in subsets(A):
        ss_gcd = A[0]
        for i in range(1, len(ss)):
          ss_gcd = gcd(ss_gcd, A[i])
          if ss_gcd == 1:
            return True
    return False


T = int(input())
for t in range(T):
    N = int(input())
    A = [int(x) for x in input().strip().split(' ')]

    if is_there_mut_prime_subset(A):
        print('YES')
    else:
        print('NO')

