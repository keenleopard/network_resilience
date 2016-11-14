from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from classes import Inter_Network
from classes import InterSF
from classes import InterRR
from classes import InterER

def main(choice = 'ER'):
    N = 40
    k = 4

    with open('frac_lmcc' + choice + '.dat', 'w') as f:
        f.write('# p\t frac_lmcc_rr\n')
        for p in np.linspace(0.55, 0.70, num=100):
            if choice == 'ER' :
                G = InterER(N,k,k)
            elif choice == 'RR' :
                G = InterRR(N,k,k)
            elif choice == 'SF3' :
                G = InterSF(N,k,k,3)
            elif choice == 'SF2.7':
                G = InterSF(N,k,k,2.7)
            elif choice == 'SF2.3':
                G = InterSF(N,k,k,2.3)
            else : print ("No such choice")

            to_be_removed = int(N * (1-p))

            # initial attack subnetwork a
            G.remove_corresp(G.attack_random(Q=to_be_removed))
            G.cascade()
            print(nx.number_of_nodes(G.Ga))
            f.write(str(p) + '\t{0.frac_lmcc}\n'.format(G))


if __name__ == "__main__":
    main('SF3')

