def permutations(N = 3):
    pass
    # ?

def combinations(N = 4, M = 3):
    # w.o repetitions
    # for subsets there should be a loop for M = 1..N

    indexes = [0] * M
    i = 1
    while N - indexes[0] >= M - 1 :
        #distibute the indexes
        for i in range(i, M):
            indexes[i] = indexes[i - 1] + 1

        for j in range(indexes[-1], N):
            print(indexes)
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

def subsets(N):
    #subsets
    for i in range(1, N + 1):
        combinations(N, i)







