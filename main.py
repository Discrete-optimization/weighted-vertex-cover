"""
December 2023
you can also see this project on our team's github organization
https://github.com/Discrete-optimization/weighted-vertex-cover
"""
from model import Model
from graph import Graph


#Enter the number of nodes and edges you want:
number_of_nodes = 200
number_of_edges = 300

#construct a graph:
G1 = Graph(number_of_nodes, number_of_edges)

G1.node_genarator()#generate random nodes ["A", "B", "C", "D"]
G1.weigth_genarator()#generate random weigth between 1 to 10 [1, 5, 3, 9]
G1.edge_genarator()#denerate random edge between ndes [("A", "B"), ("A", "C"), ("A", "D")]
G1.remove_tube()#using this function is optional. Removes tubes. [("A", "B"), ("C", "C")] -> [("A", "B")]

#set nodes and graph with nodes an edges:
nodes = G1.get_nodes()
weigth = G1.get_weigth()
graph = G1.get_edeges()

#call pyomo create and solve modle:
m1 = Model(nodes, graph, weigth)
m1.monitoring()

#using this function is optional.
G1.plot(G1.construct(), m1.get_model())
