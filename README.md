# weighted vertex cover

min $\sum$	xi wi

$\forall$ (i, j) xi + xj >= 1


from pyomo.environ import *

# ایجاد مدل
model = ConcreteModel()

# تعریف متغیرهای تصمیم
model.x = Var(['A', 'B', 'C', 'D', 'E'], within=Binary)

# افزودن قیدها
model.constraints = ConstraintList()
for (i, j) in graph:
    model.constraints.add(model.x[i] + model.x[j] >= 1)

# تابع هدف، اگر لازم است
# model.objective = Objective(...)

# حل مدل
solver = SolverFactory('glpk')
solver.solve(model)

# چاپ مقادیر متغیرهای تصمیم
for i in ['A', 'B', 'C', 'D', 'E']:
    print(i, model.x[i]())
