from pyomo.environ import *

class Model:

    def __init__(self, nodes, graph, weigth):
        print("Model constructor is called!")
        self.nodes = nodes
        self.weigth = weigth
        self.graph = graph

        # build concrete model with data specified
        self.model = ConcreteModel()
        # define variable
        self.model.x = Var(nodes, within=Binary)

    def get_model(self):
        return self.model

    def constraint(self):
        # define constraint
        self.model.value = Objective(expr=sum(self.model.x[i] for i in self.nodes), sense=minimize)
        # define ConstraintList
        self.model.constraints = ConstraintList()
        for (i, j) in self.graph:
            self.model.constraints.add(self.model.x[i] + self.model.x[j] >= 1)

    def solver(self):
        self.constraint()
        # solving model
        solver = SolverFactory('glpk')
        solver.solve(self.model)
        return(solver)

    def monitoring(self):
        self.solver()
        resualt_list = []
        for i in self.nodes:
            total = sum(self.model.x[j]() for j in self.nodes)
            print(i, self.model.x[i]())
            resualt_list.append([i, self.model.x[i]()])

        print("Total answe: {}".format(total))
        print(resualt_list)