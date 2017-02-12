# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:17:57 2017

@author: aashishsatya
"""

import itertools
from GraphUtil import *

def brute_force_VC(G):
    
    """    
    Return the vertex cover of edges E as a set, None otherwise.
    """
    
    for k in xrange(1, len(G.V) + 1):
        # iterate over k sized subsets
        k_subsets = set(itertools.combinations(G.V, k))
        # check if each of those subsets is a vertex cover
        for subset in k_subsets:
            # set(subset) is needed for O(1) checking of membership
            # otherwise subset is generated as a list and might take
            # upto O(n) time
            if check_vertex_cover(G, set(subset)):
                return set(subset)
    
    return None

    
    
    