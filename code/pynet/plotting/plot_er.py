import numpy as np
import matplotlib.pyplot as plt
#plt.subplot(2,1,1)

data = np.genfromtxt('avg_sd_er_0.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1],color='#191970', label='N = 1000')
data = np.genfromtxt('avg_sd_er_1.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1], color='#4169e1', label='N = 2000')
data = np.genfromtxt('avg_sd_er_2.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1], color='#00ced1', label='N = 4000')
data = np.genfromtxt('avg_sd_er_3.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1], color='#228b22', label='N = 8000')
data = np.genfromtxt('avg_sd_er_4.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1], color='#daa520', label='N = 16000')
'''
data = np.genfromtxt('avg_sd_rr_5.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1],'#cd5c5c', '-', label='N = 32000')
data = np.genfromtxt('avg_sd_rr_6.dat',delimiter='\t', skip_header=True)
plt.plot(data[:,0], data[:,1],'#ee82ee','-', label='N = 64000')
'''
plt.xlabel(r'$p$')
plt.ylabel(r'$P_\infty$')
plt.legend(loc='best')
'''
plt.subplot(2, 1, 2)
plt.errorbar(data[:,0], data[:,1], yerr=data[:,2], marker='^', color='#6495ed', label='N = 50000, rep = 10')
plt.legend(loc='best')
plt.xlabel(r'$p$')
plt.ylabel(r'$P_\infty$')
'''
plt.savefig('ER.pdf', bbox_inches='tight')


#plt.show()
