import numpy as np
import matplotlib.pyplot as plt

data_n4000 = np.loadtxt('frac_lmccER.dat')
#data_n64000 = np.loadtxt('N64000.dat')

#plt.subplot(2, 1, 1)
plt.plot(data_n4000[:,0], data_n4000[:,1], '.',  label='N = 4,000, avg = 10')
plt.ylabel(r'$n_\infty$')
plt.legend(loc=2)


#plt.subplot(2, 1, 2)
#plt.plot(data_n64000[:,0], data_n64000[:,1], 'o-', label='N = 64,000, avg = 1')
#plt.legend(loc=2)
#plt.xlabel(r'$p \left< k \right>$')
#plt.ylabel(r'$n_\infty$')
plt.savefig('ER_n4000.pdf', bbox_inches='tight')


#plt.show()
