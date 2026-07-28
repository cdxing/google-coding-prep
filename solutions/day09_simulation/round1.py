'''
SIMULATION — Round 1. Timer: 45 minutes.

  ---
  LC 253: Meeting Rooms II

  Given an array of meeting time intervals where
  intervals[i] = [start_i, end_i], return the minimum number of
  conference rooms required.

  Example 1:
    intervals = [[0,30],[5,10],[15,20]]
    → 2

  Example 2:
    intervals = [[7,10],[2,4]]
    → 1

  Example 3:
    intervals = [[1,5],[2,6],[3,7],[4,8]]
    → 4

  Example 4:
    intervals = [[1,5],[5,10]]
    → 1  (end == start means no overlap)

  Constraints:
  - 1 <= intervals.length <= 10^4
  - 0 <= start_i < end_i <= 10^6

  ---
  Full interview flow:
  1. Clarify the problem
  2. State baseline approach + complexity
  3. State optimized approach + complexity
  这个题目叫做timer,它给的一个情景是这样的,就是给你一个一连串的起始时间和截止时间,就是start time,end time。然后它的意思是,它相当于会议时间,要根据这一系列的时间段,起始时间,截止时间,来看你需要多少个会议室。这是一个问题的场景。那就需要看这个时间段之间,每个时间段之间,它有没有重叠,有没有overlap。比较暴力的解法就是OK,所有的,这暴力就是说直接纯,直接了当的解法,就是把所有的时间,会议时间都循环,做一个for循环,然后记录它,来找它重叠时间段,而且有多少个时间段是重叠的,就数这个数嘛,计数。最多有多少个,就需要多少个会议室来安排这个会议。这是一个直接的想法。优化的想法是这样,就是你想象,先把这个会议时间呢,它的起始时间排序一下,从最早的时间到最晚的时间。应该说把所有的开始时间,结束时间,都把它排序。然后所有的开始的时间点呢,你用一个计数器来给它加一,然后结束的这个时间呢,你减一。就是每开始一个会议就加一,结束一个会议减一。然后你就数这个数,它最大的时候是什么时候。就相当于一个人进了一个房间,你就数这个人进这个房间,然后什么时候他这个人又出来,对吧?那这个房间里有多少个人,最多有多少个人,就是你需要多少个会议,多少个会议室。那这个就是一个基本的思路。接下来就是在代码上实现它。哎呀,这个也是之前有遇到过类似的题目。这些都是需要练。我觉得现在呢,知道一下,练一下这些题目是好的,有助于理解一些算法和实现。实际
  If you want to论复杂度的话, complexity for the brute force way, right? You need to loop over the time, and maybe need to loop over the end time again. So I'm thinking that you need to have multiple loops. So take a guess, at least two layers of loop, so that you need a time order of n squared. For the optimized way, the time complexity, basically at order of n, right? You just loop once, and then that's it. And then for the space complexity, the, I think both at an order of O(n).


  4. State invariant
  for the invariant of this type of scenario, it's like a fire line, you know, from, time is ticking from zero and go forward, and at which time step, there's a meeting start and the corporate meeting end. For the meeting start, you add one, and for the meeting end, you minus one. So you will have a series of array that is ordered, right?

  5. Code it
  done

  6. Walk through a test case
  test case 1, 
  first get a list of the time stamps and the value of them 
  sort them to b
  [
    [0, 1]
    [5, 1]
    [10, -1]
    [15, 1]
    [20, -1]
    [30, -1]
  ]
  set the count and the max_room to get the max number of room count
  return max_room



  7. State final complexity
  correction:
  as the time_stamps need to be sorted, so the time complexity is O(nlog n)
  space:  O(n)

  Go.

'''


def minMeetingRooms(intervals):
    time_stamps = []
    for interval in intervals:
        time_stamps.append([interval[0], 1])
        time_stamps.append([interval[1], -1])
    time_stamps.sort()
    max_room = 0
    count = 0
    for stamp in time_stamps:
        count += stamp[1]
        max_room = max(max_room, count)
    return max_room


# --- Tests ---
print(minMeetingRooms([[0,30],[5,10],[15,20]]))     # 2
print(minMeetingRooms([[7,10],[2,4]]))               # 1
print(minMeetingRooms([[1,5],[2,6],[3,7],[4,8]]))   # 4
print(minMeetingRooms([[1,5],[5,10]]))               # 1
print(minMeetingRooms([[1,3]]))                      # 1
print(minMeetingRooms([[1,5],[2,3],[4,6],[5,7]]))   # 2
