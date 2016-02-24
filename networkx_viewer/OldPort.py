import networkx as nx 
from networkx_viewer import Viewer 

## initialize Graph ##
G=nx.Graph()

## initalize some numerican lists ## 
i=0
numlist = []
while i <= 44 :
	i+=1
	numlist.append(i)
print numlist ## this list contains numbers 1-45, for all my nodes

for n in range(1,19) :
	G.add_edge(n,(n+1)) ## rue notre dame o, rue st-sulspice, rue de la commune, rue mcgill

G.add_edge(2,21)
for n in range(21,22):
	G.add_edge(n,(n+1)) # rue st-helene

G.add_edge(3,31)
for n in range(31,36):
		G.add_edge(n,(n+1)) ## rue st-pierre
G.add_edge(36,13)

G.add_edge(4,41) 
G.add_edge(41,42) ##

G.add_edge(5,51)
for n in range(51,57) :
	G.add_edge(n,(n+1))
G.add_edge(57,12) ## rue st jean, rue du port 

G.add_edge(6,61)
for n in range(61,65) :
	G.add_edge(n,(n+1))
G.add_edge(65,11) ## 


## Viewer App ##
app=Viewer(G)
app.mainloop()
