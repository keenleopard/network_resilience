from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy
import sys
from classes import Inter_Network
from classes import InterSF
from classes import InterRR
from classes import InterER

wdir = 'data'
def main(choice,n):
    N = int(n)
    k = 4
    if choice == '3' :
        G0 = InterSF(N,k,k,3)
    elif choice == '2.7':
        G0 = InterSF(N,k,k,2.7)
    elif choice == '2.3':
        G0 = InterSF(N,k,k,2.3)
    else : print ("No such choice")

    G0 = InterSF(N,k,k,2.3)

    with open('{0}/N{1}_choice{2}_SF.dat'.format(wdir, N, choice), 'w') as f:
        f.write('# p\t frac_lmcc_rr\n')
        for p in np.linspace(0.55, 0.7, num=100):

            to_be_removed = int(N * (1-p))
            G = copy.deepcopy(G0) # for each p copy once
            # initial attack subnetwork a
            G.remove_corresp(G.attack_random(Q=to_be_removed))
            G.cascade()
            #print(nx.number_of_nodes(G.Ga))
            f.write(str(p) + '\t{0.frac_lmcc}\n'.format(G))


#if __name__ == "__main__":
main(sys.argv[1],sys.argv[2])