#https://leetcode.com/problems/different-ways-to-add-parentheses/description/

def genPlacements(N, oc=0, cc=0):
    if oc == cc == N:
        return ['']

    res = []
    # if oc < N => can open
    if oc < N:
        for s in genPlacements(N, oc + 1, cc):
            res.append('(' + s)

    # if 0 < cc < oc => can close
    if 0 <= cc < oc:
        for s in genPlacements(N, oc, cc + 1):
            res.append(')' + s)

    return res


def getLHS(str1):
    digits = '0123456789'
    res = []
    for c in reversed(list(str1)):
        if c in digits:
            res.insert(0, c)
        else:
            break

    return int(''.join(res))


def getRHS(str1):
    digits = '0123456789'
    res = []
    for c in list(str1):
        if c in digits:
            res.append(c)
        else:
            break

    return int(''.join(res))


class Solution:
    def diffWaysToCompute(self, input1):
        """
        :type input: str
        :rtype: List[int]
        """

        # tokenize: count op signs = N, find places for parenthesis arr
        N = 0
        tokenized = []
        for i, c in enumerate(input1):
            if c in '+-*':
                N += 1
                lhs = getLHS(input1[:i])
                rhs = getRHS(input1[i + 1:])

                tokenized.append((i, lhs, rhs))

        # get all possible parenthesis placements
        res = genPlacements(N)

        return res


S = Solution()
#print(S.diffWaysToCompute('12-21-33-45'))
print(S.diffWaysToCompute('1-2*3'))