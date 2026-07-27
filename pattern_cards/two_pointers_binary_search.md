# Two Pointers / Binary Search Pattern Card

## 3Sum — Sort + Fix One + Two Pointers (LC 15)
```
Trigger:   "Find all triplets that sum to X", no duplicates
Pattern:   Sort array. Fix nums[i], then two pointers (left=i+1, right=end) for remaining pair
Invariant: Outer loop skips duplicate nums[i]; inner while-loops skip duplicate left/right after match
Bug:       left starts at i+1 not 0; right decrements not increments; append values not indices
```

## Container With Most Water — Greedy Two Pointers (LC 11)
```
Trigger:   Max area between two lines, width × min height
Pattern:   left=0, right=end. Area = min(h[l],h[r]) × (r-l). Move the shorter side inward
Invariant: Moving shorter side is the only way to potentially increase area
Bug:       Use min(h[l],h[r]) not max; move shorter not taller
```

## Search in Rotated Sorted Array — Modified Binary Search (LC 33)
```
Trigger:   Sorted array rotated at unknown pivot, find target in O(log n)
Pattern:   Binary search. At each step: (1) found? (2) which half is sorted? (3) is target in sorted half?
Invariant: One half is ALWAYS sorted; only do range check on the sorted half
Bug:       Use <= not < for both while loop (left <= right) and sorted check (nums[left] <= nums[mid])
```

## General Binary Search Boundary Checklist
```
1. while left <= right  (not <, unless you want to miss left==right)
2. nums[left] <= nums[mid]  (not <, handles 2-element subarrays)
3. Target range checks use <= on inclusive side, < on exclusive side
4. Return -1 after loop if not found
```
