from __future__ import division, print_function

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import operator

import sys


class Inter_Network(nx.Graph):


    def __init__(self, n, ka, kb):
        """
        n: number of nodes of each sub network
        ka, kb: average degree of network a, b
        """

        self.n = n
        self.ka = ka
        self.kb = kb

        self.Ga = nx.empty_graph(n)
        self.Gb = nx.empty_graph(n)

        self.Ga_list = []
        self.Gb_list = []


    def remove(self, subnet='a', nodelist=None):
        """
        Remove node list in subnet a or b
        """
        if nodelist is not None:
            if subnet == 'a':
                self.Ga.remove_nodes_from(nodelist)
            if subnet == 'b':
                self.Gb.remove_nodes_from(nodelist)

    def attack_special(self, Q,type):
        """
        Creates the specific mapping scheme. Either Degree, Betweenness Centrality, or Closeness Centrality. Then it creates the coupling between
        Ga and Gb, either high to high, or high to low
        :param Q: The fraction of nodes to remove
        :param type: 0: Degree, 1: Betweenness Centrality, 2: Closeness Centrality
        :param order: 0: High to High 1: High to Low
        :return: The list of failed nodes
        """
        if Q > self.n:
            print("error in removed number of nodes")
        else:
            if type == 0:
                self.Ga_list = self.getAscendingDegreeMap(self.Ga)
                self.Gb_list = self.getAscendingDegreeMap(self.Gb)
            elif type == 1:
                self.Ga_list = self.getAscendingBetweennessCentralityMap(self.Ga)
                self.Gb_list = self.getAscendingBetweennessCentralityMap(self.Gb)
            elif type == 2:
                self.Ga_list = self.getAscendingClosenessCentralityMap(self.Ga)
                self.Gb_list = self.getAscendingClosenessCentralityMap(self.Gb)
            else:
                raise Exception("Wrong type given! Expected 0,1,2 given: " + str(type))

            failed_nodes = random.sample(range(self.n), Q)
            return failed_nodes
    
    def remove_corresp (self, failed_nodes,order, subnet='a'):
        """
        due to the one to one mapping, remove the correponding nodes of the other subnet
        """
        if order == 1:
            for x in failed_nodes:
                "We want to delete items from failed_nodes. Therefore, we check in Ga_list to get the index, at which "\
                    "position this node is in the A subnetwork based on the degree or centrality values.Then we delete"\
                    "this position in network B,by adding n nodes to the index, and finally delete the failed node"
                index = self.Ga_list.index(x)
                self.Gb.remove_node(self.Gb_list[index])
                self.Ga.remove_node(x)
        elif order == 2:
            for x in failed_nodes:
                index = self.Ga_list.index(x)
                self.Gb.remove_node(self.Gb_list[(self.n-1)-index])
                self.Ga.remove_node(x)
        else:
            raise Exception("Wrong order given! Expected 0 or 1 given: " + str(order))

    @property
    def is_mutually_connected (self):
        """
        check if the whole network is mutually connected,
        i.e. A clusters are isomorphic to B clusters.
        """
        self.clusters_a = list(nx.connected_components(self.Ga))
        self.clusters_b = list(nx.connected_components(self.Gb))
        if self.clusters_a == self.clusters_b:
            return True
        else:
            return False


    def stepNew(self,subnet,order):
        """
        For every node in the selected network, we run the procedure.
        We select the corresponding node in the other network (always available trough 1:1 mapping) trough one of our
         given lists (e.g. degree, centrality,...) and save the cluster id.
         Then we check every edge from the starting node, and do the above procedure (get the corresponding node and its
         cluster ID) If both cluster IDs are different, we remove the edge.
        :param subnet: The id of the subnet to work on
        :return: nothing
        """
        worked = False
        if subnet == 'b':

                for edge in self.Gb.edges():
                    node_index0 = self.Gb_list.index(edge[0])  # we get the index of the corresponding node
                    if order == 1:
                        corresp_node0 = self.Ga_list[node_index0]  # we get the ID of the corresponding node
                    if order == 2:
                        corresp_node0 = self.Ga_list[(self.n-1)-node_index0]  # we get the ID of the corresponding node
                    cluster_id0 = self.getClusterId(self.clusters_a, corresp_node0)  # all the edges have to connect to this cluster
                    if cluster_id0 == -1:
                        print("ERROR stepping")
                        sys.exit(-1)
                    node_index1 = self.Gb_list.index(edge[1])  # we get the index of the corresponding node
                    if order == 1:
                        corresp_node1 = self.Ga_list[node_index1]  # we get the ID of the corresponding node
                    if order == 2:
                        corresp_node1 = self.Ga_list[(self.n-1)-node_index1]  # we get the ID of the corresponding node
                    cluster_id1 = self.getClusterId(self.clusters_a, corresp_node1)  # all the edges have to connect to this cluster
                    if cluster_id1 == -1:
                        print("ERROR stepping")
                        sys.exit(-1)
                    if cluster_id0 != cluster_id1:
                        worked = True
                        self.Gb.remove_edge(*edge)

        if subnet == 'a':
                for edge in self.Ga.edges():
                    node_index0 = self.Ga_list.index(edge[0])  # we get the index of the corresponding node
                    if order == 1:
                        corresp_node0 = self.Gb_list[node_index0]  # we get the ID of the corresponding node
                    if order == 2:
                        corresp_node0 = self.Gb_list[(self.n-1)-node_index0]  # we get the ID of the corresponding node
                    cluster_id0 = self.getClusterId(self.clusters_b, corresp_node0)  # all the edges have to connect to this cluster
                    if cluster_id0 == -1:
                        print("ERROR stepping")
                        sys.exit(-1)
                    node_index1 = self.Ga_list.index(edge[1])  # we get the index of the corresponding node
                    if order == 1:
                        corresp_node1 = self.Gb_list[node_index1]  # we get the ID of the corresponding node
                    if order == 2:
                        corresp_node1 = self.Gb_list[(self.n-1)-node_index1]  # we get the ID of the corresponding node
                    cluster_id1 = self.getClusterId(self.clusters_b, corresp_node1)  # all the edges have to connect to this cluster
                    if cluster_id1 == -1:
                        print("ERROR stepping")
                        sys.exit(-1)
                    if cluster_id0 != cluster_id1:
                        worked = True
                        self.Ga.remove_edge(*edge)

        return worked

    def getClusterId(self,cluster,node):
        identifier = -1
        i = 0
        for sets in cluster:
            if node in sets:
                identifier = i
                break
            i += 1

        return identifier

    def cascade (self, order):
        """
        Iterative process for cascading failure. # not contain the initial attack part, only the remove edges part
        During this, even steps are to remove edges in subnet a;
        odd steps are to remove edges in subnet b.

        init_subnet: initially failing subnet
        """
        deletedA = True
        deletedB = True
        while (deletedA or deletedB):
            buffer = self.is_mutually_connected
            deletedA = self.stepNew('a',order)
            deletedB = self.stepNew('b',order)

    def getAscendingDegreeMap(self, g):
        """
        returns an ascending list of nodes with their corresponding degree, sorted by the degree: [node:degree]
        """
        #get all the degrees of every node in a dictionary as {node : degree}
        deegreeDictionary = g.degree()
        #sort the dictionary in ascending order based on the degree, and save in a list as [node:degree]
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1))
        return [l[0] for l in degreeList]
    
    def getAscendingClosenessCentralityMap(self,graph):
        """
        returns an ascending list of nodes with their corresponding Closeness Centrality, sorted by the degree: [node:normalized centrality]
        The Closeness Centrality of a node is the measure of "centrality" in the network, it is the sum of the length of the shortest paths between the given
        node and all the other nodes. The more central a node is, the closer it is to all the other nodes. (Wikipedia)
        """
        deegreeDictionary = nx.closeness_centrality(graph,normalized=True)
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1))
        return [l[0] for l in degreeList]

    def getAscendingBetweennessCentralityMap(self,graph):
        """
        returns an ascending list of nodes with their corresponding Betweenness Centrality, sorted by the degree: [node:normalized centrality]
        The Betweenness Centrality of a node is the measure of "centrality" in the network, it is the nbr. of the shortest paths from all nodes to
        all the others, passing trough a given node. A node with a high betweenness centrality has a large influence on the transfer of items in the network
        (Wikipedia)
        """
        deegreeDictionary = nx.betweenness_centrality(graph,normalized=True)
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1))
        return [l[0] for l in degreeList]

    @property
    def frac_lmcc(self):
        """
        fraction of No. nodes in the Largest Mutually Connected Component (LMCC).
        """
        buffer = self.is_mutually_connected
        clusters = sorted(self.clusters_a, key = lambda cluster: -len(cluster))
        fraction = len(clusters[0]) / nx.number_of_nodes(self.Ga)
        return fraction




