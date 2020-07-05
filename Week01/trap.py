"""双指针"""


class Solution1:
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume


"""动态规划"""


class Solution2:
    def trap(self, height) -> int:
        if not height: return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        # 找位置i左边最大值
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])
        # 找位置i右边最大值
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])
        #print(max_left)
        #print(max_right)
        # 求结果
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        return res
# 少写一个循环
class Solution3:
    def trap(self, height) -> int:
        n = len(height)
        if n == 0: return 0
        right = [0] * n
        right[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        res = 0
        cur = height[0]
        for i in range(1, n - 1):
            cur = max(height[i], cur)
            res += min(cur, right[i]) - height[i]
        return res


"""数学解法"""


class Solution4(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # 同时从左往右和从右往左计算有效面积
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n - i - 1] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        # 积水面积 = S1 + S2 - 矩形面积 - 柱子面积
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res

"""栈"""
class Solution5:
    def trap(self, height) -> int:
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            #print(stack)
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i-stack[-1] - 1)
            stack.append(i)
        return res

nums = [0,1,0,2,1,0,1,3,2,1,2,1]

Solution5().trap(nums)