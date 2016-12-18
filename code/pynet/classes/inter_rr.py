from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from .inter_network import Inter_Network
class InterRR(Inter_Network):

    def __init__(self, n, ka, kb):
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b
        """
        self.n = n
        self.ka = ka
        self.kb = kb
 
        self.Ga = nx.random_regular_graph(self.ka, self.n)
        # random_regular_graph(d, n, seed=None) with d (int) as the degree of each node.
        self.Gb = nx.random_regular_graph(self.kb, self.n)



