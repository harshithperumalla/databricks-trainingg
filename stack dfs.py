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
        # graph[v2].append(v1)  # uncomment for undirected

def DFS(node, visited, graph):
    if node not in graph:
        print(node, "is not a node in the graph")
        return
    
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS(neighbor, visited, graph)
def DFSiterative(node,visited,graph):
    if node not in graph:
        print(node,"it is not node in graph ")
    return
    if node not in  visited:
        print(node)
    stack=[]
    stack.append[node]
    while stack:
        currentnode=stack.pop()
    if currentnode not in vistied:
        print(currentnode)
        visited.add(currentnode)
    for i in graph(currentnode):
        dfs(currentnode,visited,graph)
   
    
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
print("DFS Traversal:")
DFS("A", visited, graph)
DFSiterative("A",visited,graph)
print("DFS Iterative:")



print("\nNodes:", nodes)
print("Graph:", graph)
