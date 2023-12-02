"""
Decemer 2023
you can also see this project on our team's github organization
https://github.com/Discrete-optimization/weighted-vertex-cover
"""


from model import Model
from graph import Graph


#Make a simple graph:
nodes = ["A", "B", "C", "D", "E", "F"]
weigth = [1, 5, 3, 9, 2, 4]
graph = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("A", "F")]

#construct a graph:
G1 = Graph(len(nodes), len(graph))

G1.set_special_nodes(nodes)
G1.set_special_weigth(weigth)
G1.set_special_graph(graph)

#call pyomo create and solve modle:
m1 = Model(nodes, graph, weigth)
m1.monitoring()

#using this function is optional.
G1.plot(G1.construct(), m1.get_model())