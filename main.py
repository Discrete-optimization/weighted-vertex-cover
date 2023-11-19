from pyomo.environ import *

weight = {'Bag1':300, 'Bag2':1, 'Bag3':200, 'Bag4':100, 'Bag5':10, 'Bag6':54}
value = {'Bag1':4000, 'Bag2':5000, 'Bag3':5000, 'Bag4':2000, 'Bag5':1000, 'Bag6':2834}

Capacity = 106
M = ConcreteModel()

M.ITEMS = Set(initialize=value.keys())
M.x = Var(M.ITEMS, domain=Binary)

M.value = Objective(expr=sum(value[i]*M.x[i] for i in M.ITEMS),sense=maximize)
M.weight = Constraint(expr=sum(weight[i]*M.x[i] for i in M.ITEMS) <=Capacity)

solver = SolverFactory('glpk', executable='/usr/bin/glpsol')
solver.solve(M)

for i in value.keys():
    print('  ', i, ':', M.x[i]())
print("objective:",M.value())