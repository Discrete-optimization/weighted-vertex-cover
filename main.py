from model import Model
from graph import Graph

number_of_nodes = 10
number_of_edges = 25

G1 = Graph(number_of_nodes, number_of_edges)

G1.node_genarator()
G1.edge_genarator()
G1.remove_tube()

nodes = G1.get_nodes()
graph = G1.get_edeges()

m1 = Model(nodes, graph)
m1.monitoring()

G1.plot(G1.construct(), m1.get_model())