# Intervals Pattern Card

## Merge Intervals (LC 56)
```
Trigger:   Overlapping/merging ranges, scheduling conflicts
Invariant: After sorting by start, only need to compare with last result interval
Bug:       Use max(prev.end, curr.end) when merging, not just curr.end
```

## Insert Interval (LC 57)
```
Trigger:   Insert a new interval into sorted non-overlapping list
Invariant: Three phases — before overlap, during overlap (merge), after overlap
Bug:       Must merge with ALL overlapping intervals, not just the first one
```

## Meeting Rooms / Interval Scheduling (LC 253)
```
Trigger:   Count max concurrent intervals or minimum resources needed
Invariant: Sort events by time; +1 for start, -1 for end; track running count
Bug:       When start == end, process end before start (free room before assigning)
```
