# Global variables
nodes = []
graph = {}

def add_node(v):
    if v in graph:
        print(v, "already exists in the graph")
    else:
        nodes.append(v)      
        graph[v] = []      

def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        # Undirected graph
        graph[v1].append(v2)
        graph[v2].append(v1)

def print_graph():
    print("\nAdjacency List:")
    for node in graph:
        print(node, "->", graph[node])


add_node("A")
add_node("B")
add_node("C")

add_edge("A", "B")
add_edge("A", "C")

print_graph()
