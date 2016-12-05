from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from .inter_network import Inter_Network

def generate(n, lam) :
    s=nx.utils.powerlaw_sequence(n, lam)
    ratio = 4.5 / np.mean(s)
    for i in range(len(s)) :
        s[i] = int(ratio * s[i])
    if sum(s) % 2 != 0 :
        s = np.append(s, [1])
        #print(s)
    return s

def scale_free_powerlaw(n = 4000, lam = 3, k_avg = 4) :
    """
    n : number of nodes
    lam : exponent
    """
    noftries = 100000
    standard = k_avg + 0.5
    
    s = generate(n, lam)
    ratio = standard / np.mean(s)
    for i in range(len(s)) :
        s[i] = int(ratio * s[i])
    if (nx.is_valid_degree_sequence(s)) :
	#G = nx.configuration_model(s) this would generate a lot of self-loops
	G = nx.random_degree_sequence_graph(s, tries = noftries)
        #break
    return G

class InterSF(Inter_Network):

    def __init__(self, n, ka, kb, lam = 3) :
        self.n = n
        self.ka = ka
        self.kb = kb
        self.Ga = scale_free_powerlaw(n, lam, ka)
        self.Gb = scale_free_powerlaw(n, lam, kb)


