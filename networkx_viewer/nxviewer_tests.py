import networkx as nx 
from networkx_viewer import Viewer

## a fcn ##
def n_disjoint_unions(G,n) :
        """A function that takes a nx graph G and 'tiles' it by creating a \
	disjoint union between it and n copies of itself. To connect these \
	iterations of G, it then checks for nodes of lesser degrees of     \
	connectivity and adds edges between them"""
        H= nx.Graph()
        lessthanlist=[]
        for i in range(n) :
                H=nx.disjoint_union(H,G)
        for i in H.nodes() :
                if nx.degree_centrality(H)[i] < .1 :
                        print i
                        print "has degree <.1"
                        lessthanlist.append(i)
        for i in range(len(lessthanlist)-4) :
                H.add_edge(lessthanlist[i], lessthanlist[(i+4)])
                print lessthanlist[i]
                  
        print lessthanlist
        #print nx.degree_centrality(H) 
        return H

## first undirected graph ##
## a simple two block by one block grid system ##
G=nx.Graph()
G.add_edge('a','b')
G.add_edge('a','c')
G.add_edge('a','z')
G.add_edge('z','d')
G.add_edge('z','y')
G.add_edge('y','e')
G.add_edge('y','c')
G.add_edge('z','w')
G.add_edge('w','f')
G.add_edge('w','b')
G.add_edge('d','e')
G.add_edge('d','f')

#app=Viewer(G)
#app.mainloop() ## take an initial look @ G


### some algorithms ##
##degree = nx.degree_centrality(G) ## returns: dict of nodes with fraction
##                                 ## of nodes they are connected to
##print degree
##
##adict = []
##for n in G.nodes_iter() :
##        if degree[n] < 0.5 :
##                adict.append(n)
##        else:
##                continue
##
##print adict
##
##for n in adict :
##        i = 0
##        G.add_edge(n,i)
##        i += 1
##
#### Run Viewer ##
##app=Viewer(G)
##app.mainloop()


## tiling attempts ##

#### A graph H ##
##H=nx.Graph()
##H.add_edge('z','w')
##H.add_edge('z','q')
##H.add_edge('z','x')
##H.add_edge('x','y')
##H.add_edge('q','y')
##H.add_edge('x','u')
##H.add_edge('w','u')

#J=nx.Graph()
#J.add_edge('f','q')
#J.add_edge('d','z')
#J.add_edge('e','w')

#app=Viewer(H)
#app.mainloop()


## a union ##
#U = nx.Graph()
#U.add_edges_from(G.edges(data=True)+H.edges(data=True))

##U=nx.intersection(G,H)
###Ux=nx.disjoint_union(U,J)
##print U.nodes()
##app=Viewer(U)
##app.mainloop()

## MAIN ##
n = 3
T = n_disjoint_unions(G,n)

app=Viewer(T)
app.mainloop()

## I think it works!! Here is a quick rundown of the current process: takes a nx graph G and creates a disjoint union of G
## w itself n times. Then, looks thru the nodes of the new graph H and considers the degree centrality. This indicates
## that it is on the outside of the graph and can be connected to another. If it is sufficiently
## small, it adds it to a list of nodes w small degree. Then, scans thru this created list, adding edges between small degree nodes
## on each iteration of original G.

## ISSUES: 1) There are a couple nodes w less connections to other iterations, namely the first and last ones considered.
##         2) Will it work for n v large? (works n=3,5) DOES NOT WORK n=2 (a hardcoded pbm) (.1 is ideal for n=3 only)
##         3) The < value for degree centrality is currently hardcoded, based on my small test graph. Will need to be adjusted
##            for an actual street network. Is there a way to generalize this variable or should be determined empirically for each case?
##         4) A solution to above? Parse thru nodes and examine range of values to determine lowest, make if == this value. 

