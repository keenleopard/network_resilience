import numpy as np
import matplotlib.pyplot as plt
#import sys

#file name = 'avg_sd_1000_kavg4_rep2_choiceER_typeBetweenness_orderHH'
#sys.argv[1] = 'N' (different N same choice same type)
#              'choice' (same N different choice same type)
#              'type' (same N same choice different type) 
#if 'type':
#sys.argv[2] = 1000 (N)
#sys.argv[3] = 'ER' (choice)
#sys.argv[4] = 100 (rep for Random)
#if 'N':
#sys.argv[2] = 'ER' (choice)
#sys.argv[3] = Betweenness_orderHH (type)
#sys.argv[4] = 100 (rep for Random)
#if 'choice':
#sys.argv[2] = 1000 (N)
#sys.argv[3] = Betweenness_orderHH (type)
#sys.argv[4] = 100 (rep for Random)
def plot_func(Input, N, choice, Type, rep_for_Random):
if Input == 'type' :
    typelist = ['Degree_orderHL', 'Betweenness_orderHL',
        'Closeness_orderHL', 'Random', 'Degree_orderHH', 
        'Betweenness_orderHH','Closeness_orderHH']
    markerlist = ['o', 'o', 'o', '^', 'o', 'o', 'o']
    colorlist = ['#191970', '#4169e1', '#00ced1', '#ee82ee','#228b22',
        '#daa520', '#cd5c5c']
    replist = ['2','2','2',rep_for_Random, '2', '2', '2']

    for i in range(len(typelist)):
        data = np.genfromtxt('./analysis/avg_sd_'+N+'_kavg4_rep'
            +replist[i]+'_choice'+choice+'_type'+typelist[i]+'.dat',
            delimiter='\t', skip_header=True)
        plt.plot(data[:,0], data[:,1], marker=markerlist[i], markeredgewidth=0.0,
            markeredgecolor=colorlist[i], linestyle='None', color=colorlist[i], 
            label='type = '+typelist[i]+', rep = '+replist[i])
    
    #plt.xlabel(r'$1-p$')
    #plt.ylabel(r'$P_\infty$')
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #title = 'N = '+sys.argv[2]+' choice = '+sys.argv[3]+' Different types'
    #plt.title(title)
    #plt.savefig('../../plot/N'+sys.argv[2]+'_choice'+sys.argv[3]
        #+'_Different_types.png', bbox_inches='tight')

if sys.argv[1] == 'N' :
    if sys.argv[3] == 'Smallp':
        if sys.argv[2] == 'ER' :
            Nlist = [1000, 2000, 4000, 8000, 16000, 32000, 64000]
            colorlist = ['#191970', '#4169e1', '#00ced1', '#ee82ee','#228b22',
                '#daa520', '#cd5c5c']
            replist = [100, 25,10,25,10,5,1]
        elif sys.argv[2] == 'RR' :
            Nlist = [1000, 2000, 4000, 8000, 16000, 32000]
            colorlist = ['#191970', '#4169e1', '#00ced1', '#ee82ee','#228b22',
                '#daa520']
            replist = [25, 25,25,25,25,10]

    elif sys.argv[3] == 'Random' : rep = sys.argv[4]
    else : rep = '2'

    for i in range(len(Nlist)):
        data = np.genfromtxt('./analysis/avg_sd_'+str(Nlist[i])+'_kavg4_rep'
            +str(replist[i])+'_choice'+sys.argv[2]+'_type'+sys.argv[3]+'.dat',
            delimiter='\t', skip_header=True) #rep -> replist[i]
        plt.plot(data[:,0], data[:,1], marker='o', markeredgewidth=0.0,
            markeredgecolor=colorlist[i], linestyle='None', color=colorlist[i],
            label='N = '+str(Nlist[i])+', rep = '+str(replist[i]))

    plt.xlabel(r'$1-p$')
    plt.ylabel(r'$P_\infty$')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    title = 'choice = '+sys.argv[2]+' type = '+sys.argv[3]+' Different Ns'
    plt.title(title)
    plt.savefig('../../plot/choice'+sys.argv[2]+'_type'+sys.argv[3]
        +'_Different_Ns.png', bbox_inches='tight')

# plot N and choice together?
if sys.argv[1] == 'choice' :
    choicelist = ['ER', 'RR']
    colorlist = ['#191970', '#cd5c5c']
    if sys.argv[3] == 'Random' : rep = sys.argv[4]
    else : rep = '2'

    for i in range(len(choicelist)):
        data = np.genfromtxt('./analysis/avg_sd_'+sys.argv[2]+'_kavg4_rep'
            +rep+'_choice'+choicelist[i]+'_type'+sys.argv[3]+'.dat',
            delimiter='\t', skip_header=True)
        plt.plot(data[:,0], data[:,1], marker='o', markeredgewidth=0.0,
            markeredgecolor=colorlist[i], linestyle='None', color=colorlist[i],
            label='choice = '+choicelist[i]+', rep = '+rep)

    plt.xlabel(r'$1-p$')
    plt.ylabel(r'$P_\infty$')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    title = 'N = '+sys.argv[2]+' type = '+sys.argv[3]+' Different choices'
    plt.title(title)
    plt.savefig('../../plot/N'+sys.argv[2]+'_type'+sys.argv[3]
        +'_Different_choices.png', bbox_inches='tight')

