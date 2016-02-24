import networkx as nx 
from networkx_viewer import Viewer 

## a fcn ##
def n_disjoint_unions(G,n) :
        """A function that takes a nx graph G and 'tiles' it by creating a \
	disjoint union between it and n copies of itself. To connect these \
	iterations of G, it then checks for nodes of lesser degrees of     \
	connectivity and adds edges between them"""
        H= nx.Graph()
        lowdeg=[]
        for i in range(n) :
                H=nx.disjoint_union(H,G)
        for i in H.nodes() :
                if nx.degree_centrality(H)[i] < .1 :
                        print i
                        print "has degree <.1"
                        lowdeg.append(i)
        for i in range(len(lowdeg)-4) :
                H.add_edge(lowdeg[i], lowdeg[(i+4)])
                print lowdeg[i]
                  
        print lowdeg
        #print nx.degree_centrality(H) 
        return H
# end fcn 

# creating a simple graph #
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

# to be simplified. screwed up from some testing. 

## MAIN ##
n = 3
T = n_disjoint_unions(G,n)

app=Viewer(T)
app.mainloop()

# et voila 
# end pgm 
# Some Discussion: I think it works!! Here is a quick rundown of the current process: takes a nx graph G and creates a disjoint union of G
## w itself n times. Then, looks thru the nodes of the new graph H and considers the degree centrality. This indicates
## that it is on the outside of the graph and can be connected to another. If it is sufficiently
## small, it adds it to a list of nodes w small degree. Then, scans thru this created list, adding edges between small degree nodes
## on each iteration of original G.

## ISSUES: 1) There are a couple nodes w less connections to other iterations, namely the first and last ones considered.
##         2) Will it work for n v large? (works n=3,5) DOES NOT WORK n=2 (a hardcoded pbm) (.1 is ideal for n=3 only)
##         3) The < value for degree centrality is currently hardcoded, based on my small test graph. Will need to be adjusted
##            for an actual street network. Is there a way to generalize this variable or should be determined empirically for each case?
##         4) A solution to above? Parse thru nodes and examine range of values to determine lowest, make if == this value. 
