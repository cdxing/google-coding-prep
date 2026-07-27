'''
Timer: 20 minutes. Closed-book.

  ---
  LC 15: 3Sum

  Given an integer array nums, return all the triplets
  [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k,
  and nums[i] + nums[j] + nums[k] == 0.

  The solution set must not contain duplicate triplets.

  Example 1: nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
  Example 2: nums = [0,1,1]          → []
  Example 3: nums = [0,0,0]          → [[0,0,0]]

  Constraints:
  - 3 <= nums.length <= 3000
  - -10^5 <= nums[i] <= 10^5

  ---
  Write:
  1. Pattern
  2. Invariant
  3. Complexity

  Then code. Go.

'''

# 1. Pattern:
# So, the pattern for this three sum is that you have three different elements that i doesn't equal to j, doesn't equal to k, that sum to certain target number. This case is zero. So you want to transfer it into a two-sum question, which is first, use the target number minus the one object in this list of numbers, and then the rest of it part, you use the rest two number to make up that target. So how to do that? So for example, for when you move over the first number, you need the target number minus that first number i, let's say. Then transfer it into a two-sum question.
# 2. Invariant:
# The environment for this pattern here is the prefix sum, the transfer it, which is also the core for the two sum question. Prefix sum, you, for each step, you register the sum from the head, from the start to the current point. What is the value of this sum? And put it into a hash map, where you record, like, how many times it happens, or in this case, it's the location of that prefix sum happens. What's the end of this prefix sum, the location? So that later you can retrieve that number using that index. So this map from the prefix sum to the index.
# 3. Complexity:
# The complexity, I think for the space, which is dominated by this half, then it's at an order of n. And for the time complexity, this is mainly dominated by the for loop, going through the for loop of this list. So I think at order of n. But I'll check if there's other process that are dominating this time complexity. I want one thing to sort the list so that the things don't go to be like duplicates. Sometimes you append the answer, then later, you also have a similar answer. So, we want to sort the initial list, so that this time complexity will be at order n log n. Wait a minute. So, this case, from threesum to twosum, right? I actually don't need to prefix. So, after you transfer or convert threesum to twosum, just you have a target, right? Then you have the need, so that you can move along the, just move along to find the combination of the two that can make the target. So, actually don't need the prefix. Prefix sum is a map of where, location of the, all the sums have the previous elements. So, here, for the threesum case, you don't actually need to, like sum up all the numbers that show up before.



def threeSum(nums):
    output = []
    prefix_sum = {}
    current_sum = 0
    '''
    for i, num in enumerate(nums):
        current_sum += num
        prefix_sum[current_sum].append(i)
        need = 0 - num

        for j, num_j in enumerate(nums):
            need_j = need - 
        if need in prefix_sum:
            output.append()
    nums = sorted(nums)

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            target = 0 - nums[i]
            need = target - nums[j]
            for k in range(j+1, len(nums)):
                if nums[k] == need:
                    output.append([nums[i], nums[j], nums[k]])
            while nums[j] == nums[j+1]:
                j+=1

        while nums[i] == nums[i+1]:
            i+=1
    '''
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            left += 1
            right -= 1
    
    return  output


# --- Tests ---
print(threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,1,1]))            # []
print(threeSum([0,0,0]))            # [[0,0,0]]
print(threeSum([-2,0,1,1,2]))       # [[-2,0,2],[-2,1,1]]
