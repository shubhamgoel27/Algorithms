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
G.remove_node('g')

def degree_check_eulerian_circuit(G):
    for node in G.nodes():
        if not G.degree(node)%2 ==0:
            return False
    return True        
    
    
    
    
    
def eulerian_circuit(G, source=None):
    """Return the edges of an Eulerian circuit in G.

    An Eulerian circuit is a path that crosses every edge in G exactly once
    and finishes at the starting node.

    Parameters
    ----------
    G : graph
       A NetworkX Graph
    source : node, optional
       Starting node for circuit.

    Returns
    -------
    edges : generator
       A generator that produces edges in the Eulerian circuit.

    
    >>> G=nx.complete_graph(3)
    >>> list(nx.eulerian_circuit(G))
    [(0, 1), (1, 2), (2, 0)]
    >>> list(nx.eulerian_circuit(G,source=1)) 
    [(1, 0), (0, 2), (2, 1)]
    >>> [u for u,v in nx.eulerian_circuit(G)]  # nodes in circuit
    [0, 1, 2]
    """
    #if not degree_check_eulerian_circuit(G):
        #return 'Degree of all vertices is not even. So graph cannot have an Eulerian circuit.'

    g = G.__class__(G) # copy graph structure (not attributes)

    # set starting node
    if source is None:
        v = next(g.nodes_iter())
    else:
        v = source

    while g.size() > 0:
        n = v   
        # sort nbrs here to provide stable ordering of alternate cycles
        nbrs = sorted([v for u,v in g.edges(n)])
        for v in nbrs:
            g.remove_edge(n,v)
            bridge = not nx.is_connected(g.to_undirected())
            if bridge:
                g.add_edge(n,v)  # add this edge back and try another
            else:
                break  # this edge is good, break the for loop 
        if bridge:
            g.remove_edge(n,v)            
            g.remove_node(n)
        yield (n,v)
        
        
        
     
def eulerian(G):    
    circuit = nx.Graph()  
    #create a copy of G so that original G doesn't get affected
    copy = G.__class__(G)
    #choose random node
    node = copy.nodes()[random.randrange(0,len(copy.nodes()))]
    circuit.add_node(node)
    i=0
    while copy and i<6:
        
        rand_num = random.randrange(0,len(copy.neighbors(node)))
        neighbour_edge = copy.neighbors(node)[rand_num]
        #move to one of it's neighbours
        second_copy = copy.__class__(copy)
        #print 'Initial graph is ' + str(copy.edges())
        #print 'Node is ' + str(node)
        #print 'Its neighbors are ' + str(copy.neighbors(node))
        #print 'Edge is ' + str(neighbour_edge)
        second_copy.remove_edge(node,neighbour_edge)
        for second_node in second_copy.nodes():
            if second_copy.degree(second_node) ==0:
                second_copy.remove_node(second_node)
        #print second_copy.nodes()
        #print second_copy.edges()
        #print nx.is_connected(second_copy)
        if nx.is_connected(second_copy):
            #print 'if loop. Node is ' + str(node) + ' its selected neighbor is '+ str(neighbour_edge)
            circuit.add_edge(node,neighbour_edge)
            #print 'abhi tak no error'
            copy.remove_edge(node,neighbour_edge)
            node = neighbour_edge
            i+=1
            #print 'if loop is running'
        else:   #if the graph becomes disconnected
            #print 'Nothing to be done. Loop will run again'
            i+=1
        print circuit.edges()    
    return circuit        
        
    #remove the corresponding edge from graph
    #check if the remaining graph is connected. If not, move to another neighbour
    #repeat previous 3 steps until the copy of graph becomes empty     
    
eulerian(G)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    