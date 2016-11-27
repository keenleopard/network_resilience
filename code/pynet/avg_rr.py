#find the average and standard deviation of repetitive results

from __future__ import division, print_function
import numpy as np

data = np.loadtxt('./data/N50000_kavg4_rep10.dat')
rep = len(data[0]) - 1

with open("avg_sd_rr.dat", 'w') as f:
    #f.write('#p*<k>\tavg_frac_lmcc\tsd\n')
    f.write('p\tavg_frac_lmcc\tsd\n')
    for line in range(len(data)):
        avg = np.mean(data[line,1:])
        avg2 = 0
        sd = np.std(data[line,1:])
        print(line)
        #for i in range(rep):
            ##print(data[line,i+1])
            #avg += data[line, i+1]
            #avg2 += data[line, i+1]**2
        #avg /= rep
        #avg2 /= rep
        #sd = np.sqrt(avg2 - avg**2)
        f.write(str(data[line,0])+'\t'+ str(avg)
                +'\t' + str(sd) + '\n')
