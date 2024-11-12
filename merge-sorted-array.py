danumz1 = [1, 2, 3, 0, 0, 0]
danumz2 = [2, 5, 6]


def merge(nums1, m, nums2, n):
    arr1 = nums1[:m]
    arr2 = nums2
    result = []

    for i in range(m + n):
        if len(arr1) > 0 and len(arr2) > 0:
            arr = arr1 if arr1[0] <= arr2[0] else arr2
            result.append(arr.pop(0))
        if len(arr1) == 0 and len(arr2) > 0:
            result.append(arr2.pop(0))
        if len(arr2) == 0 and len(arr1) > 0:
            result.append(arr1.pop(0))

    nums1.clear()
    nums1.extend(result)
    print(nums1)


merge(danumz1, 3, danumz2, 3)

# print(danumz)
