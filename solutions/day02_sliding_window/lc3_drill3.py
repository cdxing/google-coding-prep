'''
Timer: 10 minutes. Final rewrite. Closed-book.

  LC 3: Longest Substring Without Repeating Characters

  Template to nail:
    for right:          expand
        while INVALID:  shrink (remove s[left], then left += 1)
        add s[right]
        update answer

  Code. Go.
'''


def lengthOfLongestSubstring(s):
    # slide window
    left = 0 
    seen = set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# --- Tests ---
print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))     # 1
print(lengthOfLongestSubstring("pwwkew"))    # 3
print(lengthOfLongestSubstring(""))          # 0
print(lengthOfLongestSubstring("abcbda"))    # 4
