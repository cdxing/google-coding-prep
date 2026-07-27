# LC 33 - Search in Rotated Sorted Array (blind rewrite)
#
# Sorted array rotated at unknown pivot. Find target index or -1.
# O(log n).
#
# Example:
# Input:  nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Hint: one half is always sorted.

def search(nums, target):
    # YOUR CODE HERE
    left = 0
    right = len(nums) - 1
    mid = (left + right ) // 2
    output = -1

    # key is when divid to left half and right half, there's defenitely one half is monotonic, check if the target is in that half or not, if not divide the other half and check again
    while left <= right:
        if nums[mid] == target:
            return mid
        # check if the left half is monitonic or not:
        if nums[left] <= nums[mid]: # left half is monotonic
            # check if the target is in this half or not
            if nums[left] <= target and target < nums[mid]:
                # move right to the mid
                right = mid
                mid = (left + right ) // 2
            else: #
                left = mid + 1
                mid = (left + right ) // 2

        else: # right half is monotonic
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
                mid = (left + right ) // 2
            else: 
                right = mid
                mid = (left + right ) // 2

    return  output

print(search([4,5,6,7,0,1,2], 0))   # 4
print(search([4,5,6,7,0,1,2], 3))   # -1
print(search([1], 0))                # -1
print(search([1], 1))                # 0
print(search([3,1], 1))              # 1
