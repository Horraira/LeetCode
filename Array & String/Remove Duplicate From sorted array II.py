from typing import List

class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        k = 2
        for i in range(2, len(nums)):
            if k == 1 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

nums = [0,0,0,1,1,1,1,2,3,3]
solution = Solution()
print(solution.removeDuplicates(nums))
