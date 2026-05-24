nodes = []
graph = []
node_count = 0

def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count += 1
        nodes.append(v)

        for n in graph:
            n.append(0)

        temp = [0] * node_count
        graph.append(temp)

def add_edge(v1, v2, cost=1):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost   # undirected

def print_graph():
    print("\nAdjacency Matrix:")
    for row in graph:
        print(row)

def dijkstra(src):
    dist = {node: float("inf") for node in nodes}
    parent = {node: None for node in nodes}
    visited = set()

    dist[src] = 0

    for _ in range(len(nodes)):
        # pick unvisited node with smallest distance
        min_node = None
        for node in nodes:
            if node not in visited:
                if min_node is None or dist[node] < dist[min_node]:
                    min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        # update distances
        index = nodes.index(min_node)
        for neighbor_index, cost in enumerate(graph[index]):
            if cost > 0:  # edge exists
                neighbor = nodes[neighbor_index]
                if dist[min_node] + cost < dist[neighbor]:
                    dist[neighbor] = dist[min_node] + cost
                    parent[neighbor] = min_node

    return dist, parent

def shortest_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]  # reverse

# ----------------
# Example Usage
# ----------------
add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A", "B", 2)
add_edge("A", "C", 5)
add_edge("B", "D", 1)
add_edge("C", "D", 2)

print("Nodes:", nodes)
print_graph()

src = "A"
dist, parent = dijkstra(src)

print("\nShortest distances from", src)
for node in nodes:
    print(f"{src} -> {node} = {dist[node]}")

print("\nShortest paths from", src)
for node in nodes:
    print(f"{src} -> {node}:", shortest_path(parent, node))
