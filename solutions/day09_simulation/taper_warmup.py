'''
TAPER WARMUP — Wed 7/29. LC 841: Keys and Rooms.
Google Doc simulation, no-run, communication focus.
Score: 7.5/10. Correct approach, mechanical bugs (continue vs return, naming).

Complexity: O(V + E) time, O(V) space.
'''


def canVisitAllRooms(rooms):
    visited = set()
    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)
    dfs(0)
    return len(visited) == len(rooms)


# --- Tests ---
print(canVisitAllRooms([[1],[2],[3],[]]))              # True
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))       # False
print(canVisitAllRooms([[1,2],[],[0]]))                 # True
