from pyomo.environ import *

sample_graph = [(0,1), (0,5), (0,4), (0,3)]
weight = [1, 1, 1, 1]

"""

M.ITEMS = Set(initialize=value.keys())
M.x = Var(M.ITEMS, domain=Binary)

M.value = Objective(expr=sum(value[i]*M.x[i] for i in M.ITEMS),sense=maximize)
M.weight = Constraint(expr=sum(weight[i]*M.x[i] for i in M.ITEMS) <=Capacity)

solver = SolverFactory('glpk', executable='/usr/bin/glpsol')
solver.solve(M)

for i in value.keys():
    print('  ', i, ':', M.x[i]())
print("objective:",M.value())"""