'''
Timer: 15 minutes. Closed-book rewrite.

  ---
  LC 215: Kth Largest Element in an Array

  Given an integer array nums and an integer k, return the kth largest
  element in the array.

  Note: it is the kth largest element in sorted order, not the kth
  distinct element.

  Example 1: nums = [3,2,1,5,6,4], k = 2  → 5
  Example 2: nums = [3,2,3,1,2,4,5,5,6], k = 4  → 4

  Constraints:
  - 1 <= k <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4

  ---
  Write:
  1. Pattern
  2. Invariant
  3. Complexity

  Then code. Go.

'''

# 1. Pattern:
# Top K, this pattern is like, you want the top k elements, biggest, largest, smallest, and you use a stack to help to do that. So you keep the top k, and you use a minimum stack where the size, the length, larger than k, you pop out the top element, which is the smallest element in this stack.
# 2. Invariant:
# For the invariant part, I think that's the common pattern for this one. So, you got a situation of a scenario that you want to have the top k elements on something. So, you need a container to constantly update when the, if the size is over the k, right? So, you can check the elements.
# 3. Complexity:
# That thinging part. So if we use a stack, right, the space is at order of n. For the time, I think it's also at the order of n, O(n). Correct me if I'm wrong.

#import heap
import heapq

def kth_largest(nums, k):
    topk = []
    #topk = stack()

    for num in nums:
        '''
        if len(topk) < k:
            #topk.append(num)
            #heapq.heapappend(topk, num)
            heapq.heappush(topk, num)
        #if num > topk.top():
        if num > topk[0]:
            #topk.pop()
            heapq.heappop(topk)
            #heapq.heapappend(topk, num)
            heapq.heappush(topk, num)
            #topk.append(num)
        '''
        heapq.heappush(topk, num)
        if len(topk) > k:
            heapq.heappop(topk)


    #return topk.top()
    return topk[0]





# --- Tests ---
print(kth_largest([3,2,1,5,6,4], 2))        # 5
print(kth_largest([3,2,3,1,2,4,5,5,6], 4))  # 4
print(kth_largest([1], 1))                   # 1
print(kth_largest([7,7,7], 2))               # 7
