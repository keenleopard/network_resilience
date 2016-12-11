from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy
import time
import sys
import cProfile
import re
from classes import Inter_Network
from classes import InterSF
from classes import InterRR
from classes import InterER
# ER,RR, HH, HL, DEGREE, BETWEENNESS, CLOSENESS, 1000,2000,4000,
wdir = 'data'
def main(choice,num,type,order_in):
    N = num
    k_avg = 4
    rep = 2
    if choice == 'RR':
        G0 = InterRR(N, k_avg, k_avg)
    elif choice == 'ER':
        G0 = InterER(N, k_avg, k_avg)
    else : print("No such choice")
    
    if order_in == 1:
        order_str = "HH"
    else:
        order_str = "HL"
        
    if type == 0:
        type_str = "Degree"
    elif type == 1:
        type_str = "Betweenness"
    else:
        type_str = "Closeness"
    with open('{0}/N{1}_kavg{2}_rep{3}_choice{4}_type{5}_order{6}.dat'.format(wdir, N, k_avg, rep, choice,type_str,order_str), 'w') as f:
        f.write('# created on %s\n' %time.strftime("%H:%M\t%d/%m/%Y"))
        f.write('# p*<k>\t frac_lmcc\n')
        count = 0
        for p in np.linspace(0.2, 0.85, num=100):# different p same graph
            count += 1
            print('Count: ' + str(count) + ' ' + str(p))
            fraction_list = []
            to_be_removed = int(N * (1-p))

            for i in range(rep):
                G = copy.deepcopy(G0) # same graph
                G.remove_corresp(failed_nodes=G.attack_special(to_be_removed, type), order=order_in)
                G.cascade(order = order_in)
                fraction_list.append(G.frac_lmcc)
            f.write(str(round(p*k_avg, 4))
                    #str(p)
                    + '\t'
                    + '\t'.join(str(round(x, 4)) for x in fraction_list)
                    + '\n')

if __name__ == "__main__":

    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
