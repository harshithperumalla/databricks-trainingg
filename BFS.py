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
        # graph[v2].append(v1)  # uncomment for undirected

def BFS(node,graph,visited):
    if node not in graph:
        print(node,"it is not in node of graph")
        return
    else:
        queue=[]
        queue.append(node)
        visited.add(node)
    while queue:
        current=queue.pop(0)
        print(current)
    for i in graph[current]:
        queue.append(i)
        visited.add(i)
        

        
        

# Driver code
add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")

visited = set()
print("BFS Traversal:")
BFS("A",graph,visited)
components = []
for i in nodes:
    if i not in visited:
        comp = set()
        BFS(i, comp, graph)
        components.append(comp)
        visited.update(comp)#-> it traverse the disconnected to connected to visite the nodes in graph

print("\nConnected Components:", components)

if len(components) == 1:
    print("The graph is connected")
else:
    print("The graph is disconnected")
visited1 = set()

for i in list(graph):
    if i not in visited:
        print(i, "is weakly connected node of the graph")
    else:                                   #-> strong or week checks
        
        visited1 = visited
        print(i, "is strongly connected node of the graph")
        
for i in list(graph):
    if i not in visited:  
       BFS("i",visited,graph)  #-> by week to strong by using dfs traverse
    print(i, "is strongly connected node of the graph")
print("\nNodes:", nodes)
print("Graph:", graph)
