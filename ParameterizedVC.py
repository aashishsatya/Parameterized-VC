# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:48:30 2017

@author: aashishsatya

Implementation of the parameterized algorithm for vertex cover

"""

import itertools
from GraphUtil import *

sorted_vertices = []
global k

def param_vc_wrapper(G, S, next_vertex_count):
    
    """
    S is the subset selected so far
    Other parameters are as below
    """
    
#    print 'S =', S
#    print 'nvc =', next_vertex_count
#    print '----------------------------------'
    
    if len(S) > k:
        # this VC has exceeded the budget
        return None
        
    if check_vertex_cover(G, S):
        return S
        
    if len(S) == k:
        return None    
        
    # now we choose between the vertex that comes next in degree
    # or its neighbours
        
    #print type(sorted_vertices)
    new_vc = S.copy()
    new_vc.add(sorted_vertices[next_vertex_count])
    branch1 = param_vc_wrapper(G, new_vc, next_vertex_count + 1)
    branch2 = param_vc_wrapper(G, S.union(G.E[sorted_vertices[next_vertex_count]]), next_vertex_count + 1)
    if branch1 != None:
        return branch1
    elif branch2 != None:
        return branch2
    else:
        return None    
    

def parameterized_vc(G, k_val):

    """
    Runs the branching algorithm on the input instance
    G is an object of type UndirectedGraph
    k is an integer (parameter)
    """

    global sorted_vertices
    global k
    k = k_val    
    sorted_vertices = sorted(G.E, key = lambda k: len(G.E[k]), reverse = True)
    return param_vc_wrapper(G, set([]), 0)