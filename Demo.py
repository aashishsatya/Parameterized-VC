# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:04:18 2017

@author: aashishsatya
"""

import sys
from BruteForceVC import *

E = {}
V = set([])

for line in sys.stdin:
    # get the parameter
    k = int(line)
    break

for line in sys.stdin:
    line = line[:-1]    # remove '\n'
    edge_list = line.split(' ')
    if len(edge_list) == 2:
        # it's a proper edge, not an isolated vertex
        start = edge_list[0]
        end = edge_list[1]
        if start in E:
            # append end to the adjacency list of start
            E[start].append(end)
        else:
            E[start] = [end]
        # ditto for end
        if end in E:
            E[end].append(start)
        else:
            E[end] = [start]
        # add start and end to vertices of the graph
        # since V is a set, duplicates will be taken care of automatically
        V.add(start)
        V.add(end)
    elif len(edge_list) == 1:
        # degree zero vertices
        # their edge set will be []
        vertex = edge_list[0]
        E[vertex] = []
        V.add(vertex)
        
G = UndirectedGraph(V, E)

# We will be using members of class UndirectedGraph directly
# i.e. as G.E and G.V instead of using G.get_edges() and G.get_vertices()
# this kind of abstraction breaking is usually frowned upon,
# but this project might not need that level of organization I feel
        
# compute vertex cover by brute force
print brute_force_VC(G)
        
        
    