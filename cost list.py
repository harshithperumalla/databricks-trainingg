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
        # Undirected graph with weight
        list1 = (v2, cost)
        list2 = (v1, cost)
        graph[v1].append(list1)
        graph[v2].append(list2)

def print_graph():
    print("\nAdjacency List with Weights:")
    for node in graph:
        print(node, "->", graph[node])



add_node("A")
add_node("B")
add_node("C")

add_edge("A", "B", 3) 
add_edge("A", "C", 4) 

print(graph)
print_graph()
