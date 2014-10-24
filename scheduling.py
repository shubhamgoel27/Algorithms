import operator
graph  = {'a':['b','c'],
		  'b': ['d','f'],
		  'c': ['f','a'],
		  'f':['a','c'],
		  'd':['b','c','e']}

def find_path(graph, start, end, path=[]):
       path = path + [start]
       if start == end:
           return path
       if not graph.has_key(start):
           return None
       for node in graph[start]:
           if node not in path:
               newpath = find_path(graph, node, end, path)
               if newpath: return newpath
       return None		  
degree = {}
for node in graph:
	degree[node] = len(graph[node])

sequence = sorted(degree.iteritems(), key=operator.itemgetter(1))

final = [[],[],[],[],[],[]]
for i in range(6):
	copy = graph
      for i in range(2):
	#while copy:
		degree = {}
		for node in copy:
			degree[node] = len(copy[node])
		sequence = sorted(degree.iteritems(), key=operator.itemgetter(1))
		if final[i]:
			final[i]+=sequence[0][0]
		else:
			final[i] = sequence[0][0]	
		print final[i]
		copy.pop(final[i][0],None)

#print final

#print find_path(graph,'a','f')
