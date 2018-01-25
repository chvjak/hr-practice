def is_valid_pos(A, pos):
    r, c = pos
    M = len(A)
    N = len(A[0])

    if 0 <= r < M and 0 <= c < N and A[r][c] == 0:
        return True
    else:
        return False


def unique_path_count(A, pos, cache):
    res = 0
    r, c = pos
    M = len(A)
    N = len(A[0])

    if cache[r][c] != -1:
        return cache[r][c]

    if r == M - 1 and c == N - 1:
        return 1

    move1 = (r + 1, c)
    if is_valid_pos(A, move1):
        res1 = unique_path_count(A, move1, cache)
    else:
        res1 = 0

    move2 = (r, c + 1)
    if is_valid_pos(A, move2):
        res2 = unique_path_count(A, move2, cache)
    else:
        res2 = 0

    res = res1 + res2

    cache[r][c] = res
    return cache[r][c]


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        M = len(A)
        N = len(A[0])

        row = [-1] * N
        cache = [row[:] for __ in range(M)]
        res = unique_path_count(A, (0, 0), cache)

        return res


S = Solution()

print(S.uniquePathsWithObstacles([[0, 0, 0],[0, 1, 0], [0, 0, 0]]))