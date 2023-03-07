import networkx as nx
import matplotlib.pyplot as plt

file = "grafo.txt"
with open(file, 'r') as f:
    lines = f.readlines()

dic = {}
for line in lines:
    line = line.strip().split(" ")
    head, tail = line[0], line[1:]
    dic[head] = tail

# export this function and use it in another module
def get_neighbors(node):
    return dic[node]

if __name__ == "__main__":
    G = nx.Graph()
    for key, value in dic.items():
        G.add_node(key)
        for v in value:
            G.add_edge(key, v)

    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()
