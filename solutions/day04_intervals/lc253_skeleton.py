# LC 253 - Meeting Rooms II
#
# Given an array of meeting time intervals [[start, end], ...],
# find the minimum number of conference rooms required.
#
# Example:
# Input:  [[0,30],[5,10],[15,20]]
# Output: 2
#
# Approach: sweep line
# step 1: create events list — +1 for each start, -1 for each end
# step 2: sort events (tie-break: end before start)
# step 3: sweep through, track running count and max count
# return max count

def minMeetingRooms(intervals):
    sweep = []
    # 1. create event list 
    for interval in intervals:
        sweep.append([interval[0], 1])
        sweep.append([interval[1], -1])

    # 2. sort events
    sweep = sorted(sweep)
    

    # 3. sweep through
    count = 0
    max_count = 0
    for event in sweep:
        count += event[1]
        max_count = max(max_count, count)

    return max_count




intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))
