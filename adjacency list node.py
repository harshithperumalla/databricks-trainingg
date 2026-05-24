# Global variables
nodes = []
graph={}
node_count = 0

def add_node(v):
    if v in graph:
        print(v,"is already exist in graph")
    else:
        graph[v]=[]
        
        

add_node("A")
add_node("B")
print(graph)
