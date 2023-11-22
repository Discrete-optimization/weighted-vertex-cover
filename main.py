from pyomo.environ import *

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
weight = [1, 555, 1, 597, 5546, 1]
graph = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]

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

print("Total answe: {}".format(total))