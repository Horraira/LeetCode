from typing import List

class Solution:
    def jump(self, nums:List[int]) -> int:
        jump = 0
        l = r = 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l,r+1):
                furthest = max(furthest, i + nums[i])
            jump += 1
            l = r + 1
            r = furthest
        return jump


solution = Solution()
nums = [2,3,1,1,4]
print(solution.jump(nums))