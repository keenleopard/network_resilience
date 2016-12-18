from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy
import time
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
wdir = 'data'

N = int(sys.argv[1])
k_avg = 4
rep = int(sys.argv[2])

if sys.argv[3] == 'RR':
    G0 = InterRR(N, k_avg, k_avg)
elif sys.argv[3] == 'ER':
    G0 = InterER(N, k_avg, k_avg)
else : print("No such choice")

with open('{0}/N{1}_kavg{2}_rep{3}_choice{4}_typeRandom.dat'.format(wdir, N,
    k_avg, rep, sys.argv[3]), 'w') as f:
    f.write('# created on %s\n' %time.strftime("%H:%M\t%d/%m/%Y"))
    f.write('# p*<k>\t frac_lmcc\n')
    count = 0
    #for p in np.linspace(0.15, 0.8, num=100):# different p same graph
    for p in np.linspace(float(sys.argv[4]), float(sys.argv[5]), num = int(sys.argv[6])):
        count += 1
        print(count)
        fraction_list = []
        to_be_removed = int(N * (1-p))

        for i in range(rep):
            G = copy.deepcopy(G0) # same graph
            G.remove_corresp(G.attack_random(Q=to_be_removed))
            G.cascade()
            fraction_list.append(G.frac_lmcc)
        f.write(str(round(p*k_avg, 4))
                + '\t'
                + '\t'.join(str(round(x, 4)) for x in fraction_list)
                + '\n')

#if __name__ == "__main__":
    #main()
