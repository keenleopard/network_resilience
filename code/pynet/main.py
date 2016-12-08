from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy
import time
from classes import Inter_Network
from classes import InterSF
from classes import InterRR
from classes import InterER

wdir = 'data'
def main(choice = 'RR'):
    N = 16000
    k_avg = 4
    rep = 10

    if choice == 'RR':
        G0 = InterRR(N, k_avg, k_avg)
    elif choice == 'ER':
        G0 = InterER(N, k_avg, k_avg)
    else : print("No such choice")

    with open('{0}/N{1}_kavg{2}_rep{3}_ER.dat'.format(wdir, N, k_avg, rep), 'w') as f:
        f.write('# created on %s\n' %time.strftime("%H:%M\t%d/%m/%Y"))
        f.write('# p*<k>\t frac_lmcc\n')
        count = 0
        for p in np.linspace(0.59, 0.625, num=100):# different p same graph
            count += 1
            print(count)
            fraction_list = []
            to_be_removed = int(N * (1-p))

            for i in range(rep):
                G = copy.deepcopy(G0) # same graph
                #G.one2one()
                #G.fail(Q=to_be_removed)
                G.remove_corresp(G.attack_random(Q=to_be_removed))
                G.cascade()
                fraction_list.append(G.frac_lmcc)
            f.write(str(round(p*k_avg, 4))
                    #str(p)
                    + '\t'
                    + '\t'.join(str(round(x, 4)) for x in fraction_list)
                    + '\n')

if __name__ == "__main__":
    main('ER')
