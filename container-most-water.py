class Solution:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1
        while j > i:
            area = min(height[j], height[i]) * (j - i)
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


sol = Solution()

test_height_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test_height_2 = [1, 1]

print(sol.maxArea(test_height_1))
print(sol.maxArea(test_height_2))
