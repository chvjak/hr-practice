def CountSeqs(mins, maxs):
    def CountSeqsDP(mins, maxs, ix, prev):
        N = len(mins)
        if ix == N:
            return 1


        start = max(mins[ix], prev + 1)
        if start in cache[ix].keys():
            return cache[ix][start]

        if mins[ix] <= start <= maxs[ix]:
            res = 0
            for i in range(start, maxs[ix] + 1):
                res += CountSeqsDP(mins, maxs, ix + 1, i)
                res %= 998244353

            cache[ix][start] = res
            return res
        else:
            cache[ix][start] = 0
            return 0

    N = len(mins)
    cache = [{} for i in range(N)]
    return CountSeqsDP(mins, maxs, 0, mins[0] - 1)


print(CountSeqs([1, 3, 1, 4], [6, 5, 4, 6]))
print(CountSeqs([7, 8], [9, 10]))
print(CountSeqs([20, 10], [30, 20]))
print(CountSeqs([10, 20], [20, 30]))
print(CountSeqs([4, 46, 46, 35, 20, 77, 20], [41, 65, 84, 90, 49, 86, 88]))
print(CountSeqs([1, 1, 1], [10000, 10000, 10000]))