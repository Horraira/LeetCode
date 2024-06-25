class Solution:
    def isPalindrome1(self, s:str) -> bool:
        n = len(s) - 1
        for i in range(len(s)//2):
            if s[i] != s[n-i]:
                return False
        return True
    def isPalindrome2(self, s:str) ->bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while r > l and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def isalnum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))