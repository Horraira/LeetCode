class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {')':'(',
                          '}':'{',
                          ']':'[',}
        stack = []
        for char in s:
            if s in parenthesesMap:
                element = stack.pop() if stack else '@'
                if element != parenthesesMap[s]:
                    return False
            else:
                stack.append(char)
        return not stack

solution = Solution()
s = "(]"
print(solution.isValid(s))