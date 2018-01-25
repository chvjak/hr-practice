def balance(l, r, weights, wc=0):
    '''
    wc - weihgjt count
    '''
    if l == r:
        return []

    if wc == 2:
        return None

    if len(weights) == 0:
        return None

    res = [None] * 3
    res[0] = balance(l + weights[0], r, weights[1:], wc + 1)
    if res[0] is not None:
        res[0].append(weights[0])

    res[1] = balance(l, r + weights[0], weights[1:], wc + 1)
    if res[1] is not None:
        res[1].append(weights[0])

    res[2] = balance(l, r, weights[1:], wc)

    min_r = None
    for r in res:
        if r is not None:
            if min_r is None:
                min_r = r
            else:
                if len(r) < len(min_r):
                    min_r = r

    return min_r


def ScaleBalancing(strArr):
    (l, r), weights = eval(strArr[0]), eval(strArr[1])

    res = balance(l, r, weights)
    res.sort()
    # code goes here
    return res


# keep this function call here
print(ScaleBalancing( ["[5, 9]", "[1, 2, 6, 7]"] ))
















