"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        pal = 0
        number = x
        while number > 0:
            digit = number % 10
            pal = pal * 10 + digit
            number = number // 10
        return (x == pal)