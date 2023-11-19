from pyomo.environ import *

nodes = ['A', 'B', 'C', 'D', 'E']
graph = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')]

# build concrete model with data specified
model = ConcreteModel()
