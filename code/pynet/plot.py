import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('output/frac_lmcc.dat')

plt.figure()
plt.plot(data[:,0], data[:,1], '.', label='N = 64,000')
plt.xlabel(r'$p \left< k \right>$')
plt.ylabel(r'$n_\infty$')
plt.legend(loc=2)
plt.show()
