'''
SIMULATION — Round 2. Timer: 45 minutes.

  ---
  LC 133: Clone Graph

  Given a reference of a node in a connected undirected graph,
  return a deep copy (clone) of the graph.

  Each node in the graph contains a value (int) and a list of
  its neighbors (List[Node]).

  class Node:
      def __init__(self, val=0, neighbors=None):
          self.val = val
          self.neighbors = neighbors if neighbors is not None else []

  The graph is represented as an adjacency list.
  The given node will always be the first node with val = 1.

  Example 1:
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    Node 1 connects to [2,4]
    Node 2 connects to [1,3]
    Node 3 connects to [2,4]
    Node 4 connects to [1,3]
    → deep copy of same structure

  Example 2:
    adjList = [[]]
    → single node, no neighbors

  Example 3:
    adjList = []
    → empty graph, return None

  Constraints:
  - 0 <= number of nodes <= 100
  - 1 <= Node.val <= 100
  - Node.val is unique for each node
  - No repeated edges and no self-loops
  - The graph is connected

  ---
  Full interview flow:
  1. Clarify the problem

  So, my current understanding of the clone graph is that you have, after the class of node, and you can apply the neighbors, attribute is node, and the goal for this graph, to clone this, is to have a, so, when a node has its neighbor, right, its neighbor also can knows that they are their neighbor. It's not one way, it's two-way, right? It's two-way. So, suppose you have node one, and its neighbor, for example, node two, it's neighbor. Then, vice versa, node two also has node one as its neighbor, right? And when you clone node one, you will clone, the value would be, so I'm thinking about this clone, right? It's not a single one node, it's a graph that's connected to the node one as well. So, the value itself is one, and it should also cover the neighbors it connects to, and neighbor's neighbor, right? So, once you are neighbor's neighbor, you're still connected. So this is like a depth-first searching process. And what kind of confused me is that in the first example, right, you connect, first connect, in the first example, node one's neighbor are N2 and N4, right? And N2, node two, also has neighbor N3. So, if the neighbors we are talking about are directly connected to N1, then I understand, okay, only 2 and 4 are directly connected to N1, the rest of them are connected through the middle connections, right? So, for example, if N1 wants to connect to N3, it needs to go through N2 to go to N3, or go through N4 to get to N3, right?

  Still, I'm a little bit confused about the return, what to return from the clone graph, right? It's actually like an adjacent list. Because for the clone graph, you can call the value, you can call its neighbors, and it's not exactly the original node. I'm thinking about what's the exactly structure of this graph. It's not just a node, it's not an adjacency list. What's the format would it look like? I'm thinking that it can call...

  Now I have better understanding. So it's actually copy but using a separate container, separate variables. So that, okay, this node or this graph has the same sets of values and same set of values, separate container from the original value. It's not modified or make change of the original copy of the graph, of the nodes. which is a true copy

  So for the, let's first working on the DFS, depth-first search. So, because it's a connected loop, and there's no direction. So if the node one points node two, and node two also has neighbor one, right? So what? The stop case is, okay, there's no neighbor, or the neighbor's neighbor points itself, then you stop, right? Stop this process. And also if there's empty single node, there's no neighbor, we also stop. If there is num object, none list, then return none

  2. State baseline approach + complexity
  3. State optimized approach + pattern
  4. State invariant
  5. Code it
  6. Walk through a test case
  So, in the depth-first searching process, we want to a complete copy, clone, of the original graph. So, what we can do is, the key part is the node's value are copied, and its neighbors are copied, and neighbors' neighbors also copied. That way we have a complete graph, right? Rather than we only have its value and its neighbor's value, then that's it. That's not all we want. We want its neighbors, neighbors, neighbors, neighbors, and their neighbors' value as well. So how do we do that? We use the depth-first searching. So the base case is that if a certain node is visited, visited meaning that it's already copied, right? It's already cloned, then just return the visited clone. So the key is the original node. The value is the cloned node. Okay? So that's the base case. So if the node is not visited, then you first create a clone, create a new node where its value, it's the value of the one to be cloned. And then you mark it in the visited so you know this one is already visited. And for its neighbors, you first loop over all the neighbors of the original one, and then append their clone

  7. State final complexity
  The final complexity for the time, each step, right, we moved into the step. I think it's an order of n. Correct me if I'm wrong. And for the space complexity, it's an order of n. We need a container, a map, right, to store the mapping.
  Correction: Time is O(V + E), not O(n). Each node visited once (V), each edge traversed once (E). Space: O(V) for visited map + recursion stack.

  Score: 6/10. Needed 4 hints to get working code.

  Go.

'''


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    #clone = Node()
    #if node == None:
    if not node:
        return None
    #clone.val = node.val
    #clone.neighbors = node.neighbors
    visited = {}
    def dfs(nd):
        if nd in visited:
            return visited[nd]
        else:
            nd_clone = Node(nd.val)
            visited[nd] = nd_clone
            for neighbor in nd.neighbors:
                nd_clone.neighbors.append( dfs(neighbor))

            # need to return nd_clone in the else situation as well
            return nd_clone

            #visited[nd] = nd_clone

    #clone.neighbors.append(dfs(node.neighbors))
    #for n in node.neighbors:
        #clone.neighbors.append(dfs(n))

    
    #return clone
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
print(clone is not n1)                        # True (deep copy)
print(clone.neighbors[0] is not n2)           # True (deep copy)

# Test 2: single node
single = Node(1)
clone2 = cloneGraph(single)
print(clone2.val)                             # 1
print(clone2.neighbors)                       # []
print(clone2 is not single)                   # True

# Test 3: empty
print(cloneGraph(None))                       # None
