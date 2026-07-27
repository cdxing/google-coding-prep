'''  
Timer: 45 minutes. Start now.

  ---
  LC 215: Kth Largest Element in an Array

  Given an integer array nums and an integer k, return the kth largest element in the array.

  Note: it is the kth largest element in sorted order, not the kth distinct element.

  Example 1: nums = [3,2,1,5,6,4], k = 2  → 5
  Example 2: nums = [3,2,3,1,2,4,5,5,6], k = 4  → 4

  Constraints:
  - 1 <= k <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4

  ---
  Before you code, say out loud (write in comments):
  1. Clarify the problem in your own words
  2. Baseline approach and its complexity
  3. Pattern you'll use and why
  4. The invariant

  Then code. Go.

'''
# sorted the array
# kth largest then pick the order as the largest in the sorted array like array[k]
# return the kth largest number
'''
def kth_largest(nums, k):
    nums = sorted(nums, reverse = True)
    return nums[k-1]
'''

# xfrom collections import heapq
import heapq
def kth_largest(nums, k):
    # loop through the nums
    # as the loop throgh, add to the heapq 
    # keep the kth largest in the heap, if the len() of the heap is larger than k, pop out the element

    topk = []

    for num in nums:
        heapq.heappush(topk, num)

        if len(topk) > k:
            heapq.heappop(topk)

    #return heapq.heappop(topk)
    return topk[0]




nums = [3,2,1,5,6,4]
k = 2
print(kth_largest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kth_largest(nums, k))

# ============================================================
# PATTERN CARD — Heap / Top-K
# ============================================================
#
# Trigger:   "kth largest/smallest", "top k", "k most frequent"
# Invariant: min-heap of size k holds the k largest seen so far;
#            heap top (smallest of k) = kth largest
# Bug:       Python heapq is min-heap; for kth smallest use max-heap
#            (push -val). Don't forget: import heapq (not from collections)
#
# Template:
#   heap = []
#   for item in stream:
#       heapq.heappush(heap, item)
#       if len(heap) > k:
#           heapq.heappop(heap)
#   return heap[0]
#
# Complexity: O(n log k) time, O(k) space
#
# Baseline:  sort → index, O(n log n). Heap wins when k << n.
#
# Follow-up variants:
#   - Kth smallest: use max-heap (push -val, return -heap[0])
#   - Top-K frequent: count with dict, then heap on counts
#   - Streaming data: same template, heap stays size k
# ============================================================

