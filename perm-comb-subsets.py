
def permutations(N = 3):
    def index_can_be_increased(indexes, i):
        N = len(indexes)
        j = 1
        while indexes[i] + j in indexes[:i] and indexes[i] + j < N:
            j += 1

        return indexes[i] + j < N

    # since len(indexes) = len(elements) => only one iteration on last element. so last pos reached => perm is built
    indexes = [0] * N

    # for 'current' index
    i = 0
    while indexes[0] < N:

        # distribute indexes
        # consider using indexes_used = set()
        while i < N:
            j = 0
            while indexes[i] + j in indexes[:i]:
                j += 1

            indexes[i] = indexes[i] + j
            i += 1

        print(indexes)

        #'step back'
        i = N - 1
        while not index_can_be_increased(indexes, i) and i > 0:
            indexes[i] = 0
            i -= 1

        indexes[i] += 1         # strange, it works)


def combinations(N = 4, M = 3):
    indexes = [0] * M

    # while there are more then M indexes i.e enough indexes to distribute between len(indexes)
    i = 1
    while N - indexes[0] >= M - 1:
        #distibute the indexes
        for k in range(i, M):
            indexes[k] = indexes[k - 1] + 1

        for j in range(indexes[-1], N):
            print(indexes)              # yield, or res += indexes
            indexes[-1] += 1

        # go back until there is enough indexes to distribute through M - i remaining elements 'indexes'
        i = M - 1                       # go back from last index
        while N - indexes[i] <= M - 1 - i:
            if i > 0:
                i -= 1
            else:
                # we are done : N - indexes[0] < M - 1
                break
        else:
            indexes[i] += 1
            i += 1

def subsets(N):
    for i in range(1, N + 1):
        combinations(N, i)


#permutations(4)

combinations(5, 5)




