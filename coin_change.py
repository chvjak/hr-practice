f = open('coin_change1.txt')
def input():
    return f.readline()


import sys


def make_change(cache, coins, si, n):

    if n == 0:
        return 1

    if si == len(coins):
        return 0

    if cache[n][si] is not None:
        return cache[n][si]

    res = 0
    c = coins[si]
    max_coins = n // c
    for i in range(max_coins + 1):
        res += make_change(cache, coins, si + 1, n - i * c)

    cache[n][si] = res
    return res


def make_change_tabulated(cache, coins, si, n):
    coins.sort()
    for i in range(len(coins)+1):
        cache[0][i] = 1         # there is single way to have sum of 0

    for i in range(1, n + 1):
        cache[i][len(coins)] = 0         # there is no way to have a non-zero sum with 0 coins


    for i in range(1, n + 1):
        for j in range(len(coins)):
            if i < coins[j]:
                cache[i][j] = 0         # there is no way to have a sum having coins greated than that sum

            if i == coins[j]:
                cache[i][j] = 1         # if the sum is equal to current coin => other coins are greater - so there is only one way to have this sum


    # cache[i][j] - num of ways to get sum=i given coins j..max_coin_ix
    for current_n in range(1, n + 1):
        for ci in reversed(range(len(coins))):
            c = coins[ci]

            res = 0
            max_coins = current_n // c

            # cubic complexity?
            for i in reversed(range(0, max_coins + 1)):
                res += cache[current_n - i * c][ci + 1]


            cache[current_n][ci] = res

    return cache[n][0]          # number of ways to get sum=n having all coins at disposal


n, m = input().strip().split(' ')
target, coin_count = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]


cache = [[None] * (coin_count + 1) for _ in range(target + 1)]
#print(make_change(cache, coins, 0, target))
#print()
print(make_change_tabulated(cache, coins, 0, target))
