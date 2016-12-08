import numpy as np
import matplotlib.pyplot as plt
#plt.subplot(2,1,1)
def group_into_four(data) :
    data_4 = []
    for i in range(25) :
        temp = np.array([data[i*4], data[i*4+1], data[i*4+2], data[i*4+3]])
        data_4.append(np.mean(temp, axis = 0))
    return data_4

data = np.genfromtxt('./analysis/avg_sd_ER_1000.dat',delimiter='\t', skip_header=True)
d1 = np.asarray(group_into_four(data))
plt.plot(d1[:,0], d1[:,1],color='#191970', label='N = 1000')

data = np.genfromtxt('./analysis/avg_sd_ER_2000.dat',delimiter='\t', skip_header=True)
d2 = np.asarray(group_into_four(data))
plt.plot(d2[:,0], d2[:,1], color='#4169e1', label='N = 2000')

data = np.genfromtxt('./analysis/avg_sd_ER_4000.dat',delimiter='\t', skip_header=True)
d4 = np.asarray(group_into_four(data))
plt.plot(d4[:,0], d4[:,1], color='#00ced1', label='N = 4000')

data = np.genfromtxt('./analysis/avg_sd_ER_8000.dat',delimiter='\t', skip_header=True)
d8 = np.asarray(group_into_four(data))
plt.plot(d8[:,0], d8[:,1], color='#228b22', label='N = 8000')

data = np.genfromtxt('./analysis/avg_sd_ER_16000.dat',delimiter='\t', skip_header=True)
d16 = np.asarray(group_into_four(data))
plt.plot(d16[:,0], d16[:,1], color='#daa520', label='N = 16000')

data = np.genfromtxt('./analysis/avg_sd_ER_32000.dat',delimiter='\t', skip_header=True)
d32 = np.asarray(group_into_four(data))
plt.plot(d32[:,0], d32[:,1], color='#cd5c5c', label='N = 32000')
'''
data = np.genfromtxt('avg_sd_rr_6.dat',delimiter='\t', skip_header=True)
d2 = np.asarray(group_into_four(data))
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
plt.savefig('../../plot/ER_cluster_generated_data_into4.pdf', bbox_inches='tight')


#plt.show()
