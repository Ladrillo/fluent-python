def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1
    print(nums)
    return i



res = removeDuplicates([1, 1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 6])
print(res)
