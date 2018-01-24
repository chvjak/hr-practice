def count_climbs(A, res):

    if A == 0:
        res += 1
        return res

    res = count_climbs(A - 1, res)

    if A >= 2:
        res = count_climbs(A - 2, res)

    return res


class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        res = count_climbs(A, 0)
        return res


S = Solution()

print(S.climbStairs(3))