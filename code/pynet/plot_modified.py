import numpy as np
import matplotlib.pyplot as plt

#data_n4000 = np.loadtxt('average.dat')
#data_n64000 = np.loadtxt('N64000.dat')
data = np.genfromtxt('./analysis/avg_sd_30000_kavg4_rep2_choiceSF3_typeRandom.dat', 
    delimiter = '\t', skip_header=True)
plt.subplot(2, 1, 1)
#plt.plot(data_rr[:,0], data_rr[:,1], '.',  label='N = 50,000, rep = 10')
#plt.ylabel(r'$n_\infty$')
plt.plot(data[:,0], data[:,1], marker='o', markeredgewidth=0.0, 
    markeredgecolor ='#191970',linestyle='None',color= '#191970', 
    label='N=30000, rep=2')

plt.legend(loc=2)


plt.subplot(2, 1, 2)
#plt.plot(data_n64000[:,0], data_n64000[:,1], 'o-', label='N = 64,000, avg = 1')
#plt.legend(loc=2)
plt.errorbar(data[:,0],data[:,1],yerr=data[:,2],xerr=None,linestyle='-')
plt.xlabel(r'$p$')
plt.ylabel(r'$P_\infty$')
plt.savefig('../../plot/N30000_rep2_SF3.png', bbox_inches='tight')
