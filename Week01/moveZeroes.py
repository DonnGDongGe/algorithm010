class Solution:
    # 循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素
    # index 为慢指针 指向最新一个0元素的位置
    # 时间复杂度O(n)   空间复杂度O(1)
    def moveZeroes(self, nums):
        zero = 0
        for index, value in enumerate(nums):
            if nums[index] != 0:
                nums[index], nums[zero] = nums[zero] + nums[index]
                zero +=1
        return nums
                
