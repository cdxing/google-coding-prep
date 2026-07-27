'''
Timer: 15 minutes. Delayed rewrite. Closed-book.

  ---
  LC 15: 3Sum

  Given an integer array nums, return all the triplets
  [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k,
  and nums[i] + nums[j] + nums[k] == 0.

  The solution set must not contain duplicate triplets.

  Example 1: nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
  Example 2: nums = [0,1,1]          → []
  Example 3: nums = [0,0,0]          → [[0,0,0]]

  ---
  Write:
  1. Pattern
  2. Key steps
  3. Complexity

  Then code. Go.

'''

# 1. Pattern:
# So the key step is the pattern is find a three sum, right? To find a target number in three components can make up that sum. And you want to remove the duplications. So there's a couple of steps, different layers of steps, remove the duplications.
# 2. Key steps:
# The key steps are, first, you loop over the list, list of numbers. And then you have a, for the rest of the, use the two pointers, left side and right side, and while the left is smaller than the right, you check the sum of the index, left and right together. And before that, you want to sort the array, sort of the array. After sorting the array, so you can skip the duplicated parts, right? So, suppose the first number is like, minus, you don't want to have like three minus, right? You want to... You don't want to have too many duplications, so, when the current index number is the same as the last one, you want to continue to move to the next one.
# 3. Complexity:
# For the complexity for the time-wise because you need to store the list. So it's at least the n log n. And for the for loop, it's also each other at the time. So the time complexity overall dominates the process of n log n. And for the time space complexity, it's at order one, constant. but by the end of the day the time complexity is dominiated by O(n^2), one n is for the for loop and another n is for the while loop of left and right



def threeSum(nums):
    nums.sort()
    output = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                output.append([nums[i] , nums[left] , nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return output





# --- Tests ---
print(threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,1,1]))            # []
print(threeSum([0,0,0]))            # [[0,0,0]]
print(threeSum([-2,0,1,1,2]))       # [[-2,0,2],[-2,1,1]]
