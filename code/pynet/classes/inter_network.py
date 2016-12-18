from __future__ import division, print_function

import networkx as nx
import random
import operator


class Inter_Network(nx.Graph):


    def __init__(self, n, ka, kb):
        """
        :param n: number of nodes of each sub network
        :param ka: average degree of network a
        :param kb: average degree of network b
        Ga, Gb: The subnetworks
        Ga_list, Gb_list: The list of the connected edges
        cluster_a, cluster_b: The list of the cluster in the subnetworks
        """
        self.n = n
        self.ka = ka
        self.kb = kb

        self.Ga = nx.empty_graph(n)
        self.Gb = nx.empty_graph(n)

        self.Ga_list = []
        self.Gb_list = []

        self.clusters_a = []
        self.clusters_b = []

    def attack_random(self, Q, type):
        """
        Creates the specific mapping scheme. Either Degree, Betweenness Centrality, Closeness Centrality, or Random.
        :param Q: The fraction of nodes to remove
        :param type: 0: Degree, 1: Betweenness Centrality, 2: Closeness Centrality
        :param order: 0: High to High 1: High to Low
        :return: The list of failed nodes
        """
        if Q > self.n:
            raise Exception("Value of nodes to remove is larger than nodes in the network!")
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
            elif type == 3:
                self.Ga_list = range(0, self.n)
                self.Gb_list = range(0, self.n)
            else:
                raise Exception("Wrong type given! Expected 0,1,2,3 given: " + str(type))

            failed_nodes = random.sample(range(self.n), Q)
            return failed_nodes

    def remove_corresp(self, failed_nodes, order):
        """
        Due to the strong one-to-one mapping, we remove the nodes from failed_nodes and their counterparts, which
        are specified in the Ga/Gb_list
        :param failed_nodes: The list of nodes to fail (only in one subnetwork. The counterparts are looked up)
        :param order: The connectivity model. 0 : High-to-High, 1 is High-to-Low
        :return: none
        We remove a node of the list in network A, and the look up for it's counterpart: We check in the list of nodes
        of network A, at which index it is, and then delete the node at the same (or n-index, for High-to-Low)  index
        from the network B.
        """
        if order == 0:
            for x in failed_nodes:
                index = self.Ga_list.index(x)
                self.Gb.remove_node(self.Gb_list[index])
                self.Ga.remove_node(x)
        elif order == 1:
            for x in failed_nodes:
                index = self.Ga_list.index(x)
                self.Gb.remove_node(self.Gb_list[(self.n-1)-index])
                self.Ga.remove_node(x)
        else:
            raise Exception("Wrong order given! Expected 0 or 1 given: " + str(order))

    def generate_mcc(self):
        """
        We generate a list containing different sets of unique nodes. Each set corresponds to one mutually connected
        cluster in the given sub-network. This is easily done, because we don't have a "real edge" combining the two
        networks, but look up their counterparts in the lists.
        :return: none
        """
        self.clusters_a = list(nx.connected_components(self.Ga))
        self.clusters_b = list(nx.connected_components(self.Gb))

    def step(self, subnet, order):
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
                    if order == 0:
                        corresp_node0 = self.Ga_list[node_index0]  # we get the ID of the corresponding node
                    if order == 1:
                        corresp_node0 = self.Ga_list[(self.n-1)-node_index0]  # we get the ID of the corresponding node
                    cluster_id0 = self.getClusterId(self.clusters_a, corresp_node0)  # all the edges have to connect to this cluster
                    if cluster_id0 == -1:
                        raise Exception("Error occurred while stepping.")
                    node_index1 = self.Gb_list.index(edge[1])  # we get the index of the corresponding node
                    if order == 0:
                        corresp_node1 = self.Ga_list[node_index1]  # we get the ID of the corresponding node
                    if order == 1:
                        corresp_node1 = self.Ga_list[(self.n-1)-node_index1]  # we get the ID of the corresponding node
                    cluster_id1 = self.getClusterId(self.clusters_a, corresp_node1)  # all the edges have to connect to this cluster
                    if cluster_id1 == -1:
                        raise Exception("Error occurred while stepping.")

                    if cluster_id0 != cluster_id1:
                        worked = True
                        self.Gb.remove_edge(*edge)

        if subnet == 'a':
                for edge in self.Ga.edges():
                    node_index0 = self.Ga_list.index(edge[0])  # we get the index of the corresponding node
                    if order == 0:
                        corresp_node0 = self.Gb_list[node_index0]  # we get the ID of the corresponding node
                    if order == 1:
                        corresp_node0 = self.Gb_list[(self.n-1)-node_index0]  # we get the ID of the corresponding node
                    cluster_id0 = self.getClusterId(self.clusters_b, corresp_node0)  # all the edges have to connect to this cluster
                    if cluster_id0 == -1:
                        raise Exception("Error occurred while stepping.")

                    node_index1 = self.Ga_list.index(edge[1])  # we get the index of the corresponding node
                    if order == 0:
                        corresp_node1 = self.Gb_list[node_index1]  # we get the ID of the corresponding node
                    if order == 1:
                        corresp_node1 = self.Gb_list[(self.n-1)-node_index1]  # we get the ID of the corresponding node
                    cluster_id1 = self.getClusterId(self.clusters_b, corresp_node1)  # all the edges have to connect to this cluster
                    if cluster_id1 == -1:
                        raise Exception("Error occurred while stepping.")

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

    def cascade(self, order):
        """
        Iterative process, calls the step function as long as edges get removed
        :param order: The order of the connection, either HTH or HTL
        :return: none
        """
        deleted_a = True
        deleted_b = True
        while deleted_a or deleted_b:
            self.generate_mcc()
            deleted_a = self.step('a', order)
            deleted_b = self.step('b', order)

    def getAscendingDegreeMap(self, g):
        """
        Generates an ascending list of the degree for every node
        :param graph: The graph to calculate
        :return: an ascending list of the degree for every node
        """
        deegreeDictionary = g.degree()
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1))
        return [l[0] for l in degreeList]

    def getAscendingClosenessCentralityMap(self, graph):
        """
        Generates an ascending list of the closeness centrality for every node
        :param graph: The graph to calculate
        :return: an ascending list of the closeness centrality for every node
        """
        deegreeDictionary = nx.closeness_centrality(graph,normalized=True)
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1))
        return [l[0] for l in degreeList]

    def getAscendingBetweennessCentralityMap(self, graph):
        """
        Generates an ascending list of the betweenness centrality for every node
        :param graph: The graph to calculate
        :return: an ascending list of the betweenness centrality for every node
        """
        deegreeDictionary = nx.betweenness_centrality(graph,normalized=True)
        degreeList = sorted(deegreeDictionary.items(), key=operator.itemgetter(1))
        return [l[0] for l in degreeList]

    @property
    def frac_lmcc(self):
        """
        Generates the fraction of nodes in the LMCC
        :return: the fraction of nodes in the LMCC
        """
        self.generate_mcc()
        clusters = sorted(self.clusters_a, key = lambda cluster: -len(cluster))
        fraction = len(clusters[0]) / nx.number_of_nodes(self.Ga)
        return fraction




