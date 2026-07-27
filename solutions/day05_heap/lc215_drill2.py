'''
Timer: 10 minutes. Delayed rewrite. Closed-book.

  ---
  LC 215: Kth Largest Element in an Array

  Given an integer array nums and an integer k, return the kth largest
  element in the array.

  Example 1: nums = [3,2,1,5,6,4], k = 2  → 5
  Example 2: nums = [3,2,3,1,2,4,5,5,6], k = 4  → 4

  ---
  Target: zero API bugs. 10 minutes.

  Reminder — heapq API:
    heappush(heap, val)
    heappop(heap)
    heap[0]

  Code. Go.

'''

import heapq

def kth_largest(nums, k):
    topk = []
    for num in nums:
        heapq.heappush(topk, num)
        if len(topk) > k:
            heapq.heappop(topk)
    return topk[0]

    #pass




# --- Tests ---
print(kth_largest([3,2,1,5,6,4], 2))        # 5
print(kth_largest([3,2,3,1,2,4,5,5,6], 4))  # 4
print(kth_largest([1], 1))                   # 1
print(kth_largest([7,7,7], 2))               # 7
