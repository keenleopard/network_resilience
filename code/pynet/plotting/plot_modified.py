import numpy as np
import matplotlib.pyplot as plt

data_er = np.genfromtxt('./analysis/avg_sd_50000_kavg4_rep2_choiceER_typeRandom.dat', delimiter = '\t', skip_header=True)
data_rr = np.genfromtxt('./analysis/avg_sd_50000_kavg4_rep10_choiceRR_typeRandom.dat', delimiter = '\t', skip_header=True)
data_SF3 = np.genfromtxt('./analysis/avg_sd_30000_kavg4_rep2_choiceSF3_typeRandom.dat', delimiter = '\t', skip_header=True)
data_SF27 = np.genfromtxt('./analysis/avg_sd_30000_kavg4_rep2_choiceSF2.7_typeRandom.dat',  delimiter = '\t', skip_header=True)

#plt.plot(data[:,0], data[:,1], marker='o', markeredgewidth=0.0, 
    #markeredgecolor ='#191970',linestyle='None',color= '#191970', 
    #label='N=30000, rep=2')

#plt.legend(loc=2)


#plt.subplot(2, 1, 2)
#plt.plot(data_n64000[:,0], data_n64000[:,1], 'o-', label='N = 64,000, avg = 1')

plt.errorbar(data_er[:,0],data_er[:,1],marker='.',yerr=data_er[:,2],xerr=None, color = 'b', label='ER, N=50000, rep=2')
plt.errorbar(data_rr[:,0],data_rr[:,1],yerr=data_rr[:,2],xerr=None,color = 'r',linestyle='-', label='RR, N=50000, rep=10')
plt.errorbar(data_SF3[:,0],data_SF3[:,1],yerr=data_SF3[:,2],xerr=None,color = 'y',linestyle='-', label='SF3, N=30000, rep=2')
plt.errorbar(data_SF27[:,0],data_SF27[:,1],yerr=data_SF27[:,2],xerr=None,color = 'g',linestyle='-', label='SF2.7, N=30000, rep=2')

plt.legend(loc=2)
plt.xlabel(r'$1-p$')
plt.ylabel(r'$P_\infty$')
plt.savefig('../../plot/RR-50000.png', bbox_inches='tight')
