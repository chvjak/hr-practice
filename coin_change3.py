# get minimum number of coins
import sys


def nr_dp_coin_change(coins, amount):
    cache = [sys.maxsize] * (amount + 1)
    cache[0] = 0

    for a in range(amount + 1):
        for c in coins:
            if amount - c >= 0:
                if cache[a - c] is not None:
                    res1 = 1 + cache[a - c]

                    cache[a] = min(cache[a], res1)


    return cache[amount]


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = [None] * (amount + 1)

        def dp_coin_change(coins, amount):
            if amount == 0:
                return 0

            if cache[amount] is not None:
                return cache[amount]

            res = sys.maxsize
            for c in coins:
                if amount - c >= 0:
                    res1 = 1 + dp_coin_change(coins, amount - c)

                    res = min(res, res1)

            cache[amount] = res
            return res

        res = dp_coin_change(coins, amount)

        if res == sys.maxsize:
            res = -1

        return res

    def coinChangeNR(self, coins, amount):
        return nr_dp_coin_change(coins, amount)


S = Solution()
print(S.coinChange([1,2,5], 11))
print(S.coinChangeNR([1,2,5], 11))