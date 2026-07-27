'''
Mini Mock — Block 4 v2. Timer: 15 minutes. Sliding window approach.

  ---
  LC 209: Minimum Size Subarray Sum

  Given an array of positive integers nums and a positive integer target,
  return the minimal length of a SUBARRAY (contiguous, order preserved)
  whose sum is >= target. If there is no such subarray, return 0.

  NOTE: "subarray" = contiguous elements in original order.
        "subset"   = any elements, any order.
        This problem requires a subarray — you cannot sort or reorder.

  Example 1: target = 7, nums = [2,3,1,2,4,3] → 2
             (subarray [4,3] has sum >= 7)

  Example 2: target = 4, nums = [1,4,4]        → 1

  Example 3: target = 11, nums = [1,1,1,1,1,1,1,1] → 0

  ---
  Pattern: Sliding window (shrink when VALID to minimize)

  LC 3 comparison:
    LC 3:   while INVALID → shrink  (remove duplicates until window is clean)
    LC 209: while VALID   → shrink  (sum >= target, try smaller window)

  Code. Go.

'''
# pattern: So the pattern is that the array is all positive numbers. So you can have a monotonic increase when you add up. There's no minus number. And also, it's asking about subarray, so you want to preserve its difference. So it's fine that using sliding window.
# invariant: The invariant is that for the for loop, you expand the window, and inside using a while loop to shrink the window. So this is the common pattern invariant. Use the for loop to expand the right side, the right side of the window, and use the while loop to update the left side, the left side of the window.
# complexity: For the time complexity, it's, because it, of course, there's a while loop to go through the n numbers of the. Generally, there's this while loop to navigate this window, right, this nested. I was thinking that compared to the three sum, it's probably, probably, it's at order that the left and right are updated in the same time, right? So, at maximum, if the n is in infinity, then what's the worst case? Could be take to the max, to the degree, to the n squared. So I think the time complexity is n squared. For the space, I think it's fine. It's still in the order of constant, or one. Correct me if I'm wrong.
# correction: each element at most add once and removed once, so around 2n, operations, so O(n)

def minSubArrayLen(target, nums):
    left=0
    #min_len = len(nums) + 1
    min_len = float('inf')
    current_sum = 0
    #is_larger = False
    for right in range(len(nums)):
        current_sum += nums[right]
        if nums[right] >= target:
            return 1
        #while left < right and  current_sum >= target:
        while left <= right and  current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
            #is_larger = True


    return min_len if min_len != float('inf') else 0 #is_larger else 0 



# --- Tests ---
print(minSubArrayLen(7, [2,3,1,2,4,3]))          # 2
print(minSubArrayLen(4, [1,4,4]))                  # 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))      # 0
print(minSubArrayLen(15, [1,2,3,4,5]))             # 5
print(minSubArrayLen(3, [1,1]))                    # 0
print(minSubArrayLen(6, [3,1,1,5,1]))              # 2
