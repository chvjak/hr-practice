# TODO: bottom up
def longest_ap(arr, cache, si = 0, delta=0):
    N = len(arr)

    if N - 1 == si:
        return 1        # +1 for the first element of arithmetic progression

    if delta in cache[si].keys():
        return cache[si][delta]

    res = res1 = res2 = 0
    for i in range(si + 1, N):
        if arr[si] + delta == arr[i]:
            res1 = 1 + longest_ap(arr, cache, i, delta)  # try continue with current delta

        res2 = longest_ap(arr, cache, i, arr[i] - arr[si])

        res = max(res, res1, res2)

    cache[si][delta] = res

    return res


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, arr):
        N = len(arr)
        if N == 0:
            return 0

        if N == 1:
            return 1

        cache = [{} for _ in range(N)]

        res = longest_ap(arr, cache, 0, arr[1] - arr[0])

        return res


S = Solution()
print(S.solve([2,2]))
print(S.solve([2,2,2]))
print(S.solve([1, 2,2]))
print(S.solve([1, 2,2,2]))
print(S.solve([100,10,8,300,6,1,4,2]))
print(S.solve([1, 2, 3, 4]))
print(S.solve([2, 1, 4, 1, 6, 3, 8]))