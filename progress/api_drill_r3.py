'''
API Recall Drill — Round 3 (final). From memory, no looking.
'''

# ============================================================
# 1. set
# ============================================================
# add element: set.add(e)
# remove (error if missing): set.remove(e)
# remove (safe): set.discard(e)
# check membership: if e in set:
# length: len(set)

# ============================================================
# 2. dict
# ============================================================
# set key: dict[key] = value
# get with default: dict.get(key, default)
# check key exists: if key in dict:
# delete key: del dict[key]
# iterate keys: for key in dict:
# iterate key-value: for key, value in dict.items():
# length: len(dict)

# ============================================================
# 3. list
# ============================================================
# append to end: list.append(e)
# pop from end: list.pop()
# pop from index: list.pop(i)
# access last: list[-1]
# access first: list[0]
# length: len(list)
# sort in place: list.sort()
# sorted copy: sorted(list)

# ============================================================
# 4. deque
# ============================================================
# import: from collections import deque
# create: queue = deque()
# enqueue: queue.append(e)
# dequeue: queue.popleft()
# peek front: queue[0]
# peek back: queue[-1]
# length: len(queue)

# ============================================================
# 5. heapq
# ============================================================
# import: import heapq
# push: heapq.heappush(heap, e)
# pop smallest: heapq.heappop(heap)
# peek smallest: heap[0]
# heapify: heapq.heapify(list)

# ============================================================
# 6. string
# ============================================================
# length: len(s)
# char at index: s[i]
# slice: s[i:j]
# check substring: if subs in s:
# split whitespace: s.split()
# split comma: s.split(", ")
# join list: ", ".join(list)
# iterate: for c in s:

# ============================================================
# 7. built-ins
# ============================================================
# max / min: max(x, y) / min(x, y)
# abs: abs(x)
# range(n): from 0 to n-1
# range(start, stop): from start to stop -1
# range(start, stop, step): from start to stop -1 with step size step
# enumerate: for i, num in enumerate(nums)
# zip: for x, y in zip(list1,list2)
# sorted with key: sorted(list, key = lambda x: x[1])
# sorted reverse: sorted(list, reverse = True)
# float infinity: float('inf')
