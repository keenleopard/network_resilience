from __future__ import division, print_function
import numpy as np
import sys
#file name = 'N1000_kavg4_rep10_choiceER_typeBetweenness_orderHH'
#sys.argv[1] = 1000 (N)
#sys.argv[2] = 10 (rep)
#sys.argv[3] = 'ER' (choice)
#sys.argv[4] = Betweenness_orderHH (type)
#sys.argv[5] = './data/' (path)
#(future)sys.argv[6] = 'random' or 'crucial' (attack)

#we change x axis to be (1-p)
#the standard deviation is for the mean: sigma/sqrt(rep)
wdir = sys.argv[5]
data = np.loadtxt(wdir+'N'+sys.argv[1]+'_kavg4_rep'
    +sys.argv[2]+'_choice'+sys.argv[3]+'_type'+sys.argv[4]+'.dat')
rep = int(sys.argv[2])
with open('./analysis/avg_sd_'+sys.argv[1]+'_kavg4_rep'
    +sys.argv[2]+'_choice'+sys.argv[3]+'_type'+sys.argv[4]+'.dat', 'w') as f:

    f.write('1-p\tavg_frac_lmcc\tsd\n')
    for line in range(len(data)) :
        avg = np.mean(data[line,1:])
        sd_of_mean = np.std(data[line,1:])/np.sqrt(rep)
        #print(line,avg,sd_of_mean)
        #f.write(str(1-data[line,0]/4.)+'\t'+ str(avg)
                #+'\t' + str(sd_of_mean) + '\n')
        f.write(str(data[line,0])+'\t'+ str(avg)
                +'\t' + str(sd_of_mean) + '\n')

