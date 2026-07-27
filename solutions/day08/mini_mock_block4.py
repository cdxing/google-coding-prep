'''
Mini Mock — Block 4. Timer: 25 minutes. Full interview flow.

  ---
  LC 209: Minimum Size Subarray Sum

  Given an array of positive integers nums and a positive integer target,
  return the minimal length of a subarray whose sum is greater than or
  equal to target. If there is no such subarray, return 0.

  Example 1: target = 7, nums = [2,3,1,2,4,3] → 2
             (subarray [4,3] has sum >= 7)

  Example 2: target = 4, nums = [1,4,4]        → 1

  Example 3: target = 11, nums = [1,1,1,1,1,1,1,1] → 0

  Constraints:
  - 1 <= target <= 10^9
  - 1 <= nums.length <= 10^5
  - 1 <= nums[i] <= 10^4

  ---
  Full interview flow:
  1. Clarify the problem
  A: So this question is asking about, given a list of numbers and given a target number, to see if the, make the sum of the subarrays of this array of numbers, what's the least number of, the fewer is number of items in this subarray to make the sum larger or equal to the target.
  2. State baseline approach + complexity
  A: The baseline brute force way, and try out each and every combination to, like, balance some from the first one, then the second one, and down, right. And this, so it needs to, first the loop, loop is for. Then have one loop and have a register this sum, right. And it needs to count how many numbers, how many numbers it will use from the original. This is the brute force way. And so the time complexity would be, because it needs a container to, able to revisit, right, how many numbers it used. So the time complexity is at order of n, and the space complexity then order, that's the current way that I thought. Could be more complicated than that.
  3. State optimized approach + complexity
  A: Optimize the way I was thinking sorts the array. Then it added the time complexity and the order, I was thinking if it's worth it. But this way is more straightforward. So if we sort it in a reverse order, then we can count it from the largest number, and then add up. Once one condition fulfills the results, then that's the minimum steps you need to take, right? So it's very straightforward and easy to code.

  4. Code it
  5. Walk through a test case
  6. State final complexity
  7. Handle follow-up if asked

  Go.

'''


def minSubArrayLen(target, nums):
    nums = sorted(nums, reverse=True)
    current_sum = 0
    count = 0
    is_larger = False
    for num in nums:
        current_sum  += num
        count += 1
        if current_sum >= target:
            is_larger = True
            break
    return count if is_larger == True else 0


# --- Tests ---
print(minSubArrayLen(7, [2,3,1,2,4,3]))          # 2
print(minSubArrayLen(4, [1,4,4]))                  # 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))      # 0
print(minSubArrayLen(15, [1,2,3,4,5]))             # 5
print(minSubArrayLen(3, [1,1]))                    # 0

