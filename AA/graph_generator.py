
import random
import math


class GraphGenerator:

    def __init__(self, nvertices):
        self.nvertices=nvertices
        self.densities=[0.125,0.25,0.50,0.75]
        random.seed(97487)


    def generate_graph(self, outfile):

        for d in self.densities:
            axis_values= [[i, j] for i in range(1,40) for j in range(1,40)] #valor para eixos de x e y
            filename=f'{outfile}_{self.nvertices}_{int(d*100)}.txt'
            outf = open(filename , "w")
            
            for i in range(self.nvertices):
                coord=random.choice(axis_values)
                axis_values.remove(coord)

                #don't allow vertices too close
                if [coord[0]-1, coord[1]] in axis_values:
                    axis_values.remove([coord[0]-1, coord[1]]) 

                if [coord[0]+1, coord[1]] in axis_values:
                    axis_values.remove([coord[0]+1, coord[1]]) 

                if [coord[0], coord[1]-1] in axis_values:
                    axis_values.remove([coord[0], coord[1]-1]) 

                if [coord[0], coord[1]+1] in axis_values:
                    axis_values.remove([coord[0], coord[1]+1])

            # based on the density compute the number of edges
            nedges= math.ceil(d*(self.nvertices*(self.nvertices-1)/2))


            #Incidence matrix 
            incidence_matrix= [[0 for i in range(self.nvertices)]  for j in range(nedges) ]
           
            for j in range(nedges): #para cada aresta, determinar os 2 vértices em que toca

                coords1 = random.randint(0, self.nvertices-1) # Escolher um vértice que é extremo desta aresta 
                coords2 = random.randint(0, self.nvertices-1) # Escolher um vértice que é extremo desta aresta

                incidence_matrix[j][coords1]  += 1
                incidence_matrix[j][coords2]  += 1
           
            [outf.write(f'{str(row).replace("[","").replace("]","").replace(",","")}\n') for row in incidence_matrix]
