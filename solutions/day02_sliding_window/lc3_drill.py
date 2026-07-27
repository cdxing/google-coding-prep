'''
Timer: 15 minutes. Closed-book rewrite.

  ---
  LC 3: Longest Substring Without Repeating Characters

  Given a string s, find the length of the longest substring without
  repeating characters.

  Example 1: s = "abcabcbb" → 3  ("abc")
  Example 2: s = "bbbbb"    → 1  ("b")
  Example 3: s = "pwwkew"   → 3  ("wke")

  Constraints:
  - 0 <= s.length <= 5 * 10^4
  - s consists of English letters, digits, symbols, spaces

  ---
  Write:
  1. Pattern
  2. Invariant
  3. Complexity

  Then code. Go.

'''

# 1. Pattern:
# The panel is more remember largest industry and this subset, the sequence, there must be order of the same stream or the same aggregation, we will have the same order.
# 2. Invariant:
# So the situation is that you need to get, oftentimes, the pattern is that you have a subtree, that is older, is the original tree, you can't use a sliding window, you move the left and right, and update the left to extend and strengthen the edges of the subtree. So you can get that. So the pattern to update left and right, always larger than left.
# 3. Complexity:
# Complexity, so the subtree for the space complexity with the order of n. And for the time complexity, it's also an order of n because it goes through all the, each and every characters of the string.


def lengthOfLongestSubstring(s):
    left = 0
    seen = set()
    max_len = 0

    '''
    for right in range(0, len(s)):
        if s[right] in seen:
            left = right
        else:
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
    '''
    for right in range(0, len(s)):
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
