from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

class InterSF(Inter_Network):

    def __init__(self, lam = 3)
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b
        all parameters already defined in the base class inter_Network
        """

        #self.Ga = nx.scale_free_graph(self.n, pa)
	self.Ga = nx.random_powerlaw_tree(self.n, lam)
	# random_powerlaw_tree(n, gamma=3, seed=None, tries=100) with gamma (float) – Exponent of the power law ; tries (int) – Number of attempts to adjust the sequence to make it a tree.
        self.Gb = nx.fast_gnp_random_graph(self.n, lam)
        
        #nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb)) // not really have the connected big graph


