# LC 15 - 3Sum
#
# Given an integer array nums, return all unique triplets
# [a, b, c] such that a + b + c = 0.
#
# No duplicate triplets allowed.
#
# Example:
# Input:  [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
#
# Approach: sort + fix one number + two pointers for the remaining pair

def threeSum(nums):
    nums = sorted(nums)
    output = []
    for i, num in enumerate(nums):
        need = 0 - num
        left = i + 1
        right = len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        while left < right:
            if left != i and right != i:
                if (nums[left] + nums[right]) == need:
                    output.append([nums[left], nums[i], nums[right]])
                    while left < right and nums[left]  == nums [left + 1]:
                        left += 1
                    while left < right and nums[right]  == nums [right - 1]:
                        right -= 1
                    left +=1
                    right -=1
                elif nums[left] + nums[right] < need:
                    left += 1
                else:
                    right -= 1



                    
    return output


print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(threeSum([0, 1, 1]))               # []
print(threeSum([0, 0, 0]))               # [[0,0,0]]
