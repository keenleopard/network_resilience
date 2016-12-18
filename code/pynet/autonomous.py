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

    G = InterER(N, k_avg, k_avg)
    G.one2one()

    autolist = G.setAutonomousNode(autoFrac=0.1, method="random")
    print(autolist)

    removeFrac = 0.1
    G.attack_random(subnet='a', Q=int(N * removeFrac))
    G.cascade(auto=True)

if __name__ == "__main__":
    main()
