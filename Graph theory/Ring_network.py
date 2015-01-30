def make_node(G, node1, node2):
	if node1 not in G:
		G[node1]= {}
	G[node1][node2] = 1	
	if node2 not in G:
		G[node2] = {}
	G[node2][node1] = 1	
	return G

ring = {}

n=6 #number of sides

for i in range(n):
	make_node(ring,chr(65+i),chr(65+((i+1)%n)))

#total number of edges
print sum([len(ring[node]) for node in ring.keys()])/2

print ring		


