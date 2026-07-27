# LC 347 - Top K Frequent Elements
#
# Given an integer array nums and an integer k,
# return the k most frequent elements. (any order)
#
# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Input: nums = [1], k = 1
# Output: [1]
#
# Approach: frequency count + min-heap of size k
# step 1: count frequencies with a dict
# step 2: use a min-heap to keep only the top k frequent elements
# step 3: extract elements from the heap
import heapq
from collections import defaultdict

def topKFrequent(nums, k):
    frequencies = defaultdict(int)
    topk = []

    for num in nums:
        frequencies[num] += 1
        
    for num, freq in frequencies.items():
        heapq.heappush(topk, (freq, num))
        if len(topk) > k:
            heapq.heappop(topk)

    keys = []
    for i in range(len(topk)):
        keys.append(topk[i][1])

    return keys



print(topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(topKFrequent([1], 1))             # [1]
