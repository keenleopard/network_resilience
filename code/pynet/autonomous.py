from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy
import time
from classes import Inter_Network, InterRR, InterER

def main():
    N = 100
    k_avg = 4

    testGraph = InterER(N, k_avg, k_avg)
    testGraph.one2one()

    autolist = testGraph.setAutonomousNode(autoFrac=0.1, method="random")
    print(autolist)
    print(testGraph.nodes())
    print(testGraph.Ga.nodes())
    print(testGraph.Gb.nodes())

    removeFrac = 0.1
    testGraph.attack_random(subnet='a', Q=int(N * removeFrac))

if __name__ == "__main__":
    main()
