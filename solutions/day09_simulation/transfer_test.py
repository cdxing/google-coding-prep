'''
TRANSFER TEST — LC 207: Course Schedule
Environment: Google Doc simulation, no-run, dry run manually.

Clarify:
- Input: numCourses (int), prerequisites (list of [a, b] pairs where b must be taken before a)
- Output: boolean — can all courses be finished?
- Core insight: this is cycle detection in a directed graph
- Build adjacency list, then DFS with 3-state tracking

Complexity:
- Time: O(V + E) — visit each course once, traverse each edge once
- Space: O(V + E) — adjacency list + state array + recursion stack
'''


def canFinish(numCourses, prerequisites):
    if not prerequisites and numCourses > 0:
        return True
    adjList = [[] for _ in range(numCourses)]
    for preq in prerequisites:
        adjList[preq[1]].append(preq[0])
    # use a 3-state list to denote its status, 0 = unvisited, 1 = in progress, 2 = done
    state = [0] * numCourses
    def dfs(course):
        if state[course] == 1:
            return False # loop found, false
        elif state[course] == 2:
            return True # safe
        else:
            state[course] = 1
            for neighbor in adjList[course]:
                if dfs(neighbor) == False:
                    return False
            state[course] = 2
        return True
    for course in range(numCourses):
        if dfs(course) == False:
            return False
    return True


# --- Tests ---
print(canFinish(2, [[1,0]]))                         # True
print(canFinish(2, [[1,0],[0,1]]))                   # False
print(canFinish(4, [[1,0],[2,1],[3,2]]))             # True
print(canFinish(3, [[0,1],[0,2],[1,2]]))             # True
print(canFinish(1, []))                              # True
print(canFinish(3, [[0,1],[1,2],[2,0]]))             # False
print(canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))       # True
