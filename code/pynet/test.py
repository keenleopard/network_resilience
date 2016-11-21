from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from numpy import linalg as la

def zz(s) :
    norm = la.norm(s,2)
    norm1 = la.norm(s,1)
    print('norm', norm,'norm1', norm1, 'sum s', sum(s))
    if norm >= ((max(s) + np.amin(s) + 1)**2 / (4 * np.amin(s))) :
        print('max', max(s), 'np.amax', np.amax(s))
        return True
    else :
        return False


def generate(n, lam) :
    s=nx.utils.powerlaw_sequence(n, lam)
    ratio = 4.5 / np.mean(s)
    for i in range(len(s)) :
        s[i] = int(ratio * s[i])
    if sum(s) % 2 != 0 :
        s = np.append(s, [1])
        #print(s)
    return s

i = 0
noftrue = 0
while (1) :
    s = generate(500, 2.3)
    #if nx.is_valid_degree_sequence(s) != zz(s) 
        #print ('official is', nx.is_valid_degree_sequence(s), '\n')
        #print ('zz is', zz(s))
    if nx.is_valid_degree_sequence(s) == False :
        print ('is valid:', nx.is_valid_degree_sequence_havel_hakimi(s), 
        'sum is', sum(s))
    else :
        s_valid = s
        print ('is valid:', nx.is_valid_degree_sequence(s_valid))
        break
i = 0
while (i < 100) :
    #G = nx.configuration_model(s_valid)
    #G = nx.expected_degree_graph(s_valid, selfloops = False)
    #G = nx.havel_hakimi_graph(s_valid)
    G = nx.random_degree_sequence_graph(s_valid, tries = 1000000)
    if nx.is_connected(G) == True :
        print('is connected:', nx.is_connected(G), 
            nx.number_connected_components(G))
        nx.draw(G)
        plt.show()
        break
    else :
        i += 1
print (i)

#print ('same for', i, 'times')
#print ('number of true is', noftrue)
