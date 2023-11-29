from pyomo.environ import *
from graph import Graph


number_of_nodes = 5
number_of_edges = 8

G1 = Graph(number_of_nodes, number_of_edges)

G1.node_genarator()
G1.edge_genarator()


nodes = G1.get_nodes()
weight = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
graph = G1.get_edeges()

# build concrete model with data specified
model = ConcreteModel()


# define variable
model.x = Var( nodes, within=Binary)

# define constraint
model.value = Objective(expr = sum(model.x[i] for i in nodes), sense=minimize)

# define ConstraintList
model.constraints = ConstraintList()
for (i, j) in graph:
    model.constraints.add(model.x[i] + model.x[j] >= 1)

# solving model
solver = SolverFactory('glpk')
solver.solve(model)

# test answer
color_map = []
for i in nodes:
    total = sum(model.x[j]() * weight[j.index(j)] for j in nodes)
    print(i, model.x[i]())
    if(model.x[i]() == 1):
        color_map.append("red")
    else:
        color_map.append("blue")

print("Total answe: {}".format(total))

G = G1.construct()
G1.plot(G, color_map)