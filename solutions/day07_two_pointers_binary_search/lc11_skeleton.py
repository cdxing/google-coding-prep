# LC 11 - Container With Most Water
#
# Given n vertical lines with heights h[i],
# find two lines forming a container that holds the most water.
#
# Area = min(h[left], h[right]) × (right - left)
#
# Example:
# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Approach: two pointers, move the shorter side inward

def maxArea(height):
    # YOUR CODE HERE
    left  = 0
    right = len(height) - 1
    output = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        output = max(area, output)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return output



print(maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(maxArea([1,1]))                  # 1
print(maxArea([4,3,2,1,4]))            # 16
print(maxArea([1,2,1]))                # 2
