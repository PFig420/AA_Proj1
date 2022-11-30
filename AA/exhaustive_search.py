
from re import I

import time
class ExhaustiveSearch:

    def __init__(self):
        self.nvertices = None
        pass

    def exh_search(self, infile):
        start = time.time()
        print(infile)
        edges_and_vertices = []
        f = open(infile, "r")
        n_line = 0
        num_total_vertices = None
        vert_list = []
        lone_vertice_flag = False
        for line in f:
            
            len_line = len(line) + 1

            if n_line == 0: #operaçoes a fezer na primeira passagem
                num_total_vertices = int( len_line/2)
                vert_list = [0 for i in range(num_total_vertices)]

            vertice1 = None
            vertice2 = None
            i = 0
            for char in line:
                if char == '1':
                    if vertice1 == None:
                        vertice1 = i
                        vert_list[int(i/2)] = vert_list[int(i/2)]+1
                    else:
                        vertice2 = i 
                        vert_list[int(i/2)] = vert_list[int(i/2)]+1
                elif char == '2':
                    vertice1 = i 
                    vertice2 = i 
                    vert_list[int(i/2)] = vert_list[int(i/2)]+1
                    break
                i = i + 1
            tuple_base = (n_line, int(vertice1 / 2), int(vertice2 / 2))
            edges_and_vertices.append(tuple_base)
            n_line = n_line + 1
        for elem in vert_list:
            if elem == 0:  
                lone_vertice_flag = True
          
        max_matching, end, j = self.max_matching(edges_and_vertices, n_line, lone_vertice_flag)
        return max_matching, end-start, j, n_line
        # edges_and_vertices vai conter tuplos (arestas, vértice1, vertice2)

    def max_matching(self, edges_and_vertices,  num_edges, lone_vertice_flag):
        j = 0
        list_counter = [0 for i in range(num_edges)] #regista o nº de arestas que não têm vértices com a aresta da posição
    
        for i in range(num_edges):
            j += 1
            edge = edges_and_vertices[i]
          
            for edge2 in edges_and_vertices:
                j += 1
                if edge[0] != edge2[0] and edge[1] != edge2[1] and edge[1] != edge2[2] and edge[2] != edge2[1] and edge[2] != edge2[2]:
                    list_counter[i] += 1
          
        if lone_vertice_flag:
            end = time.time()
            return max(list_counter) +1, end, j
        else:    
            end = time.time()
            return max(list_counter), end, j
        
    