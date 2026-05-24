# Global variables
nodes = []
graph = {}

def add_node(v):
    if v in graph:
        print(v, "already exists in the graph")
    else:
        nodes.append(v)      
        graph[v] = []      

def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        # Directed edge with weight
        graph[v1].append((v2, cost))

def print_graph():
    print("\nDirected Adjacency List with Weights:")
    for node in graph:
        for edge in graph[node]:
            print(f"{node} --{edge[1]}--> {edge[0]}")
    print()

add_node("A")
add_node("B")
add_node("C")

add_edge("A", "B", 3)
add_edge("A", "C", 4)
add_edge("B", "C", 2)

print(graph)      
print_graph()     
