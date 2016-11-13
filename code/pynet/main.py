from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from classes import Inter_Network
from classes import InterSF
from classes import InterRR
from classes import InterER

def main():
    N = 4000
    k = 4

    with open('frac_lmcc_rr.dat', 'w') as f:
        f.write('# p\t frac_lmcc_rr\n')
        for p in np.linspace(0.59, 0.63, num=100):
            G_ER = InterER(N,k,k)
            G_RR = InterRR(N,k,k)
            #G_SF = InterSF(3,N,k,k)
            to_be_removed = int(N * (1-p))

            # initial attack subnetwork a
            G_RR.remove_corresp(G_RR.attack_random(Q=to_be_removed))
            G_RR.cascade()
            print(nx.number_of_nodes(G_RR.Ga))
            f.write(str(p) + '\t{0.frac_lmcc}\n'.format(G_RR))


if __name__ == "__main__":
    main()

