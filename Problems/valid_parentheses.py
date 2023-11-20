"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(string):
    # pair of open and close brackets
    # open_close = {'(': ')', '{': '}', '[': ']'}
    open_close = dict(('()', '[]', '{}'))
    stack = []
    for char in string:
        if char in '({[':
            stack.append(char)
        # elif char == ')' and stack and stack[-1] == '(' or char == '}' and stack and stack[-1] == '{' or char == ']' and stack and stack[-1] == '[' :
        #     stack.pop()
        # elif len(stack) > 0 and open_close[stack.pop()] == char:
        #     continue
        elif len(stack) == 0 or open_close[stack.pop()] != char:
            return False
    return len(stack) == 0

print(isValid('()'))