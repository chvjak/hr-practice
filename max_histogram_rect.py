class Solution:
    def largestRectangleArea0(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        N = len(heights)
        if N == 0:
            return 0

        heights.append(0)
        max_rect = 0
        prev_h_pos = {0:-1}
        prev_h = 0
        for i, h in enumerate(heights):
            if h > prev_h:
                prev_h_pos[h] = i
            elif h < prev_h:
                if h not in prev_h_pos.keys() or prev_h_pos[h] is None:
                    prev_h_pos[h] = i

                for ph, pi in prev_h_pos.items():
                    if ph > h and pi is not None:
                        rect = (i - pi) * ph
                        max_rect = max(max_rect, rect)
                        prev_h_pos[h] = min(prev_h_pos[h], pi)
                        prev_h_pos[ph] = None


            prev_h = h


        return max_rect

S = Solution()
print(S.largestRectangleArea([0]))
print(S.largestRectangleArea([2,1,2]))
print(S.largestRectangleArea([2,1,5,6,2,3]))
print(S.largestRectangleArea([1,1,1,3,3,4,4,17,1]))