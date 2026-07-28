'''
API Recall Drill — Round 2. From memory, no looking.
'''

# ============================================================
# 1. set
# ============================================================
# add element: set.push(e)
# remove element (error if missing): set.remove(e)
# remove element (safe): set.discard(s)
# check membership: in e in set:
# length: len(set)


# ============================================================
# 2. dict
# ============================================================
# set key: dict[key] = value
# get with default: dict.get(key, default)
# check key exists: if key in dict:
# delete key: del dict[key]
# iterate keys: for key in dict:
# iterate key-value: for key, value in dict.items()
# length: len(dict)


# ============================================================
# 3. list
# ============================================================
# append to end: list.append()
# pop from end: list.pop()
# pop from index: list.pop(i)
# access last element: list[-1]
# access first element: list[0]
# length: len(list)
# sort in place: list.sort()
# sorted copy: sorted(list)


# ============================================================
# 4. deque  (which module?)
# ============================================================
# import: import deque
# create: queue = deque
# enqueue (add to right): queue.append(e)
# dequeue (remove from left): queue.popleft()
# peek front: queue[0]
# peek back:  queue[-1]
# length: len(queue)


# ============================================================
# 5. heapq  (which module?)
# ============================================================
# import: from collections import heapq
# push: heapq.heappush(heap, e)
# pop smallest: heapq.heappop(heap)
# peek smallest: heap[0]
# heapify a list: heapq.heapify(list)


# ============================================================
# 6. string
# ============================================================
# length: len(s)
# access char at index: s[i]
# slice: s[i: j]
# check substring: if subs in s:
# split by whitespace: s.split()
# split by comma: s.split(", ")
# join list into string: ", ".join(list)
# iterate: for c in s: ; for i, c in enumerate(s)


# ============================================================
# 7. common built-ins
# ============================================================
# max / min: max(x, y) / min(x, y)
# abs: abs(x)
# range(n): n: int, for i in range(n)
# range(start, stop): iterate from index start to (stop -1)
# range(start, stop, step):iterate from index start to (stop -1)  with step 
# enumerate: for i, num in enumerate(numx)
# zip: for x, y in zip(list1, list2):
# sorted with key: sorted(dict, key = lambda x: x[1])
# sorted reverse: sorted(list, reverse=True)
# float infinity: float('inf')
