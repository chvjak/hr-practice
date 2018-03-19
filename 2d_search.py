def sm(m, r0, c0, rN, cN, t):
    R = rN - r0 + 1
    if R == 0:
        return False

    C = cN - c0 + 1
    if C == 0:
        return False

    if R == 1 and C == 1:
        return m[r0][c0] == t

    if m[r0][c0] > t or m[rN][cN] < t:
        return False

    mr = (r0 + rN) // 2
    mc = (c0 + cN) // 2
    res = False

    res |= sm(m, r0, c0, mr, mc, t)
    res |= sm(m, r0, mc + 1, mr, cN, t)
    res |= sm(m, mr + 1, mc + 1, rN, cN, t)
    res |= sm(m, mr + 1, c0, rN, mc, t)
    return res


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, m, t):
        R = len(m)

        if R == 0:
            return False

        C = len(m[0])

        if C == 0:
            return False

        return sm(m, 0, 0, R - 1, C - 1, t)

S = Solution()

m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,23,30]]
t = 4

m = [[1, 1, 3, 5, 7]]

print(S.searchMatrix(m, t))