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
        
        #nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb)) // not really have the connected big graph


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
                #self.remove_nodes_from(nodelist)
                self.Ga.remove_nodes_from(nodelist)
            if subnet == 'b':
                #self.remove_nodes_from(nodelist + self.n)
                self.Gb.remove_nodes_from(nodelist)
                
    def attack_random (self, subnet='a', Q=1):
        """
        remove Q nodes in one sub network randomly
        Q=1: number of nodes to be removed. (<= self.n)
        subnet='a', specify which subnetwork. (a/b)
        """
        if Q > self.n :
            print("error in removed number of nodes")
        else:
            failed_nodes = np.array(random.sample(range(self.n), Q))
            self.remove(subnet, failed_nodes) # remove the failed nodes of the selected subnet
            if subnet == 'a':
                self.remove('b', failed_nodes) # due to the one to one mapping, remove the correponding nodes of the other subnet
            elif subnet == 'b':
                self.remove('a', failed_nodes)
            else:
                print("error in subnet")
        return failed_nodes
    
    def attack_crucial (self, subnet='a', Q=1):
        """
        remove Q mostly connected nodes in one subnetwork.
        Q=1: number of nodes to be removed.
        subnet='a', specify which subnetwork. a/b
        """
        descending_order = sorted(G.nodes(), key = lambda i: -G.degree(i)) # getting node list from most degree to least degree
        attacked_nodes = np.array(descending_order[:Q])
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
        allowed_cluster = None
        if subnet == 'b':
            for node in self.Gb.nodes():
                for cluster in self.clusters_a:
                    if (node in cluster): allowed_neighbors = cluster
                for neighbor in self.Gb.neighbors(node):
                    if (neighbor not in allowed_neighbors):
                        self.remove_edge(node+self.n, neighbor+self.n)
                        self.Gb.remove_edge(node, neighbor)

        elif subnet == 'a':
            for node in self.Ga.nodes():
                for cluster in self.clusters_b:
                    if (node in cluster): allowed_neighbors = cluster
                for neighbor in self.Ga.neighbors(node):
                    if (neighbor not in allowed_neighbors):
                        self.remove_edge(node, neighbor)
                        self.Ga.remove_edge(node, neighbor)
        else:
            print("error in step subnet")


    def cascade (self, init_subnet='a'):
        """
        Iterative process for cascading failure.
        During this, even steps are to remove edges in subnet a;
        odd steps are to remove edges in subnet b.

        init_subnet: initially failing subnet
        """
        if init_subnet == 'a':
            count = 1
        elif init__subnet == 'b':
            count = 0
        else:
            print("error in initial removal")

        while (not self.is_mutually_connected):
            self.step(chr(97 + (count % 2 != 0))) #even count for a, odd count for b
            #print(count)
            count += 1

    @property
    def frac_lmcc(self):
        """
        fraction of No. nodes in the Largest Mutually Connected Component (lMCC).
        """
        if self.is_mutually_connected:
            clusters = sorted(self.clusters_a, key = lambda cluster: -len(cluster))
            fraction = len(clusters[0]) / nx.number_of_nodes(self.Ga)
            return fraction
        else:
            print("not mutually connected yet")




