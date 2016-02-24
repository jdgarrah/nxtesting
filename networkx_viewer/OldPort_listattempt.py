import networkx as nx 
from networkx_viewer import Viewer 

## initialize Graph ##
G=nx.Graph()

## initalize some numerical lists ## 
i=0
numlist = []
while i <= 44 :
	i+=1
	numlist.append(i)
print numlist ## this list contains numbers 1-45, for all my nodes

masterlist = []
for n in numlist :
	masterlist.append(numlist)
print masterlist

for n in masterlist :
	G.add_edge(n,(n+1)) ## rue notre dame o, rue st-sulspice, rue de la commune, rue mcgill

#G.add_edge(3,27)
for n in range(0,5):
	G.add_edge(3[n],3[n+1]) 
#G.add_edge(32,13) ## rue st-pierre

#for n in range(0,1) :
#	G.add_edge(2[n],2[n+1])


## Viewer App ##
app=Viewer(G)
app.mainloop()
