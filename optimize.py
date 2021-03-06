import numpy as np
from scipy.optimize import minimize
import networkx as nx 
import random

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

A = ["a" + str(i) for i in range(1, 8)]
B = ["b" + str(i) for i in range(1, 8)]
C = ["c" + str(i) for i in range(1, 8)]

correct = {"A": A[1], "B":B[0], "C":C[2]} #on purpose I set them to low,
                                          #indexes, but not to perfectly zero ones


def objective_function(x):
    g = nx.Graph()
    def weight_function(w, z, index1, index2):
        #the next lines are just to fix it so that the correct
        #objects have shorter paths to each other (the assumption)
        #this will obviosly not be included in the correct code
        
        first_part= second_part = 3
        if w in [correct["A"], correct["B"], correct["C"]]:
            first_part = 1
        if z in [correct["A"], correct["B"], correct["C"]]:
            second_part = 1
        
        weight = x[0]*(min(first_part + second_part, random.randrange(2, 6))**x[1])*(index1+index2)**x[2]
        
        return weight
    
    for a in A:
        index_a = A.index(a) + 1 #this should never be zero
        for b in B:
            index_b=B.index(b) + 1
            
            g.add_edge(a, b, weight = weight_function(a, b, index_a, index_b))
            for c in C:
                index_c=C.index(c)
                g.add_edge(b, c, weight = weight_function(b, c, index_b, index_c))
                g.add_edge(a, c, weight = weight_function(a, c, index_a, index_c))

    A_list = []
    B_list = []
    C_list = []


    centrality = nx.eigenvector_centrality(g)


    for _, o in sorted([(centrality[obj], obj) for obj in centrality], reverse=True):
        if o in A:
            A_list.append(o)
        elif o in B:
            B_list.append(o)
        else:
            C_list.append(o)
    
    return A_list.index(correct["A"]) + B_list.index(correct["B"]) + C_list.index(correct["C"])


x0 = np.array([1.3, -0.7, -0.8])
#x1 = np.array(frange(-2, 5,0.5))
#xs = np.array(frange(-2, 5,0.5))
res = minimize(objective_function, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})

print(res.x)
#print C_list


