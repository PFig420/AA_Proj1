 
from re import I
import time

class GreedySearch:
    def __init__(self):
        self.nvertices = None
        pass

    def greedy_search(self, infile):
        start = time.time()
        print(infile)
        edges_and_vertices = []
        f = open(infile, "r")
        n_line = 0
        num_total_vertices = None

        for line in f:
            
            len_line = len(line) + 1

            if n_line == 0: #operaçoes a fezer na primeira passagem
                num_total_vertices = int( len_line/2)
              

            vertice1 = None
            vertice2 = None
            i = 0
            for char in line:
                if char == '1':
                    if vertice1 == None:
                        vertice1 = i
                        
                    else:
                        vertice2 = i 
                       
                elif char == '2':
                    vertice1 = i 
                    vertice2 = i 
                    break
                i = i + 1
            tuple_base = (n_line, int(vertice1 / 2), int(vertice2 / 2))
            edges_and_vertices.append(tuple_base)
            n_line = n_line + 1
       
          
        max_matching , end, j = self.max_matching(edges_and_vertices, n_line, num_total_vertices)
        return max_matching, end-start, j, n_line
        # edges_and_vertices vai conter tuplos (arestas, vértice1, vertice2)

    def max_matching(self, edges_and_vertices, nedges, num_total_vertices):
            list_counter = [0 for i in range(num_total_vertices)]
            j = 0

            for edge in edges_and_vertices:
                j += 1
                list_counter[edge[1]] += 1
                if edge[1] != edge[2]:
                    list_counter[edge[2]] += 1

            end = time.time()
            return nedges - min(list_counter), end, j