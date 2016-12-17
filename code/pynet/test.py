from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy
import time
from classes import Inter_Network, InterRR, InterER

def main():
    N = 10
    k_avg = 4

    testGraph = InterER(N, k_avg, k_avg)

    nx.draw(testGraph)
    plt.show()

if __name__ == "__main__":
    main()
