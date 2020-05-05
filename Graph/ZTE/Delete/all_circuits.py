import numpy as np
from collections import Counter
import networkx as nx
import graph_tool.all as gt

# read
matrix_load = np.loadtxt('Example_0409.csv', dtype=np.int, delimiter=",")
# pre
col, row = matrix_load.shape
A = np.zeros((col+row, col+row))
A[:col, col:] = matrix_load[:,:]
A[col:, :col] = matrix_load.T[:,:]
# graph
G = nx.from_numpy_matrix(A, create_using=nx.Graph)
list_G = nx.to_dict_of_lists(G)
g = gt.Graph()
for v in list_G:
    for u in list_G[v]:
        g.add_edge(v, u)
        g.add_edge(u, v)
# all circuits
# all_circuits = gt.all_circuits(g)
cycle_list = [c for c in gt.all_circuits(g) if c.size in range(4, 15)]
print(len(cycle_list))