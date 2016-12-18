import numpy as np
import matplotlib.pyplot as plt
# random er 4000
data = np.genfromtxt('./analysis/avg_sd_ER_4000.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1], color='#00ced1', label='N=4000, Random')

# degree high 4000
data2 = np.loadtxt('./analysis/avg_sd_ER_4000_DH.dat')
plt.plot(data2[:,0], data2[:,1], '-',  label='N=4000, Degree H2H')


plt.xlabel(r'$p*<k>$')
plt.ylabel(r'$P_\infty$')
plt.legend(loc='best')


plt.savefig('ER_4000nodes_all.pdf', bbox_inches='tight')
