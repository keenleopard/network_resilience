from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import operator

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


        #degreeListA = self.getAscendingDegreeMap(self.Ga)
        #degreeListB = self.getAscendingDegreeMap(self.Gb)
        #print(self.getAscendingBetweennessCentralityMap(self.Ga))

        #self.lowToLow(degreeListA,degreeListB)
        #self.highToHigh(degreeListA,degreeListB)
        #self.highToLow(degreeListA,degreeListB)


        #self.Ga = nx.path_graph(n)
        #self.Gb = nx.path_graph(n)

        nx.Graph.__init__(self, nx.disjoint_union(self.Ga, self.Gb))


    def getAscendingClosenessCentralityMap(self,graph):
        """
        returns an ascending list of nodes with their corresponding Closeness Centrality, sorted by the degree: [node:normalized centrality]
        The Closeness Centrality of a node is the measure of "centrality" in the network, it is the sum of the length of the shortest paths between the given
        node and all the other nodes. The more central a node is, the closer it is to all the other nodes. (Wikipedia)
        """
        deegreeDictionary = nx.closeness_centrality(graph,normalized=True)
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1)) 
        return degreeList

    def getAscendingBetweennessCentralityMap(self,graph):
        """
        returns an ascending list of nodes with their corresponding Betweenness Centrality, sorted by the degree: [node:normalized centrality]
        The Betweenness Centrality of a node is the measure of "centrality" in the network, it is the nbr. of the shortest paths from all nodes to
        all the others, passing trough a given node. A node with a high betweenness centrality has a large influence on the transfer of items in the network
        (Wikipedia)
        """
        deegreeDictionary = nx.betweenness_centrality(graph,normalized=True)
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1)) 
        return degreeList

    def getAscendingDegreeMap(self,graph):
        """
        returns an ascending list of nodes with their corresponding degree, sorted by the degree: [node:degree]
        """
        #get all the degrees of every node in a dictionary as {node : degree}
        deegreeDictionary = graph.degree()
        #sort the dictionary in ascending order based on the degree, and save in a list as [node:degree]
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1)) 
        return degreeList


    def lowToLow(self,listA,listB):
        """
        Connects the lowest degree to the lowest degree of the two graphs
        list: [node:degree]
        """
        for x in range(self.n):
            self.add_edge(listA[x][0],listB[x][0]+self.n) #graphB nodes have an offset of n
   
    def highToHigh(self,listA,listB):
        """
        Connects the highest degree to the highest degree of the two graphs
        list: [node:degree]
        """
        for x in range(self.n-1,-1,-1):
            self.add_edge(listA[x][0],listB[x][0]+self.n) #graphB nodes have an offset of n


    def highToLow(self,listA,listB):
        """
        Connects the highest degree of Network A to the lowest degree of Netowrk B
        list: [node:degree]
        """
        for x in range(self.n-1,-1,-1):
            self.add_edge(listA[x][0],listB[self.n-x-1][0]+self.n) #graphB nodes have an offset of n

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




