from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

class InterSF(Inter_Network):

    def __init__(self)
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b
        all parameters already defined in the base class inter_Network
        """

        self.Ga = nx.scale_free_graph(self.n, pa)
        self.Gb = nx.fast_gnp_random_graph(self.n, pb)
        #self.Ga = nx.path_graph(n)
        #self.Gb = nx.path_graph(n)
        
        #nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb)) // not really have the connected big graph


