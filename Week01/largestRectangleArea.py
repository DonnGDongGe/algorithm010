# 1. 暴力求解,超时
def largestRectangleArea1(heights):
    res = 0
    n = len(heights)
    for i in range(n):
        left_i = i
        right_i = i
        # 找到左边比当前位置小的柱子
        while left_i >= 0 and heights[left_i] >= heights[i]:
            left_i -= 1
        while right_i < n and heights[right_i] >= heights[i]:
            right_i += 1
        res = max(res, (right_i - left_i - 1) * heights[i])
    return res


# 2. 当我们找 i 左边第一个小于 heights[i]
# 如果 heights[i-1] >= heights[i]
# 其实就是和 heights[i-1] 左边第一个小于 heights[i-1] 一样。
# 依次类推，右边同理。


def largestRectangleArea2(heights):
    if not heights:
        return 0
    n = len(heights)
    left_i = [0] * n
    right_i = [0] * n
    left_i[0] = -1
    right_i[-1] = n
    for i in range(1, n):
        tmp = i - 1
        while tmp >= 0 and heights[tmp] >= heights[i]:
            tmp = left_i[tmp]
        left_i[i] = tmp
    for i in range(n - 2, -1, -1):
        tmp = i + 1
        while tmp < n and heights[tmp] >= heights[i]:
            tmp = right_i[tmp]
        right_i[i] = tmp
    # print(left_i)
    # print(right_i)
    res = 0
    for i in range(n):
        res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
    return res


# 栈
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res



Solution().largestRectangleArea([2,1,5,6,2,3])