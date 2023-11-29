import matplotlib.pyplot as plt
from itertools import combinations, groupby
import networkx as nx
import random
import string

class Graph:
    def __init__(self, nodes_num, edges_num):
        print("Graph constructor is called!")
        self.nodes_num = nodes_num
        self.edge_num = edges_num
        self.nodes = []
        self.edge = []

    def get_nodes(self):
        return self.nodes
    def get_edeges(self):
        return self.edge

    def get_random_lable(sef, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return (result_str)

    def node_genarator(self):
        curr_node = []
        while (len(curr_node) < self.nodes_num):
            node = self.get_random_lable(3)
            if node not in curr_node:
                curr_node.append(node)

        self.nodes = curr_node

    def edge_genarator(self, length):
        edge = []
        for counter in range(0, length):
            curr_edge = [random.choice(self.nodes), random.choice(self.nodes)]
            edge.append(curr_edge)

        self.edge = edge

    def construct(self):
        G = nx.Graph()
        G.add_edges_from(self.edge)
        return G

    def plot(self, G):
        plt.figure(figsize=(16, 10))
        nx.draw(G, node_color='blue',
                with_labels=True,
                node_size=500,
                font_color='white'
                )

        plt.show()




number_of_nodes = 15
number_of_edges = 45

G1 = Graph(number_of_nodes, number_of_edges)
print(G1.get_nodes())
G1.node_genarator()
print(G1.get_nodes())

