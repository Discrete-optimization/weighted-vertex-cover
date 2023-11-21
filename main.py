from pyomo.environ import *

nodes = ['A', 'B', 'C', 'D', 'E']
graph = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')]

# build concrete model with data specified
model = ConcreteModel()


# define variable
model.x = Var( nodes, within=Binary )

# define constraint
model.value = Objective(expr = sum(model.x[i] for i in nodes), sense=minimize)

# define ConstraintList
model.constraints = ConstraintList()
for (i, j) in graph:
    model.constraints.add(model.x[i] + model.x[j] >= 1)
