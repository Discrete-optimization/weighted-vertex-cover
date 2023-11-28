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
    G.add_nodes_from(range(n))
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
G = gnp_random_connected_graph(499,0.001)

node_list = G.nodes

print(len(node_list))
print(G.edges)

plt.figure(figsize=(16,10))
nx.draw(G, node_color='lightblue',
        with_labels=True,
        node_size=500)

#plt.show()
