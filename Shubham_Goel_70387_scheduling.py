# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:32:30 2014

@author: shubhamgoel
"""
import networkx as nx

G = nx.Graph()
nodes = ['a','b','c','d','e','f','g']
G.add_nodes_from(nodes)
#edges = [('a','b'),('a','f'),('c','b'),('c','d'),('d','g'),('g','f'),('f','e'),('e','d')]
edges = [('a','h'),('a','f'),('h','b'),('h','i'),('b','c'),('c','i'),('i','f'),('f','k'),('k','g'),('j','k'),('j','e'),('g','e'),('e','d'),('c','d')]
G.add_edges_from(edges)
def scheduling(graph):
    """Takes input of a graph and returns a list with each element containing all
        those vertices which can work together at the same time"""    
    final_list = []         #Final list which contains schedules of all nodes
    count=0                     #Counter to keep track of the number of steps
    while True:
        count+=1            
        copy = graph.__class__(graph)  
        if len(final_list) !=0:
            for j in range(len(final_list)):
                copy.remove_nodes_from(final_list[j])
                #Removing nodes covered in previous iteration
        print copy.nodes()        
        if not copy:        #If copy has no nodes left, stop the code. Result is reached
            break                    
        task_list = []          #List to store vertices being covered in this iteration
        while copy:    
            deg_seq = nx.degree(copy).values()  #Store degree sequence of graph
            index = deg_seq.index(min(deg_seq)) #Find index of min degree vertex
            node = copy.nodes()[index]          #Choose vertex with corresponding index
                                 
            task_list.append(node)              #Adding node to this list
            neighbours = copy.neighbors(node)   
            copy.remove_node(node)              #Removing the node for this iteration
            copy.remove_nodes_from(neighbours)  #Removing its neighbors for this iteration
        print "Vertices in iteration number " + str(count) + ": " + str(task_list)
        final_list.append(task_list)    
    return final_list
    
print scheduling(G)   # Demo of the function on the graph discussed in class    