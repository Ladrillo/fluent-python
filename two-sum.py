nums = [3, 2, 4]
target = 6

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in hashmap:
            return [hashmap[needed], i]
        hashmap[num] = i

print(twoSum(nums, target))
