import matplotlib.pyplot as plt
from itertools import combinations, groupby
import networkx as nx
import random
import string



def get_random_lable(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)

def node_genarator(length):
    curr_edge = []
    while(len(curr_edge) < length):
        node = get_random_lable(3)
        if node not in curr_edge:
            curr_edge.append(node)

    return curr_edge

def edge_genarator(nodes, length):
    edge = []
    for counter in range (0, length):
        curr_edge = [random.choice(nodes), random.choice(nodes)]
        edge.append(curr_edge)

    return edge

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


number_of_nodes = 15
number_of_edges = 45
G = nx.Graph()
nodes = node_genarator(number_of_nodes)
print(nodes)
edges = edge_genarator(nodes, number_of_edges)
print(edges)


#G = nx.erdos_renyi_graph(100, 0.1)
#G = nx.fast_gnp_random_graph(55, 0.1, seed=None, directed=False)
#G = gnp_random_connected_graph(100,0.01)
G.add_edges_from(edges)

"""curr_lable = []
for ed in edges:
    l = {(ed[0], ed[1]): '1'}
    curr_lable.append(l)

print(curr_lable)"""

plt.figure(figsize=(16,10))
nx.draw(G, node_color='blue',
        with_labels=True,
        node_size=500,
        font_color='white'
        )
"""
edge_labels={('A', 'B'): 'AB',
             ('B', 'C'): 'BC',
             ('B', 'D'): 'BD'},
"""
plt.show()
