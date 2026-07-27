# LC 394 - Decode String
#
# Given an encoded string, return its decoded string.
# Rule: k[encoded_string] → repeat encoded_string k times
#
# Examples:
# "3[a]2[bc]"     → "aaabcbc"
# "3[a2[c]]"      → "accaccacc"
# "2[abc]3[cd]ef" → "abcabccdcdcdef"
#
# Approach: stack
# 4 cases per character:
#   digit  → build current number (handle multi-digit)
#   '['    → push (current_str, current_num) onto stack, reset both
#   letter → append to current_str
#   ']'    → pop (prev_str, num), current_str = prev_str + num * current_str

def decodeString(s):
    stack = []
    current_str = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char

    return current_str


print(decodeString("3[a]2[bc]"))      # aaabcbc
print(decodeString("3[a2[c]]"))       # accaccacc
print(decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
