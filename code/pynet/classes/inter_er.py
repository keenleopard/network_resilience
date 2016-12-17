from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from .inter_network import Inter_Network
class InterER(Inter_Network):

    def __init__(self, n, ka, kb) :
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b

        """
        self.n = n
        self.ka = ka
        self.kb = kb

        pa = self.ka / self.n
        pb = self.kb / self.n

        self.Ga = nx.fast_gnp_random_graph(n, pa)
        self.Gb = nx.fast_gnp_random_graph(n, pb)

        nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb))
        #nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb)) // not really have the connected big graph


