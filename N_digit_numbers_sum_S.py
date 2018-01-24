def countNumbersTabulated(cache, N, S):
    for i in range(N + 1):
        cache[i][0] = 0

    for i in range(S + 1):
        cache[0][i] = 0

    for i in range(min(10, S + 1)):
        cache[1][i] = 1

    for j in range(2, N + 1):
        for k in range(S + 1):
            res = cache[j - 1][k]
            for i in range(1, 10):
                if i < k:
                    res += cache[j - 1][k - i]
            cache[j][k] = res % 1000000007

    return cache[N][S]

def countNumbers(cache, N, S):
    if cache[N][S] is not None:
        return cache[N][S]

    if S == 0:
        return 0

    if N == 1 and S < 10:
        cache[N][S] = 1
        return 1

    if N == 0:
        return 0

    res = countNumbers(cache, N - 1, S) # for trailing zero


    res %= 1000000007

    # loop through digits
    for i in range(1, 10):
        if i < S:
            res += countNumbers(cache, N - 1, S - i)


        res %= 1000000007



    cache[N][S] = res
    return res



class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, S):
        cache = [[0] * (S + 1) for _ in range(N + 1)]
        #res = countNumbers(cache, N, S)
        res = countNumbersTabulated(cache, N, S)

        return res

    def solveDP(self, N, S):
        cache = [[None] * (S + 1) for _ in range(N + 1)]
        res = countNumbers(cache, N, S)

        return res


S = Solution()

print(S.solve(2, 11))

print(S.solve(2, 3))
print(S.solve(3, 4))
print(S.solve(2, 4))

print()

print(S.solveDP(2, 11))
print(S.solveDP(2, 3))
print(S.solveDP(3, 4))
print(S.solveDP(2, 4))
