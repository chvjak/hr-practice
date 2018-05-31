def cutRod(rod_length, cut_prices):
    cache = {}

    def cutRodDP(rod_length):
        if rod_length in cache.keys():
            return cache[rod_length]
        res = cut_prices[rod_length - 1]
        for cut in range(1, rod_length):
            if cut <= rod_length:
                res1 = cutRodDP(rod_length - cut) + cut_prices[cut - 1]
                res = max(res1, res)

        cache[rod_length] = res
        return res

    res = cutRodDP(rod_length)

    return res


# code
T = int(input().strip())
for t in range(T):
    rod_length = int(input().strip())
    cut_prices = [int(x) for x in input().strip().split(' ')]

    res = cutRod(rod_length, cut_prices)

    print(res)

