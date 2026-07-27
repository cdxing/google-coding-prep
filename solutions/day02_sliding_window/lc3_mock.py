'''
  Timer: 45 minutes. Start now.

  LC 3: Longest Substring Without Repeating Characters

  Given a string s, find the length of the longest substring without repeating characters.

  Example 1: s = "abcabcbb" → 3  ("abc")
  Example 2: s = "bbbbb"    → 1  ("b")
  Example 3: s = "pwwkew"   → 3  ("wke")

  Constraints:
  - 0 <= s.length <= 5 * 10^4
  - s consists of English letters, digits, symbols, spaces

  ---
  Start with clarification, then baseline, then pattern. Go.

'''

# sliding window
# this question can us the sliding windiw
# for left in the range)
# the idea is using sliding window and the get the meximum length about of the window
# 

def sliding_window(s):
    left = 0
    seen = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left +1)
        
    return max_len





s = "abcabcbb"
print(sliding_window(s))
s = "bbbbb"
print(sliding_window(s))
s = "pwwkew"
print(sliding_window(s))
s = ""
print(sliding_window(s))
s = "a"
print(sliding_window(s))


# ============================================================
# FOLLOW-UP: Longest Substring with At Most K Distinct Characters (LC 340)
# ============================================================
#
# Given a string s and integer k, find the length of the longest
# substring that contains at most k distinct characters.
#
# Example 1: s = "eceba", k = 2  → 3  ("ece")
# Example 2: s = "aa", k = 1     → 2  ("aa")
# Example 3: s = "aabacbebebe", k = 3 → 7 ("cbebebe")
#
# Key difference from LC3:
#   - set() only tracks presence — can't tell when a char fully leaves
#   - use dict {char: count} so you can delete when count hits 0
#
# Pattern card:
#   Trigger:   "longest/shortest substring with condition on distinct chars"
#   Invariant: window [left, right] has <= k distinct chars; shrink left when violated
#   Bug:       use dict counter, not set; del key when count == 0
#

def longest_k_distinct(s, k):
    left = 0
    count = {}  # char -> frequency in current window
    max_len = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len


# --- Tests ---
print(longest_k_distinct("eceba", 2))       # 3
print(longest_k_distinct("aa", 1))           # 2
print(longest_k_distinct("aabacbebebe", 3))  # 7
print(longest_k_distinct("", 2))             # 0
print(longest_k_distinct("a", 0))            # 0
