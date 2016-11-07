from __future__ import division, print_function

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy


from classes import InterER

def main():
    N = 400
    k_avg = 4
    rep = 1
    G0 = InterER(N,k_avg,k_avg)

    with open('frac_lmcc.dat', 'w') as f:
        f.write('# p*<k>\t frac_lmcc\n')
        count = 0
        for p in np.linspace(0.59, 0.63, num=100):
            count += 1
            print(count)
            fraction_list = []
            to_be_removed = int(N * (1-p))

            for i in range(rep):
                G = copy.deepcopy(G0)
                G.one2one()
                G.fail(Q=to_be_removed)
                G.cascade()
                fraction_list.append(G.frac_lmcc)
            f.write(str(round(p*k_avg, 4))
                    + '\t'
                    + '\t'.join(str(round(x, 4)) for x in fraction_list)
                    + '\n')

if __name__ == "__main__":
    main()

