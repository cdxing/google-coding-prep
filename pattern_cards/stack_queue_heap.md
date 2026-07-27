# Stack / Queue / Heap Pattern Card

## Valid Parentheses — Stack for Matching (LC 20)
```
Trigger:   Matching pairs, nesting validation, balanced brackets
Pattern:   Push openers onto stack; on closer, check stack top matches
Invariant: Stack always contains unmatched openers in order
Bug:       Check stack is not empty before peeking; check stack is empty at end
```

## Top K Frequent Elements — Min-Heap of Size K (LC 347)
```
Trigger:   "Top K" or "K most/least" anything
Pattern:   Count frequencies (dict), then maintain min-heap of size k
Invariant: Heap size never exceeds k; smallest freq gets popped
Bug:       Use heapq.heappush/heappop with (freq, value) tuples, not list .append/.pop
```

## Decode String — Stack as Saved Context (LC 394)
```
Trigger:   Nested structure, recursive encoding, brackets with multipliers
Pattern:   4 cases per char: digit → build number, '[' → push & reset,
           ']' → pop & combine, letter → append
Invariant: Stack stores (prev_string, multiplier) tuples
Bug:       Multi-digit numbers: current_num = 10 * current_num + int(char)
```

## Daily Temperatures — Monotonic Stack (LC 739)
```
Trigger:   "Next greater/warmer/larger element" for each position
Pattern:   Stack stores indices; while current > stack top, pop and resolve
Invariant: Stack elements are in decreasing order (monotonic decreasing)
Bug:       Use `while stack and ...` not `while stack is not []`; unresolved indices stay 0
```

## Min Stack — Parallel Min Tracking (LC 155)
```
Trigger:   Design a stack with O(1) getMin
Pattern:   Two stacks: main stack + min_stack tracking running min at each level
Invariant: min_stack[-1] is always the current minimum
Bug:       First push: no previous min to compare — handle empty min_stack case
```

## Queue using Stacks — Lazy Transfer (LC 232)
```
Trigger:   Implement FIFO using LIFO structures
Pattern:   stack_in for push, stack_out for pop/peek; transfer only when stack_out is empty
Invariant: stack_out order is correct FIFO; transferring onto non-empty stack_out breaks order
Bug:       empty() must check both stacks; use .pop() not .pop; append() not append[]
```
