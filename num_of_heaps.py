from math import log2


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # sum of all permutations for each layer
        # permutations(N) = N!

        num_of_full_layers = int(log2(A + 1))
        size_of_last_layer = A - (2 ** num_of_full_layers - 1)

        res = 1
        permutations_i = 1
        # A = 3: i = {0, 1}
        for i in range(num_of_full_layers):
            if i != 0:
                # A = 3: j = {}, {2}, {3, 4}, {5, 6, 7, 8}
                for j in range(2 ** (i - 1) + 1, 2 ** i + 1):
                    permutations_i *= j
                    permutations_i %= 1000000007

            res *= permutations_i
            res %= 1000000007

        permutations_i = 1
        for j in range(1, size_of_last_layer + 1):
            permutations_i *= j
            permutations_i %= 1000000007

        res *= permutations_i
        res %= 1000000007

        return res

s = Solution()

print(s.solve(1))
print(s.solve(2))
print(s.solve(3)) # 2
print(s.solve(7)) # 1 * 2 * 4! = 2 * (1 * 2 * 3 * 4) = 2 *