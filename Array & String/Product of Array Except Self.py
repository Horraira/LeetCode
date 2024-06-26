from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in nums]
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1 ):
            res[i] = postfix * res[i]
            postfix *= nums[i]
        return res

solution = Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))