import networkx as nx
import matplotlib.pyplot as plt

file = "grafo.txt"
with open(file, 'r') as f:
    lines = f.readlines()

dic = {}
for line in lines:
    line = line.strip().split(" ")
    head, tail = line[0], line[1:]
    # print(f"key: {head} => value: {tail}")
    dic[head] = tail

def create_graph():
    G = nx.DiGraph()
    for key, value in dic.items():
        G.add_node(key)
        for v in value:
            G.add_edge(key, v)
    return G
# export this function and use it in another module
def get_neighbors(node):
    return dic[node]

# plot the graph implementing Depth First Search
def dfs(G, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(G[vertex]) - visited)
    return visited

if __name__ == "__main__":
    G = create_graph()
    # pick a tree-like layout
    # pos = nx.
    nx.draw_planar(G, node_size=1000, with_labels=True, font_size=14)
    plt.show()
