# this looks like coin change
def get_all_combinations(numbers, number_ix, target_sum):
    if target_sum < 0:
        return []

    if target_sum == 0:
        return [[]]

    res1 = get_all_combinations(numbers, number_ix, target_sum - numbers[number_ix])
    res1 = [r + [numbers[number_ix]] for r in res1]

    if number_ix > 0:
        res2 = get_all_combinations(numbers, number_ix - 1, target_sum)
    else:
        res2 = []

    return res1 + res2


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, numbers, target_sum):
        numbers.sort()
        res = get_all_combinations(numbers, len(numbers) - 1, target_sum)
        res.sort()
        return res


s = Solution()

print(s.combinationSum([ 8, 10, 6, 11, 1, 16, 8 ], 28))