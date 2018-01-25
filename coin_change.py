def count_coinchange(coins_list, cix, target, cache):

    if target == 0:
        return 1

    if cix == len(coins_list):
        return 0

    if cache[cix][target] != -1:
        return cache[cix][target]

    res = 0
    c = coins_list[cix]
    for i in range(target // c + 1):
        if target >= c * i:
            res += count_coinchange(coins_list, cix + 1,  target - c * i, cache)

    cache[cix][target] = res
    return res


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, coins_list, target):
        cache_row = [-1] * (target + 1)
        cache = [cache_row[:] for __ in range(len(coins_list))]
        res = count_coinchange(coins_list, 0, target, cache)

        return res


S = Solution()

print(S.coinchange2([1, 2, 3], 4))