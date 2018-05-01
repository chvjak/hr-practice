'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# Your task is to complete this Function \
# function should return True/False
def isInterleave(A, B, C):
    # Code here

    cache = {}
    def dp_isInterleave(a_ix, b_ix, c_ix):
        if a_ix == len(A) and b_ix == len(B) and c_ix == len(C):
            return True

        if (a_ix, b_ix, c_ix) in cache:
            return cache[(a_ix, b_ix, c_ix)]


        if a_ix < len(A) and A[a_ix] == C[c_ix]:
            res1 = dp_isInterleave(a_ix + 1, b_ix, c_ix + 1)
        else:
            res1 = False

        if b_ix < len(B) and B[b_ix] == C[c_ix]:
            res2 = dp_isInterleave(a_ix, b_ix + 1, c_ix + 1)
        else:
            res2 = False

        res = res1 or res2
        cache[(a_ix, b_ix, c_ix)] = res

        return res

    return dp_isInterleave(0, 0, 0)


print(isInterleave(*'XY X XXY'.split(' ')))
print(isInterleave(*'YX X XXY'.split(' ')))
print(isInterleave(*'YXY XYXYX XXXXYYXY'.split(' ')))