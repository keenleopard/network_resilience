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
#sys.argv[1] = N
#sys.argv[2] = rep
#sys.argv[3] = choice
#sys.argv[4] = p start
#sys.argv[5] = p end
#sys.argv[6] = number of p

def main():
    N = int(sys.argv[1])
    k = 4
    rep = int(sys.argv[2])
    choice = sys.argv[3]
    p_start = float(sys.argv[4])
    p_end = float(sys.argv[5])
    num_p = int(sys.argv[6])
    wdir = './data'
    if choice == '3' :
        G0 = InterSF(N,k,k,3)
    elif choice == '2.7':
        G0 = InterSF(N,k,k,2.7)
    elif choice == '2.3':
        G0 = InterSF(N,k,k,2.3)
    else : print ("No such choice")
    #with open('frac_lmccSF'+choice+'_node'+str(N)+'.dat', 'w') as f:
    with open('{0}/N{1}_kavg{2}_rep{3}_choiceSF{4}_typeRandom.dat'.format(wdir,
    N, k, rep, choice), 'w') as f:
#        f.write('# created on %s\n' %time.strftime("%H:%M\t%d/%m/%Y"))
        f.write('# 1-p\t frac_lmcc_sf\n')
        count = 0
        #for p in np.linspace(0.55, 0.7, num=25):
        for p in np.linspace(p_start, p_end, num=num_p):
            count+=1
            print(count)
            fraction_list = []
            to_be_removed = int(N * (1-p))

            for i in range(rep):
                G = copy.deepcopy(G0) # for each p copy once
                # initial attack subnetwork a
                G.remove_corresp(G.attack_random(Q=to_be_removed))
                G.cascade()
                fraction_list.append(G.frac_lmcc)
            f.write(str(1-p) + '\t{0.frac_lmcc}\n'.format(G))
            f.write(str(1-p)
                + '\t'
                + '\t'.join(str(round(x, 4)) for x in fraction_list)
                + '\n')

if __name__ == "__main__":
    main()
