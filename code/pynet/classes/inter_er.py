from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

class InterER(nx.Graph):

    def __init__(self, n, ka, kb):
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b
        """
        self.n = n
        self.ka = ka
        self.kb = kb

        pa = ka / n
        pb = kb / n

        self.Ga = nx.fast_gnp_random_graph(n, pa)
        self.Gb = nx.fast_gnp_random_graph(n, pb)
        #self.Ga = nx.path_graph(n)
        #self.Gb = nx.path_graph(n)

        nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb))


    def one2one (self):
        """
        one to one connection between two sub networks.
        """
        for i in range(self.n):
            self.add_edge(i, self.n+i)

    def remove(self, subnet='a', nodelist=None):
        """
        Remove node list in subnet a or b
        """
        if nodelist is not None:
            if subnet == 'a':
                self.remove_nodes_from(nodelist)
                self.Ga.remove_nodes_from(nodelist)
            if subnet == 'b':
                self.remove_nodes_from(nodelist + self.n)
                self.Gb.remove_nodes_from(nodelist)

    def fail (self, subnet='a', Q=1):
        """
        remove Q nodes in one sub network randomly
        Q=1: number of nodes to be removed. (<= self.n)
        subnet='a', specify which subnetwork. (a/b)
        """
        failed_nodes = np.array(random.sample(range(self.n), Q))
        self.remove(subnet, failed_nodes)
        if subnet == 'a':
            self.remove('b', failed_nodes)
        elif subnet == 'b':
            self.remove('a', failed_nodes)
        else:
            print("error in subnet")
        return failed_nodes

    def attack (self, subnet='a', Q=1):
        """
        remove Q mostly connected nodes in one subnetwork.
        Q=1: number of nodes to be removed.
        subnet='a', specify which subnetwork. a/b
        """
        descending_order = sorted(G.nodes(), key = lambda i: -G.degree(i))
        attacked_ndoes = np.array(descending_order[:Q])
        self.remove(subnet, attacked_nodes)
        return attacked_nodes

    @property
    def is_mutually_connected (self):
        """
        check if the whole network is mutually connected,
        i.e. A clusters are isomophic to B clusters.
        """
        #Gb_nodes = np.array(self.Gb.nodes())
        #mapping = dict(zip(Gb_nodes, Gb_nodes - self.n))
        #Gb_copy = nx.relabel_nodes (self.Gb, mapping, copy = True)
        self.clusters_a = list(nx.connected_components(self.Ga))
        self.clusters_b = list(nx.connected_components(self.Gb))
        if self.clusters_a == self.clusters_b:
            return True
        else:
            return False

    def step (self, subnet):
        """
        Each step in cascading failure.
        Remove edges in the subnet connecting nodes in different clusters
        in the other subnet.
        """

    def cascade (self, init_subnet='a'):
        """
        Iterative process for cascading failure.
        During this, even steps are to remove edges in subnet a;
        odd steps are to remove edges in subnet b.

        init_subnet: initially failing nodes
        """
        if init_subnet == 'a':
            count = 1
        elif init__subnet == 'b':
            count = 0
        else:
            print("error in initial removal")

        while (not self.is_mutually_connected):
            self.step(chr(97 + (count % 2 != 0))) #even count for a, odd count for b
            count += 1



