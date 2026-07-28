'''
Timer: 15 minutes. Delayed rewrite. Closed-book.

  ---
  LC 3: Longest Substring Without Repeating Characters

  Given a string s, find the length of the longest substring without
  repeating characters.

  Example 1: s = "abcabcbb" → 3  ("abc")
  Example 2: s = "bbbbb"    → 1  ("b")
  Example 3: s = "pwwkew"   → 3  ("wke")

  ---
  Invariant: The current window contains no duplicate characters.

  Code. Go.

'''


def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0
    '''
    for right, c in enumerate(s):
        if not seen or c not in seen:
            seen.add(c)
        else:
            seen.remove(s[left])
            left = right
            seen.add(c)
        max_len = max(max_len, right - left + 1)
    '''
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
print(lengthOfLongestSubstring("a"))         # 1
print(lengthOfLongestSubstring("abcda"))     # 4
