import matplotlib.pyplot as plt
import networkx as nx
import random
import string

class Graph:
    def __init__(self, nodes_num, edges_num):
        print("Graph constructor is called!")
        self.nodes_num = nodes_num
        self.edge_num = edges_num
        self.nodes = []
        self.weigth = []
        self.edge = []

    def get_nodes(self):
        return self.nodes
    def get_edeges(self):
        return self.edge

    def get_weigth(self):
        return self.weigth

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

    def weigth_genarator(self):
        weigth_list = []
        while (len(weigth_list) < self.nodes_num):
            weigth = random.randint(1, 10)
            weigth_list.append(weigth)

        self.weigth = weigth

    def edge_genarator(self):
        edge = []
        for counter in range(0, self.edge_num):
            curr_edge = [random.choice(self.nodes), random.choice(self.nodes)]
            edge.append(curr_edge)

        self.edge = edge

    #Nodes are not made randomly and the user specifies them
    def set_special_nodes(self, nodes):
        self.nodes = nodes

    # weigth are not made randomly and the user specifies them
    def set_special_weigth(self, weigth):
        self.weigth = weigth

    #The graph is not made randomly and the user specifies it
    def set_special_graph(self, edge):
        self.edge = edge

    def remove_tube(self):
        for e in self.edge:
            if(e[0] == e[1]):
                self.edge.remove(e)

    def construct(self):
        G = nx.Graph()
        G.add_edges_from(self.edge)
        return G

    def color_map(self, model):
        color_map = []
        G = self.construct()
        for g in G:
            for i in self.nodes:
                if (g == i):
                    if (model.x[i]() == 1):
                        color_map.append('yellow')#Selected
                    else:
                        color_map.append('gray')# not Selected

        return color_map

    def plot(self, G, model):
        color_map = self.color_map(model)
        plt.figure(figsize=(16, 10))
        nx.draw(G, node_color=color_map,
                with_labels=True,
                node_size=500,
                font_color='black'
                )

        plt.show()


