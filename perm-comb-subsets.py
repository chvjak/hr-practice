
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

        yield indexes

        #'step back'
        i = N - 1
        while not index_can_be_increased(indexes, i) and i > 0:
            indexes[i] = 0
            i -= 1

        indexes[i] += 1         # strange, it works)


def combinations(N = 4, M = 3):
    # w.o repetitions
    # for subsets there should be a loop for M = 1..N

    indexes = [0] * M
    i = 1

    # while there are more then M indexes i.e enough indexes to distribute between len(indexes)
    while N - indexes[0] >= M - 1 :
        #distibute the indexes
        for i in range(i, M):
            indexes[i] = indexes[i - 1] + 1

        for j in range(indexes[-1], N):
            yield indexes
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
    #subsets
    for i in range(1, N + 1):
        combinations(N, i)


#permutations(4)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, N, K):
        res = []
        for c in combinations(N, K):
            res.append(c[:])


        return res

S = Solution()
print(S.combine(1, 1))
print(S.combine(4, 2))




