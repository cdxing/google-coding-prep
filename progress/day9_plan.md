# Day 9 Plan — Tuesday July 28, 2026

## Today's win conditions
1. Complete two 45-min unknown rounds
2. Fix one highest-impact weakness from simulation
3. 11:00 research oral update (15-30 min max)
4. Evening: Bay Area luggage packed

## Morning

7:15-7:45  Wake up, self-talk, light movement
7:45-8:10  Breakfast, prep, settle in

## Warm-up (8:10-8:30, 20 min, no notes)

Write skeletons only, one small example mental trace each:

1. Sliding window while-shrink
   ```
   for right: expand
       while INVALID: remove s[left], left += 1
       add s[right]
       update answer
   ```

2. BFS level-by-level
   ```
   queue = deque(sources)
   while queue:
       for _ in range(len(queue)):
           node = queue.popleft()
           for neighbor: if in_bounds and unvisited: append
       time += 1
   ```

3. 3Sum dedup
   ```
   sort
   for i: if i>0 and nums[i]==nums[i-1]: continue
       left, right = i+1, end
       while left < right:
           if < 0: left++  elif > 0: right--
           else: append, skip dup left, skip dup right, left++, right--
   ```

4. API quick recall (write once, no file needed)
   ```
   set: add(), remove()
   deque: append(), popleft()
   heapq: heappush(h,v), heappop(h), h[0]
   len() for everything
   ```

## Google Two-Round Simulation

8:30-9:15   Round 1 — unknown Medium, full interview flow
9:15-9:30   Break — walk, water, no answers
9:30-10:15  Round 2 — different pattern, unknown Medium

Full flow each round:
```
Clarify semantics (contiguous? ordered? positive? duplicates?)
→ baseline approach + complexity
→ optimized approach + pattern
→ state invariant
→ code
→ walk through test case
→ state complexity
→ handle follow-up
```

Observe:
- Did I misread problem constraints?
- Was first-pass code stable?
- Did I invent any fake API?
- Did I test proactively?
- Did I communicate throughout?

## Debrief (10:15-10:35)

Score each round /10:
```
1  Clarification
1  Correct pattern
1  Baseline stated
1  Invariant stated
2  Complete working code
1  API/syntax clean
1  Tests
1  Complexity correct
1  Communication + follow-up
```

Pick ONE highest-impact issue for afternoon repair.

## Research (10:35-11:30)

10:35-10:50  Prep update (3 items: done, current, next step)
11:00        Oral report to professor
11:30        Done — back to Google

## Afternoon

12:15-12:45  Fix one worst issue from morning simulation
1:00-2:00    Delayed closed-book retest of that issue
2:15-3:00    Communication practice: edge cases, complexity
3:15-4:00    Five-interview battle map (name, focus, story, risk, review)
4:15-5:15    Light Google review or job admin
5:15-6:00    Wrap up, record, prep Wed airport review materials

## Evening

6:00-7:00   Dinner
7:00-7:45   Pack Bay Area luggage (do tonight, not Wed morning)
7:45-8:30   Business maintenance
8:30-9:00   Pattern cards light review
9:00+       No new problems. Sleep.

## Wednesday decision rule

Both rounds >= 7, no repeated bug types:
→ Strict taper. Pattern cards only. Rest.

Any round < 7:
→ Wed morning: 30 min fix on that one issue, then stop.
