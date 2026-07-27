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
# Approach: stack, 4 cases: digit, '[', ']', letter

def decodeString(s):
    stack = [] 
    current_number = 0
    current_string = ""
    #output = ""
    for c in s:
        if c.isdigit():
            current_number = 10 * current_number + int(c)
        elif c == "[":
            
            stack.append((current_string, current_number))
            current_number = 0
            current_string = ""
        elif c == "]":
            prev_s, prev_n = stack.pop()
            current_string = prev_s + prev_n * current_string
        else:
            current_string += c
    return current_string




print(decodeString("3[a]2[bc]"))      # aaabcbc
print(decodeString("3[a2[c]]"))       # accaccacc
print(decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
