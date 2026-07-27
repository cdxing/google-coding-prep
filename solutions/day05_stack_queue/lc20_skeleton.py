# LC 20 - Valid Parentheses
#
# Given a string containing just '(', ')', '{', '}', '[', ']',
# determine if the input string is valid.
#
# Rules:
# - Open brackets must be closed by the same type
# - Open brackets must be closed in the correct order
# - Every close bracket has a corresponding open bracket
#
# Examples:
# "({[]})" -> True
# "({[}])" -> False
# "("      -> False
# "()"     -> True

def isValid(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in match:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()

        else: 
            stack.append(char)
    return len(stack) == 0

print(isValid("({[]})"))   # True
print(isValid("({[}])"))   # False
print(isValid("("))         # False
print(isValid("()"))        # True
