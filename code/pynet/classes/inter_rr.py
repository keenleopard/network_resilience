from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

class InterRR(Inter_Network):

    def __init__(self)
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b
        all parameters already defined in the base class inter_Network
        """

        self.Ga = nx.random_regular_graph(self.ka, self.n)
	# random_regular_graph(d, n, seed=None) with d (int) as the degree of each node.
        self.Gb = nx.random_regular_graph(self.kb, self.n)
        
        #nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb)) // not really have the connected big graph


