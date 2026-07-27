# Mock 02 — Sliding Window

## Problem
- LC 3: Longest Substring Without Repeating Characters
- Pattern: Sliding Window

## Result
- Solved with guidance
- Score: 7/10

## What worked
- Identified sliding window as correct pattern
- Understood the set-based invariant
- Completed follow-up (LC 340, K distinct chars with dict counter)

## Bugs
- First attempt used nested `for` loops (O(n^2), not sliding window)
- Used `string.size` instead of `len(string)` (C++ habit)
- Never cleared the `seen` set between iterations
- Conceptual gap: didn't initially see why `while s[right] in seen` shrinks from left

## Root cause
- Pattern recognition correct, but template not internalized
- Python API confusion (mixing C++ and Python syntax)

## Follow-up completed
- LC 340: Longest Substring with At Most K Distinct Characters
- Key insight: set -> dict counter, `del` key when count == 0
