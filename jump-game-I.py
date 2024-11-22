class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        farthest_reach = 0
        for i in range(0, len(nums)):
            if i > farthest_reach:
                return False
            current_reach = i + nums[i]
            print(f"from idx {i} I can reach idx {current_reach}")
            farthest_reach = max(farthest_reach, current_reach)
            if farthest_reach >= len(nums) - 1:
                return True
        return False


sol = Solution()
test_nums_1 = [2, 3, 1, 1, 4]
test_nums_2 = [3, 2, 1, 0, 4]
print(sol.canJump(test_nums_1))
