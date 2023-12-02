<p>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Discrete-optimization/weighted-vertex-cover">
</p>

# weighted nodes cover

This project discusses the graph covering problem in which a set of edges in an edge- and node-weighted graph is chosen to satisfy some covering constraints while minimizing the sum of the weights. In this problem, because of the large integrality gap of a naive linear programming (LP) relaxation, LP rounding algorithms based on the relaxation yield poor performance. Here we propose a stronger LP relaxation for the graph covering problem. The proposed relaxation is applied to designing primal–dual algorithms for two fundamental graph covering problems: the prize-collecting edge dominating set problem and the multicut problem in trees. Our algorithms are an exact polynomial-time algorithm for the former problem, and a 2-approximation algorithm for the latter problem. These results match the currently known best results for purely edge-weighted graphs.

## TODO

- [x] phase1: Implement the Int model for the node covering problem in pyomo software and run it on different graphs.
- [x] phase2: Implement the approximate algorithm program for the node coverage example in pyomo (hint: take a graph with its weights and implement its linear programming model to reach an initial solution and... use graph packages and Compare the approximate algorithm with the int model on large size graphs up to 10,000 nodes.
- [x] phase3: Show that in the relax model, for the node covering problem, the upper limit for the variables (=>1) is not necessary.


## Requirements
````
pip install -r requirements.txt
````

## How to run?
````
python3 main.py
````
