from pyomo.environ import *
from graph import Graph

number_of_nodes = 200
number_of_edges = 300

G1 = Graph(number_of_nodes, number_of_edges)

G1.node_genarator()
G1.edge_genarator()
G1.remove_tube()

nodes = G1.get_nodes()
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
resualt_list = []
for i in nodes:
    total = sum(model.x[j]() for j in nodes)
    print(i, model.x[i]())
    resualt_list.append([i, model.x[i]()])

print("Total answe: {}".format(total))
print(resualt_list)

G = G1.construct()
for g in G:
    for i in nodes:
        if(g==i):
            if(model.x[i]() == 1):
                color_map.append('yellow')
            else:
                color_map.append('gray')


G1.plot(G, color_map)