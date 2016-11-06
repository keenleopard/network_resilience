from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from classes import InterER

def main():
    N = 4000
    k_avg = 4

    with open('frac_lmcc.dat', 'w') as f:
        f.write('# p*<k>\t frac_lmcc\n')
        for p in np.linspace(0.59, 0.63, num=100):
            G = InterER(N,k_avg,k_avg)
            G.one2one()

            to_be_removed = int(N * (1-p))
            G.fail(Q=to_be_removed)
            G.cascade()
            print(nx.number_of_nodes(G.Ga))
            f.write(str(p*k_avg) + '\t{0.frac_lmcc}\n'.format(G))


if __name__ == "__main__":
    main()

