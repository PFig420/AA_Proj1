import math
import random
from os import listdir
from exhaustive_search import ExhaustiveSearch

from graph_generator import GraphGenerator
from greedy_heuristic import GreedySearch

nvertices=[i for i in range(4,21)]

#e = ExhaustiveSearch()

g= GreedySearch()
for n in nvertices:
    m= GraphGenerator(n)
    m.generate_graph("graph/")

list = listdir("graph/")
temp = {}

f = open("res_greedy.txt", "w")

for file in list:
    #res, time, j, n_edges = e.exh_search("graph/"+file)
    res, time, j, n_edges = g.greedy_search("graph/"+file)
    #f.write(f"{file} : Maximum Matching {res} \n")
    temp[file] = (res, time, j, n_edges)
    
index_temp = sorted(temp.items())

for item in index_temp:
    print(item[0])
    f.write(f"{item[0]} : Maximum Matching {item[1][0]}  in {item[1][1]} seconds; Number of operations: {item[1][2]}, Number of edges: {item[1][3]}\n")