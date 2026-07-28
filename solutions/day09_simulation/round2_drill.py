'''
Clone Graph — closed-book rewrite.

Given a reference of a node in a connected undirected graph,
return a deep copy (clone) of the graph.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Constraints:
- 0 <= nodes <= 100
- Node.val unique
- No self-loops, no repeated edges
- Graph is connected

Go.
'''


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None
    visited = {} # map those visited in the map for exit the recursive activity
    def dfs(node): # dfs as entry point
        if node in visited:
            return visited[node]
        else:
            clone = Node(node.val)
            visited[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

    return dfs(node)


# --- Tests ---
# Test 1: 4-node cycle
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]
clone = cloneGraph(n1)
print(clone.val)                              # 1
print([n.val for n in clone.neighbors])       # [2, 4]
print(clone is not n1)                        # True
print(clone.neighbors[0] is not n2)           # True

# Test 2: single node
single = Node(1)
clone2 = cloneGraph(single)
print(clone2.val)                             # 1
print(clone2.neighbors)                       # []
print(clone2 is not single)                   # True

# Test 3: empty
print(cloneGraph(None))                       # None
