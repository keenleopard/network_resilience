from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
from classes import InterER

def main():
    N = 200
    k = 4

    G = InterER(N, k, k)
    G.one2one()
    nodes = G.fail(Q=1)
    G.cascade()
    print("failed:", nodes)
    #print("nodes: ", G.nodes(), G.Ga.nodes(), G.Gb.nodes())
    #print("edges: ", G.Ga.edges(), G.Gb.edges())

    print(G.is_mutually_connected)
    clusters = sorted(G.clusters_a, key = lambda cluster: -len(cluster))
    print(len(clusters[0]))

    #nx.draw_networkx(G)
    #plt.show()


if __name__ == "__main__":
    main()

