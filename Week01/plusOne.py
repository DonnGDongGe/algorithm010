class Solution(object):
    def plusOne(self, digits):
        sums = 0
        for i in digits:
            sums = sums * 10 + i  #10进制乘以10，进行累积和；
        sums_str = str(sums + 1)
        return map(int, list(sums_str))


class Solution2(object):
    def plusOne(self, digits):
        # 从最低位开始做加法运算
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        ans = [0] * (len(digits) + 1)
        ans[0] = 1
        return ans


def plusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits) - 1 - i))
    return [int(i) for i in str(num + 1)]
