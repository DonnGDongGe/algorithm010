# 拿数组里的第一个数字和后面的数字分别相加，
# 看是否等于target；如果不等于target，
# 那么就继续拿数组里的第二个数字和后面的数字相加；
# 不停的去一个个试...直到等于target，
# 返回这2个数字所在的下标

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)  # 获取nums的长度，是4
        for x in range(n):  # 外层循环先取出下标0，对应着数组里的第一个数字
            for y in range(x + 1, n):  # 内层循环取出下标1，对应着数组里的第二个数字
                if nums[x] + nums[y] == target:  # 如果第一个数字+第二个数字=target
                    return x, y  # 上面的判断是对的话，那么就返回下标
                    break  # 并停止程序
                else:  # 如果上面的条件不满足的话，内层for循环就会继续取出下标2进行判断...如果都不满足，那么外层for循环就会取出下标1...依次类推
                    continue


def twoSum1(nums, target):
    map = {}
    for index, value in enumerate(nums):
        if nums[index] not in map:
            map[target - nums[index]] = index
        else:
            return map[nums[index]], index
    return -1, -1


answer = twoSum1([2, 7, 11, 15], 9)
print(answer)