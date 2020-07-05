# 暴力法
"""
最简单直接的方法是遍历每个滑动窗口，找到每个窗口的最大值。
一共有 N - k + 1 个滑动窗口，每个有 k 个元素，
于是算法的时间复杂度为 O(Nk)，表现较差。
时间复杂度：
O(Nk)。其中 N 为数组中元素个数。
空间复杂度：
O(N−k+1)，用于输出数组。
"""


class Solution1:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]


Solution1().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
"""
双向队列
"""
from collections import deque


class Solution2:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

Solution2().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)

def maxSlidingWindow(nums, k):
    d = deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out

maxSlidingWindow([1, 2, 3, -3, 5, 3, 6, 7], 3)

"""动态规划"""
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
            
        return output
