'''
Dijkstra Emergency Block — closed-book skeleton.

Trigger: shortest path + weighted + non-negative weights
Structure: dist map + min-heap
Key: relax edges, skip stale entries
Complexity: O((V + E) log V)

Write dijkstra(graph, start) → dict of shortest distances.
graph[node] = [(neighbor, weight), ...]
'''

import heapq


def dijkstra(graph, start):
    output = {start: 0}
    heap = [[0, start]]

    while heap:
        d, node = heapq.heappop(heap)

        if d != output[node]:
            continue
        for neighbor, weight in graph[node]:
            new_d = d + weight
            if new_d < output.get(neighbor, float('inf')):
                output[neighbor] = new_d
                heapq.heappush(heap, [new_d, neighbor])

        

    return output
    pass


# --- Tests ---
# Graph:  A --5--> B
#         A --2--> C
#         C --1--> B
#         B --3--> D
graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 3)],
    'C': [('B', 1)],
    'D': []
}
result = dijkstra(graph, 'A')
print(result)  # {'A': 0, 'B': 3, 'C': 2, 'D': 6}

# Single node
print(dijkstra({'X': []}, 'X'))  # {'X': 0}

# Two nodes
print(dijkstra({'A': [('B', 7)], 'B': []}, 'A'))  # {'A': 0, 'B': 7}
