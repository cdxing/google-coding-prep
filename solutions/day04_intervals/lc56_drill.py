'''
Timer: 20 minutes. Closed-book.

  ---
  LC 56: Merge Intervals

  Given an array of intervals where intervals[i] = [start_i, end_i],
  merge all overlapping intervals, and return an array of the
  non-overlapping intervals that cover all the intervals in the input.

  Example 1: intervals = [[1,3],[2,6],[8,10],[15,18]]
             → [[1,6],[8,10],[15,18]]

  Example 2: intervals = [[1,4],[4,5]]
             → [[1,5]]

  Constraints:
  - 1 <= intervals.length <= 10^4
  - intervals[i].length == 2
  - 0 <= start_i <= end_i <= 10^4

  ---
  Write:
  1. Pattern
  2. Invariant
  3. Complexity

  Then code. Go.

'''

# 1. Pattern:
# So the pattern for this part that you see overlapping and non-converged windows. So this is the pattern I want you to reference, please. It's similar to a sliding window.
# 2. Invariant:
# for the interval variance is that we want to make it a sorted before the first, the left side of all interval, so that you can compare the right side of the previous interval and the left side of the current interval to decide whether you want to merge it. If the intervals, all the intervals are not sorted, it will change a lot of, like, some of the intervals you may visit again, take more space complexity and time complexity.
# 3. Complexity:
# For the time, for the complexity, if you versus sorting and loop over all the elements, I think it's at order of n, and space complexity would be at, because you need to store the elements. I think also order of n.


def merge(intervals):
    intervals = sorted(intervals)
    output = []
    #for i, interval in enumerate(intervals):
    for interval in intervals:
        if not output or interval[0] > output[-1][1]:
            output.append(interval)
        else:
            output[-1][1] = max(output[-1][1], interval[1])
    return output




# --- Tests ---
print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                  # [[1,5]]
print(merge([[1,4],[0,4]]))                  # [[0,4]]
print(merge([[1,1]]))                        # [[1,1]]
print(merge([[1,4],[2,3]]))                  # [[1,4]]
