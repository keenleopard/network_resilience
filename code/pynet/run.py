import os
N_values = [1000,2000,4000]
graph_type = ["ER","RR"]
types = [0,1,2]
order = [1,2]
for q in graph_type:
	for x in N_values:
		for z in types:
			for p in order:
				os.system('python3 main.py '+ q + ' ' + str(x) + ' ' + str(z) + ' ' + str(p))
