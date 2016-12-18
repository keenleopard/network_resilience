from __future__ import division, print_function

import numpy as np
import copy
import time
import sys
from classes import InterRR
from classes import InterER
wdir = 'data'


def main(choice,num,type_in,order_in):
    N = num
    k_avg = 4
    rep = 2

    if choice == 'RR':
        G0 = InterRR(N, k_avg, k_avg)
    elif choice == 'ER':
        G0 = InterER(N, k_avg, k_avg)
    else:
        print("No such choice")

    if order_in == 0:
        order_str = "HH"
    elif order_in == 1:
        order_str = "HL"

    if type_in == 0:
        type_str = "Degree"
    elif type_in == 1:
        type_str = "Betweenness"
    elif type_in == 2:
        type_str = "Closeness"
    elif type_in == 3:
        type_str = "Random"

    with open('{0}/N{1}_kavg{2}_rep{3}_choice{4}_type{5}_order{6}_TMP.dat'.format(wdir, N, k_avg, rep, choice,type_str,order_str), 'w') as f:
        f.write('# created on %s\n' %time.strftime("%H:%M\t%d/%m/%Y"))
        f.write('# p*<k>\t frac_lmcc\n')
        count = 0
        nbr = 0
        """1-p is the fraction of nodes we remove We choose 100 p values evenly distributed between the given range"""
        for p in np.linspace(0.2, 0.85, num=100):
            count += 1

            "Output Progress Bar"
            sys.stdout.write('\r')
            if count % 10 == 1:
                nbr += 1
            sys.stdout.write("Status: [%s %s] %d" %("=" * nbr, " " * int(9-nbr), count))

            sys.stdout.flush()
            fraction_list = []
            to_be_removed = int(N * (1-p))

            """For a specific fraction of nodes, we redo the experiment several times on the same initial graph"""
            for i in range(rep):
                G = copy.deepcopy(G0)
                G.remove_corresp(failed_nodes=G.attack_random(to_be_removed, type_in), order=order_in)
                G.cascade(order=order_in)
                fraction_list.append(G.frac_lmcc)
            f.write(str(round(p*k_avg, 4))
                    + '\t'
                    + '\t'.join(str(round(x, 4)) for x in fraction_list)
                    + '\n')
            if count == 100:
                print("")

if __name__ == "__main__":
    """arguments: Choice (RR/ER), Number of Nodes, Type of Mapping (Degree, Betweenness, Closeness, Random),
    Order of Mapping (High to High, High to Low)"""
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
