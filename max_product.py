import sys


def prod(nums):
    res = 1
    for x in nums:
        res *= x

    return res


def maxProductNZ(nums):
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 0:
        return -sys.maxsize

    rest_product = prod(nums)
    product = 1
    res = -sys.maxsize

    for x in nums:
        product *= x
        rest_product //= x

        if x < 0:
            res = max(res, product, rest_product)  # x in right
            res = max(res, product // x, rest_product * x)  # x in left
        else:
            res = max(res, product)

    return res


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -sys.maxsize
        prev_z = -1
        for i, x in enumerate(nums):
            if x == 0:
                res = max(res, maxProductNZ(nums[prev_z + 1:i]), 0)
                prev_z = i
        else:
            res = max(res, maxProductNZ(nums[prev_z + 1:]))

        return res


S = Solution()
print(S([-1,2,3,-5,-2]))



