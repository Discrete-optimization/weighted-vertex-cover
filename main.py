from model import Model
from graph import Graph

"""number_of_nodes = 200
number_of_edges = 300

G1 = Graph(number_of_nodes, number_of_edges)

G1.node_genarator()
G1.edge_genarator()
G1.remove_tube()

nodes = G1.get_nodes()
graph = G1.get_edeges()"""

nodes = ["A", "B", "C", "D"]
graph = [("A","B"), ("A","C"), ("A","D")]

m1 = Model(nodes, graph)
m1.monitoring()




"""G = G1.construct()
for g in G:
    for i in nodes:
        if(g==i):
            if(model.x[i]() == 1):
                color_map.append('yellow')
            else:
                color_map.append('gray')


G1.plot(G, color_map)"""