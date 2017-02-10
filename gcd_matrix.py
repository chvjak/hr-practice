f = open('gcd_matrix2.txt')
def input():
    return f.readline()

import sys

def memoize(function):
    from functools import wraps

    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


@memoize
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


class UniqueCounter:
    def __init__(self, gcd_matrix, gcd_dict):
        # calculate ingredients

        R = len(gcd_matrix)
        C = len(gcd_matrix[0])

        row_template = [None] * C
        unique_gcd_count = [row_template[:] for x in range(R)]

        gcd_count = len(gcd_dict)
        for i in range(R):
            for j in range(C):
                uc = [0] * gcd_count

                if j > 0:
                    uc = [a + b for a, b in zip(uc, unique_gcd_count[i][j - 1])]

                if i > 0:
                    uc = [a + b for a, b in zip(uc, unique_gcd_count[i - 1][j])]

                if i > 0 and j > 0:
                    uc = [a - b for a, b in zip(uc, unique_gcd_count[i - 1][j - 1])]

                uc[gcd_dict[gcd_matrix[i][j]]] += 1
                unique_gcd_count[i][j] = uc


        self.unique_gcd_count = unique_gcd_count

    def get_count(self, r0, c0, rN, cN):

        uc = self.unique_gcd_count[rN][cN]

        if r0 > 0:
            uc = [a - b for a, b in zip(uc, self.unique_gcd_count[r0 - 1][cN])]

        if c0 > 0:
            uc = [a - b for a, b in zip(uc, self.unique_gcd_count[rN][c0 - 1])]

        if r0 > 0 and c0 > 0:
            uc = [a + b for a, b in zip(uc, self.unique_gcd_count[r0 - 1][c0 - 1])]

        return sum([1 for x in uc if x > 0])


def count_distinct(matrix, query):
    r1, c1, r2, c2 = query
    sm = matrix[r1:r2 + 1]
    sm = [r[c1:c2 + 1] for r in sm]

    s = set()
    for r in sm:
        s |= set(r)

    return len(s)

def run():
    n, m, q = input().strip().split(' ')
    n, m, q = [int(n), int(m), int(q)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    queries = []
    for a0 in range(q):
        r1, c1, r2, c2 = input().strip().split(' ')
        r1, c1, r2, c2 = [int(r1), int(c1), int(r2), int(c2)]
        # your code goes here
        queries += [[r1, c1, r2, c2]]

    data = []
    max_gcd = max(a + b)
    gcd_list = [0] * (max_gcd + 1)
    for aa in a:
        row = []
        for bb in b:
            gcd_ab = GCD(aa, bb)
            gcd_list[gcd_ab] = 1
            row += [gcd_ab]

        data += [row]

    gcd_np = data

    # TODO: consider sorting of gcd_list by freq

    gcd_list = [i for i in range(max_gcd + 1) if gcd_list[i] != 0]

    uc = UniqueCounter(data, dict(zip(gcd_list, range(len(gcd_list)))))
 #   for r1, c1, r2, c2 in queries:
        #print(count_distinct(gcd_np, [r1, c1, r2, c2]))
  #      print(uc.get_count(r1, c1, r2, c2))

import cProfile as profile

profile.run("run()")






