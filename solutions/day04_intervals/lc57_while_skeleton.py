# LC 57 - Insert Interval (three while-loops approach)
#
# You are given an array of non-overlapping intervals sorted by start,
# and a new interval. Insert the new interval and merge if necessary.
# Return the array of intervals after insertion.
#
# Example:
# Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]

def insert(intervals, newInterval):
    i = 0
    result = []

    # phase 1: add all intervals entirely before newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # phase 2: merge all overlapping intervals into newInterval
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    result.append(newInterval)

    # phase 3: add all remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1


    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))
