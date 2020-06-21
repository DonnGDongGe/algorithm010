class Solution(object):
    # 暴力求解,时间复杂度O(n^2),空间复杂度O(1)
    def twoSum1(self, nums, target):
        for index1, value in enumerate(nums):
            for index2, value2 in enumerate(nums):
                answer = value1 + value2
                if target == answer:
                    if index1 == index2:
                        continue
                    return [index1, index2]



    # 使用哈希表，时间空间复杂度都为O(n)
    def twoSum2(self, nums, target):
        hasmap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in hasmap:
                return [hasmap.get(diff), i]
            hasmap[value] = i
    
