from typing import List

class Solution:
    def rotate(self, nums:List[int], k: int) -> int:
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r -1

        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r = l+1, r-1
        return nums

nums = [1,2,3,4,5,6,7]
solution = Solution()
print(solution.rotate(nums,2))