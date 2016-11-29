import os
N_values = [1000,2000,4000,8000,16000,32000,64000]
graph_type = ["ER","RR"]
for q in graph_type:
	for x in N_values:
		os.system('bsub \"python3 main.py '+ q + ' ' + str(x)+" \" ")

graph_type = ["3","2.7","2.3"]
for q in graph_type:
	for x in N_values:
		#print('bsub \"python3 main.py '+ q + ' ' + str(x)+"\"")
		os.system('bsub \"python3 main.py '+ q + ' ' + str(x)+"\"")
