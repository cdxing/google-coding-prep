'''
  Given an array of integers nums and an integer k, return the number of contiguous subarrays where the sum equals k.

  Example 1:
  Input:  nums = [1,1,1], k = 2
  Output: 2

  Example 2:
  Input:  nums = [1,2,3], k = 3
  Output: 2

  The array can contain negative numbers. Length up to 20,000.
'''

# 1. the array can hav nagative number, so the sum is not monotonic, not using slide window
# 2. continguous subarray make the question easier
# 3. brute force way is to loop all the the numbers and then loop again
# 4. more optimized way is to use prefix sum that to check if the current sum - k shows up in the prefix sum
from collections import defaultdict

def subarrays(nums:[], k:int):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    currentSum = 0
    output = 0

    for num in nums:
        currentSum += num
        need = currentSum - k
        output += prefix_sum[need]
        prefix_sum[currentSum] += 1

    return output

nums = [1,1,1]
k = 2
print(subarrays(nums, k))

nums = [1,2,3]
k = 3
print(subarrays(nums, k))

'''
    What if I also want to return the actual subarrays, not just the count? How would your approach change?
'''

# register the index of the prefix sums

def actual_subarrays(nums:[], k:int):
    prefix_sum = defaultdict(int)
    prefix_sum_actual = defaultdict(list)

    prefix_sum[0] = 1
    prefix_sum_actual[0] = [-1]

    currentSum = 0
    output = 0
    output_array = []

    for i, num in enumerate(nums):
        currentSum += num
        need = currentSum - k

        output += prefix_sum[need]
        if prefix_sum_actual[need]:
            #current_array = []
            #for idx in prefix_sum_actual[need]:
            #    for j in range(idx + 1, i+1):
            #        current_array.append(nums[j])
            #output_array.append(current_array)
            for start_idx in prefix_sum_actual[need]:
                output_array.append(nums[start_idx+1:i+1])
        prefix_sum[currentSum] += 1
        prefix_sum_actual[currentSum].append(i)

    return output, output_array

nums = [1,1,1]
k = 2
print(actual_subarrays(nums, k))

nums = [1,2,3]
k = 3
print(actual_subarrays(nums, k))

