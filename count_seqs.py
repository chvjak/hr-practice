def CountSeqs(mins, maxs, prev):
    if len(mins) == 0:
        return 1

    if mins[0] <= prev + 1 <= maxs[0]:
        res = 0
        for i in range(prev + 1, maxs[0] + 1):
            res += CountSeqs(mins[1:], maxs[1:], i)

        return res
    else:
        return 0


print(CountSeqs([7,8], [9, 10], 6))