f = open('merge_sort2.txt')
def input():
    return f.readline()

def merge(l_arr, r_arr):
    res = []
    LN, RN = len(l_arr), len(r_arr)

    li = 0
    ri = 0
    inv_count = 0

    while li < LN and ri < RN:
        if l_arr[li] <= r_arr[ri]:
            res.append(l_arr[li])
            li += 1
        else:
            res.append(r_arr[ri])
            ri += 1

            inv_count += LN - li        # TODO: still something is incorrect. 2FIX

    if li < LN:
        res.extend(l_arr[li:])
    else:
        res.extend(r_arr[ri:])

    return inv_count, res


def merge_sort(arr):
    N = len(arr)

    if N > 1:
        mid = N // 2
        inv_count_l, l_arr = merge_sort(arr[:mid])
        inv_count_r, r_arr = merge_sort(arr[mid:])

        inv_count, sorted_arr = merge(l_arr, r_arr)

        return inv_count_l + inv_count + inv_count_r, sorted_arr
    else:
        return 0, arr

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def inversionCount(self, A):

        inv_count, res = merge_sort(A)
        #print(inv_count, res)

        return inv_count


T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]

    S = Solution()

    print(S.inversionCount(arr))