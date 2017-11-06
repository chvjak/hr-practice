def pow2(self, x, n, d):
    if n == 0:
        return 0 if x == 0 else 1

    if n == 1:
        return x % d

    x = (x % d)
    res = 1
    while n > 0:
        if n % 2:
            res = (res * x) % d

        x = (x * x) % d
        n = n // 2

    return res