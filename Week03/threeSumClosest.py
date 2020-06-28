def threeSumClosest(num, target):
    num.sort()
    result = num[0] + num[1] + num[2]
    for i in range(len(num) - 2):
        # 保证不重复计算
        if i > 0 and num[i] == num[i - 1]:
            continue
        j, k = i + 1, len(num) - 1
        while j < k:
            sum = num[i] + num[j] + num[k]
            if sum == target:
                return sum
            # 差值小的作为结果
            if abs(sum - target) < abs(result - target):
                result = sum
            # 如果和<目标值，则说明做指针较大
            if sum < target:
                j += 1
            # 如果和>目标值，则说明右指针较大
            elif sum > target:
                k -= 1

    return result


threeSumClosest([1, 2, 3, 4], 4)


def threeSumClosest(num, target):
    num.sort()
    result = num[0] + num[1] + num[2]
    for i in range(len(num)):
        if i > 0 and num[i] == num[i - 1]:
            continue
        j, k = i + 1, len(num) - 1
        while j < k:
            sum = num[i] + num[j] + num[k]
            if sum == target:
                return sum
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
        return result