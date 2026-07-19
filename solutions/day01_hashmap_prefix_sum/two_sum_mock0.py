def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]

        seen[num] = i

    return []

tests = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 2, 3], 10),
    ([], 1),
]

for nums, target in tests:
    print(nums, target, "->", two_sum(nums, target))

def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) -1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] > target:
            right = right -1
        else:
            left = left + 1
    return []

tests = [
    ([2, 7, 11, 15], 9),
    ([2, 3, 4], 6),
    ([3, 3], 6),
    ([1, 2, 3], 10),
    ([], 1),
]
for nums, target in tests:
    print("two sum sorted", nums, target, "->", two_sum_sorted(nums, target))
