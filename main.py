from pyomo.environ import *
from graph import Graph


number_of_nodes = 15
number_of_edges = 45

G1 = Graph(number_of_nodes, number_of_edges)
print(G1.get_nodes())
G1.node_genarator()
print(G1.get_nodes())

print(G1.get_edeges())
G1.edge_genarator()
print(G1.get_edeges())

G = G1.construct()
G1.plot(G)


"""nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
weight = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
graph = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J")]

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
for i in nodes:
    total = sum(model.x[j]() * weight[j.index(j)] for j in nodes)
    print(i, model.x[i]())

print("Total answe: {}".format(total))"""