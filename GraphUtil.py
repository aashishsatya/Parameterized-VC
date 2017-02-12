# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:25:31 2017

@author: aashishsatya

A script having a set of simple functions to check graph properties.

"""

#class UndirectedGraph:
#    
#    def __init__(self, V, E):
#        
#        """
#        Initialize the Graph class. Accepts a set of vertices V and edges E as input.
#        V is implemented as a set
#        E is implemented as an adjacency list in the form of a dictionary.
#        """
#        
#        self.V = V
#        self.E = E

def check_vertex_cover(E, S):
    
    """
    Returns True if set S is a vertex cover of the edge set E,
    False otherwise.
    S is implemented as a set
    E is implemented as an adjacency list mapping a vertex to a list
    of edges
    """
    
    for start in E.keys():
        if start in S:
            # vertex start is already in the cover
            # so we needn't check its corresponding edges
            continue
        for end in E[start]:
            if not (end in S):
                return False
    return True
