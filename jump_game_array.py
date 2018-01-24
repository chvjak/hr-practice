def canJumpDP(A, si, cache):
    if cache[si] is not None:
        return cache[si]

    N = len(A)
    print(N, N - 1, si)

    if N - 1 - si <= A[si]:  # N = 5, last index = 5 - 1 = 4, si = 3
        return True

    res = False
    for i in range(1, A[si] + 1):
        res1 = canJumpDP(A, si + i, cache)
        if res1:
            res = True
            break

    cache[si] = res
    return res


class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        cache = [None] * len(A)
        res = canJumpDP(A, 0, cache)

        return 1 if res else 0

S = Solution()
print(S.canJump([1, 1, 1, 1, 0]))