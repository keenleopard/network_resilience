import numpy as np
import matplotlib.pyplot as plt
plt.subplot(2,1,1)
data = np.genfromtxt('avg_sd_rr.dat', delimiter='\t', skip_header=True)#[:, 1:]
plt.plot(data[:,0], data[:,1], '^-', color='#6495ed', label='N = 50000, rep = 10')
plt.xlabel(r'$p$')
plt.ylabel(r'$P_\infty$')
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.errorbar(data[:,0], data[:,1], yerr=data[:,2], marker='^', color='#6495ed', label='N = 50000, rep = 10')
plt.legend(loc='best')
plt.xlabel(r'$p$')
plt.ylabel(r'$P_\infty$')
plt.savefig('RR.pdf', bbox_inches='tight')


#plt.show()
