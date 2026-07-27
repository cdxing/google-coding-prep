# LC 33 - Search in Rotated Sorted Array
#
# A sorted array is rotated at some unknown pivot.
# Given target, return its index, or -1 if not found.
# Must run in O(log n).
#
# Example:
# Input:  nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Key insight: at every step of binary search,
# one half of the array is always sorted.
# Determine which half is sorted, then check
# if target falls within that sorted range.

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]: # left is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1 # target in the left sorted half
            else:
                left = mid + 1 # target is in the right half
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1 # target at right sorted half
            else:
                right = mid - 1 # target is in the left half
    return -1


print(search([4,5,6,7,0,1,2], 0))   # 4
print(search([4,5,6,7,0,1,2], 3))   # -1
print(search([1], 0))                # -1
print(search([1], 1))                # 0
print(search([3,1], 1))              # 1
