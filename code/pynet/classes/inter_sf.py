from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

def scale_free_powerlaw(n = 4000, lam = 3, k_avg = 4) :
    """
    n : number of nodes
    lam : exponent
    """
    noftries = n ** 2
    standard = k_avg + 0.5
    ratio = standard / np.mean(s)

    while (1) :
        s = nx.utils.powerlaw_sequence(n, lam)
        for i in range(len(s)) :
            s[i] = int(ratio * s[i])
        if (nx.is_valid_degree_sequence(s)) :
	    #G = nx.configuration_model(s) this would generate a lot of self-loops
	    G = nx.random_degree_sequence_graph(s, tries = noftries)
            break
    return G

class InterSF(Inter_Network):

    def __init__(self, lam = 3) :
        self.Ga = scale_free_powerlaw(self.n, lam, self.ka)
        self.Gb = scale_free_powerlaw(self.n, lam, self.kb)


