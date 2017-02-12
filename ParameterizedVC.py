# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:48:30 2017

@author: aashishsatya

Implementation of the parameterized algorithm for vertex cover

"""

import itertools
from GraphUtil import *

#def rr_1(G, k):
#    
#    """
#    Applies Reduction Rule 1 to G and returns (G', k')
#    
#    RR1: If G contains an isolated vertex v, delete v from G.
#    The new instance is (G − v, k)
#    """
#    
#    pass
#
#def rr_2(G, k):
#    
#    """
#    Applies Reduction Rule 2 to G and returns (G', k')
#    
#    RR2: If there is a vertex v of degree at least k + 1, 
#    then delete v (and its incident edges) from G and 
#    decrement the parameter k by 1. 
#    The new instance is (G − v, k − 1)
#    """
#    
#    pass

#Reduction Rule 3 will be hard-coded into the code for vertex cover

#RR3: Let (G, k) be an input instance such that RR1 and RR2 are not 
#applicable to (G, k). If k < 0 and G has more than k^2 + k vertices,
#or more than k^2 edges, then conclude that we are dealing 
#with a no-instance

def param_vc_wrapper(G, S, k, next_vertex_count, sorted_vertices):
    
    """
    S is the subset selected so far
    Other parameters are as below
    """
    
    if k < 0:
        # this VC has exceeded the budget
        return None
        
    if check_vertex_cover(G, S):
        return S
        
    if k == 0:
        return None    
        
    # now we choose between the vertex that comes next in degree
    # or its neighbours
        
    #print type(sorted_vertices)
    new_vc = S.copy()
    new_vc.add(sorted_vertices[next_vertex_count])
    branch1 = param_vc_wrapper(G, new_vc, k - 1, next_vertex_count + 1, sorted_vertices)
    branch2 = param_vc_wrapper(G, S.union(G.E[sorted_vertices[next_vertex_count]]), k - len(G.E[sorted_vertices[next_vertex_count]]), next_vertex_count + 1, sorted_vertices)
    if branch1 != None:
        return branch1
    elif branch2 != None:
        return branch2
    else:
        return None
    
    

def parameterized_vc(G, k):

    """
    Runs the branching algorithm on the input instance
    G is an object of type UndirectedGraph
    k is an integer (parameter)
    """
    
    print 'k =', k
    sorted_vertices = sorted(G.E, key = lambda k: len(G.E[k]), reverse = True)
    return param_vc_wrapper(G, set([]), k, 0, sorted_vertices)
        