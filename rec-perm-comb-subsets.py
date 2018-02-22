def combinations(arr, M):
    N = len(arr)
    if M == 0:
        return [set()]

    if M > N:
        return [set()]

    res = []
    for i in range(N - M + 1):
        res1 = combinations(arr[i + 1:], M - 1)

        for r in res1:
            r.add(arr[i])
            res.append(r)

    return res



def subsets(arr):

    # get all in range(N)
    ...
        # get combination(arr, i)



def permutations(arr):
    N = len(arr)
    if N == 1:
        return [[arr[0]]]

    res = []
    for i in range(N):
        res1 = permutations(arr[:i] + arr[i + 1:])
        for r in res1:
            res.append(r + [arr[i]])

    return res

#p = permutations([1,2,3])
#print(len(p), p)

s = combinations([1,2,3, 4], 2)
print(s)

#print(permutations0([1,2]))