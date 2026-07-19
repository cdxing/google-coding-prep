# Pattern Card — Prefix Sum + HashMap

## Problem Family

**Subarray Sum Equals K**

Given an integer array `nums` and an integer `k`, return the number of continuous subarrays whose sum equals `k`.

Important wording:

- `subarray` means continuous.
- It is not a subset or arbitrary combination.
- `nums` may contain negative numbers, so sliding window is not always safe.

---

## Core Pattern

Convert:

```text
subarray sum = k
```

into:

```text
current_prefix_sum - previous_prefix_sum = k
```

Therefore:

```text
previous_prefix_sum = current_prefix_sum - k
```

At each index, ask:

```text
How many previous prefix sums equal current_sum - k?
```

Use a hash map to store:

```python
prefix_count[prefix_sum] = frequency_seen_so_far
```

---

## Why Not Sliding Window?

Sliding window relies on monotonic behavior:

```text
expand window -> sum increases
shrink window -> sum decreases
```

This only works reliably when all numbers are non-negative.

If negative numbers exist, expanding the window can decrease the sum, and shrinking can increase it. So use prefix sum + hash map instead.

---

## Algorithm

1. Initialize:

```python
prefix_count = {0: 1}
current_sum = 0
count = 0
```

`{0: 1}` means before reading any numbers, prefix sum `0` has appeared once. This allows subarrays starting at index `0` to be counted.

2. For each `num` in `nums`:

```text
current_sum += num
previous_sum = current_sum - k
count += prefix_count[previous_sum]
prefix_count[current_sum] += 1
```

3. Return `count`.

Key order:

```text
First check previous_sum.
Then record current_sum.
```

If you update first, especially when `k = 0`, you may accidentally count an empty subarray.

---

## Python Code

```python
def subarray_sum(nums: list[int], k: int) -> int:
    prefix_count = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        previous_sum = current_sum - k
        if previous_sum in prefix_count:
            count += prefix_count[previous_sum]

        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count
```

---

## Tests

```python
print(subarray_sum([1, 1, 1], 2))      # 2
print(subarray_sum([1, 2, 3], 3))      # 2
print(subarray_sum([1, -1, 0], 0))     # 3
print(subarray_sum([0, 0], 0))         # 3
print(subarray_sum([], 0))             # 0
print(subarray_sum([3], 3))            # 1
print(subarray_sum([-1, -1, 1], 0))    # 1
```

---

## Complexity

```text
Time:  O(n)
Space: O(n)
```

Each number is processed once, and each hash map lookup/update is average O(1).

---

## 60-Second Interview Explanation

```text
I’ll first clarify that we are counting continuous subarrays, not arbitrary subsets, and nums may contain negative numbers. Because of negative numbers, sliding window is not reliable here.

The brute-force solution is to enumerate every start and end index and compute the sum, which takes O(n^2).

To optimize, I use prefix sums. At any position, current_sum is the sum from the beginning to the current index. If a previous prefix sum satisfies current_sum - previous_sum = k, then the subarray between that previous position and the current index sums to k. So previous_sum = current_sum - k.

I keep a hash map from prefix sum to frequency. For each number, I update current_sum, check how many times current_sum - k has appeared before, add that frequency to the answer, and then record current_sum.

I initialize the map with {0: 1} so subarrays starting at index 0 are counted correctly.

Time complexity is O(n), and space complexity is O(n).
```

---

## Common Mistakes

1. Saying `subset` or `combination` instead of `continuous subarray`.
2. Using sliding window when negative numbers are allowed.
3. Writing `k - current_sum` instead of `current_sum - k`.
4. Forgetting `prefix_count = {0: 1}`.
5. Updating `prefix_count[current_sum]` before checking `current_sum - k`.
6. Writing `prefix_count[current_sum] += 1` when the key may not exist.

Correct update:

```python
prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
```

---

## Tomorrow Morning Reproduction Drill

Without looking at the answer:

1. Explain why sliding window fails with negative numbers.
2. Derive:

```text
previous_sum = current_sum - k
```

3. Write the function from memory.
4. Run the four core tests:

```python
[1, 1, 1], k = 2
[1, 2, 3], k = 3
[1, -1, 0], k = 0
[0, 0], k = 0
```

5. Say the 60-second explanation out loud once.

---

## One-Line Memory Hook

```text
For each current_sum, count how many previous sums equal current_sum - k.
```
