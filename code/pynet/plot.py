import numpy as np
import matplotlib.pyplot as plt

#data_n4000 = np.loadtxt('frac_lmccsf.dat')
#data_n64000 = np.loadtxt('N64000.dat')

#plt.subplot(2, 1, 1)
data = np.loadtxt('frac_lmccSF.dat')
plt.plot(data[:,0], data[:,1], '.',  label='N = 50, rep = 1')
plt.ylabel(r'$n_\infty$')
plt.legend(loc=2)


#plt.subplot(2, 1, 2)
#plt.plot(data_n64000[:,0], data_n64000[:,1], 'o-', label='N = 64,000, avg = 1')
#plt.legend(loc=2)
#plt.xlabel(r'$p \left< k \right>$')
#plt.ylabel(r'$n_\infty$')
plt.savefig('SF3_50nodes.pdf', bbox_inches='tight')


#plt.show()