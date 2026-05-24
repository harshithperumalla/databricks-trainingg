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
# Detect cycle in directed graph using DFS
def is_cyclic_util(node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if is_cyclic_util(neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)
    return False

def is_cyclic():
    visited = set()
    rec_stack = set()

    for node in graph:
        if node not in visited:
            if is_cyclic_util(node, visited, rec_stack):
                return True
    return False
    return None  # if no path found
add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")

print("Cycle Detected:", is_cyclic())