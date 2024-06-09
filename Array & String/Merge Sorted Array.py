from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n]
            n, last = n-1, last-1

        return nums1

solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(solution.merge(nums1,m,nums2,n))