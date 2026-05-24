from collections import deque

# Global variables
graph = {}
nodes = []
node_count = 0

def add_node(v):
    global node_count
    if v in graph:
        print(v, "is already present in the graph")
    else:
        node_count += 1
        nodes.append(v)
        graph[v] = []   # adjacency list for the new node

def add_edge(v1, v2):
    if v1 not in graph or v2 not in graph:
        print("One or both nodes are not present in the graph")
    else:
        graph[v1].append(v2)   # directed graph
        # graph[v2].append(v1) # uncomment for undirected

def BFS(start, target):
    if start not in graph:
        print(start, "is not in the graph")
        return None
    if target not in graph:
        print(target, "is not in the graph")
        return None

    visited = set()
    parent = {}   # to reconstruct path
    queue = deque([start])
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()
        
        if current == target:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None  # if no path found
add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")

print(BFS("A", "D"))

