# LC 56 - Merge Intervals
#
# Given an array of intervals where intervals[i] = [start_i, end_i],
# merge all overlapping intervals and return an array of the
# non-overlapping intervals that cover all the intervals in the input.
#
# Example:
# Input:  [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def merge(intervals):
    # step 1: sort by the first element 
    # step 2: init result with []
    # step 3: for each interval:
    #   if overlap: result[-1][1] = current[1]
    #   else: result.add(current)
    # return result
    intervals = sorted(intervals)
    result = []
    for i, interval in enumerate(intervals):
        if i == 0:
            result.append(interval)
        else:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)

    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
        

