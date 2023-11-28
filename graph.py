import matplotlib.pyplot as plt
from itertools import combinations, groupby
import networkx as nx
import random

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_node(range(n), weight=2)
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G


probability = 0.1
G = nx.erdos_renyi_graph(20, 0.1)
#G = gnp_random_connected_graph(100,0.01)

node_list = G.nodes

print(G.nodes)
print(G.edges)
color_map = []
for node in node_list:
    if node < 50:
        color_map.append('blue')
    else:
        color_map.append('green')

plt.figure(figsize=(16,10))
nx.draw(G, node_color=color_map,
        with_labels=True,
        node_size=500)

plt.show()
