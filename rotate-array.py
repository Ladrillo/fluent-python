def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[0:-k]

rotate([1, 2, 3, 4, 5, 6, 7], 3)
