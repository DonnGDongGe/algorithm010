class Solution:
    # 双指针
    # 最小的那根柱子决定最大的面积
    def maxArea(self, height):
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
