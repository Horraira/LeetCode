from typing import List

class Solution:
    def canJump(self, nums:List[int]) -> bool:
        goal = len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


nums = [3,2,1,0,4]
solution = Solution()
print(solution.canJump(nums))