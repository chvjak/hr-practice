def my_lis(A, min_n=0):

    N = len(A)
    lis = [1] * N

    for i in range(1, N):
        for j in range(0, i):
            if A[i] > A[j] and lis[i] <= lis[j]:
                lis[i] = lis[j] + 1

    return max(lis)



    return res


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        res = my_lis(A)
        return res


S = Solution()

print(S.lis([ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 ]))