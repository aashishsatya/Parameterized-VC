# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:17:57 2017

@author: aashishsatya
"""

import itertools
import time
from GraphUtil import *

TIME_MAX = 60

def brute_force_VC(G):
    
    """    
    Return the vertex cover of edges E as a set, None otherwise.
    """
    
    start_time = time.time()
    current_time = start_time
    for k in xrange(1, len(G.V) + 1):
        print 'Checking subsets of size', str(k) + '...'
        # iterate over k sized subsets
        #k_subsets = set()
        # check if each of those subsets is a vertex cover
        for subset in itertools.combinations(G.V, k):
            current_time = time.time()
            # set(subset) is needed for O(1) checking of membership
            # otherwise subset is generated as a list and might take
            # upto O(n) time
            if check_vertex_cover(G, set(subset)):
                return (set(subset), current_time - start_time)
            if current_time - start_time > TIME_MAX:
                # timeout
                return (None, TIME_MAX)
    
    return (None, current_time - start_time)

    
    
    