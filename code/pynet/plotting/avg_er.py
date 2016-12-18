#find the average and standard deviation of repetitive results

from __future__ import division, print_function
import numpy as np
data = []
data.append(np.loadtxt('./data/N1000_kavg4_rep10_ER.dat'))
data.append(np.loadtxt('./data/N2000_kavg4_rep10_ER.dat'))
data.append(np.loadtxt('./data/N4000_kavg4_rep10_ER.dat'))
data.append(np.loadtxt('./data/N8000_kavg4_rep10_ER.dat'))
data.append(np.loadtxt('./data/N16000_kavg4_rep10_ER.dat'))
#data.append(np.loadtxt('./data/N32000_kavg4_rep10_ER.dat'))
#data.append(np.loadtxt('./data/N64000_kavg4_rep10_ER.dat'))
rep = len(data[0][0]) - 1

for i in range(len(data)):
    with open('avg_sd_er_'+str(i)+'.dat', 'w') as f:
        f.write('#p*<k>\tavg_frac_lmcc\tsd\n')
        #f.write('p\tavg_frac_lmcc\tsd\n')    
        d = data[i]
        for line in range(len(d)):
            avg = np.mean(d[line,1:])
            sd = np.std(d[line,1:])
            print(line)
            f.write(str(d[line,0])+'\t'+ str(avg)
                +'\t' + str(sd) + '\n')


