from typing import List

class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

# nums = [0,0,0,1,1,1,1,2,3,3]
solution = Solution()
nums = [1,1,1,2,2,3]
print(solution.removeDuplicates(nums))
