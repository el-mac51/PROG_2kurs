def sums(nums, trgt):
    num = {}
    for i in range(len(nums)):
        current = nums[i]
        comple = trgt - current
        if comple in num:
            return [num[comple], i]
        num[current] = i
    return
nums = [2,7,11,15]
target = 9

print(sums(nums, target))
