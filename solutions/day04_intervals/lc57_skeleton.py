# LC 57 - Insert Interval
#
# You are given an array of non-overlapping intervals sorted by start,
# and a new interval. Insert the new interval and merge if necessary.
# Return the array of intervals after insertion.
#
# Example:
# Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]

def insert(intervals, newInterval):
    # phase 1: add all intervals that end before newInterval starts
    result = []

    for interval in intervals:
        if interval[1] < newInterval[0]:
            result.append(interval)
        # phase 2: merge all intervals that overlap with newInterval
        elif interval[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    result.append(newInterval)

    # return result
    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))
