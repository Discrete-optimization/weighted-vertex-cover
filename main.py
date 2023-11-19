from pyomo.environ import *

nodes = ['A', 'B', 'C', 'D', 'E']
graph = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')]

# build concrete model with data specified
model = ConcreteModel()


# define variable
model.x = Var( nodes, within=Binary )

# define constraint
model.value = Objective(expr = sum(model.x[i] for i in nodes), sense=minimize)

# define constraint
model.weight = Constraint(expr = (model.x[i[0]] + model.x[i[1]] for i in graph) >= 1 )
