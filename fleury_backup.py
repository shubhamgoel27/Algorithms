# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 18:49:36 2014

@author: shubhamgoel
"""
from networkx import nx
import random

G = nx.Graph()
nodes = ['a','b','c','d','e','f','g']
G.add_nodes_from(nodes)
edges = [('a','b'),('a','f'),('c','b'),('c','d'),('d','g'),('g','f'),('f','e'),('e','d')]
G.add_edges_from(edges)
G.remove_node('g')   #Commenting this line out will make the graph not have an Eulerian circuit

def degree_check_eulerian_circuit(G):
    for node in G.nodes():
        if not G.degree(node)%2 ==0:
            return False
    return True        
    

     
def eulerian(G):    
    if not degree_check_eulerian_circuit(G):
        return 'No Eulerian circuit because all vertices do not have even degree'
    circuit = nx.Graph()  
    #create a copy of G so that original G doesn't get affected
    copy = G.__class__(G)
    #choose random node
    node = copy.nodes()[random.randrange(0,len(copy.nodes()))]
    circuit.add_node(node)
    i=0
    while copy:        
        rand_num = random.randrange(0,len(copy.neighbors(node)))
        neighbour_edge = copy.neighbors(node)[rand_num]
        #move to one of it's neighbours
        second_copy = copy.__class__(copy)  #Create another copy
        second_copy.remove_edge(node,neighbour_edge) #Remove the edge from this copy
        for second_node in second_copy.nodes():      #Remove nodes with degree 0 in second_copy
            if second_copy.degree(second_node) ==0:
                second_copy.remove_node(second_node)
        if second_copy: #Checks to see if graph is not empty            
            if nx.is_connected(second_copy):  #Check connectedness of graph
                circuit.add_edge(node,neighbour_edge)
                copy.remove_edge(node,neighbour_edge)
                node = neighbour_edge
                i+=1
               
        if len(copy.edges())==1:  #For the final edge in copy, delete it
            edge = copy.edges()
            #print ' The last edge is ' + str(edge)
            copy.remove_edge(edge[0][0],edge[0][1])
            circuit.add_edge(edge[0][0],edge[0][1])
            return circuit
    return circuit        
        
    #remove the corresponding edge from graph
    #check if the remaining graph is connected. If not, move to another neighbour
    #repeat previous 3 steps until the copy of graph becomes empty     
    
final = eulerian(G)
if type(final)==str:
    print final
else:
    nx.draw(final)    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    