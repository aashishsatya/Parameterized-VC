# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:53:50 2017

@author: aashish_b130160cs

Script that generates a test case and the solution
The vertex cover (answer) is saved in 'ans.txt'
Program generates test cases with vertex cover of size greater than
n/LOWER_LIMIT and n/UPPER_LIMIT
k is the size of the vertex cover rounded off to the next multiple
of ten.

"""

import random
from GraphUtil import *
from BruteForceVC import *
from ParameterizedVC import *

UPPER_LIMIT = 4
LOWER_LIMIT = 8

def generate_test_case(n, k):

    vertices = set([])
    edges = {}
    
    # add all vertices to the vertex set
    for i in xrange(0, n):
        vertices.add('v_' + str(i))
        
    # select the vertex cover
        
    vc_size = k
        
    # uncomment the below lines if you want the vc to be
    # selected randomly
    
#    vc_size = int(n/UPPER_LIMIT)
#    while vc_size >= int(n/UPPER_LIMIT) or vc_size < int(n/LOWER_LIMIT):
#        vc_size = int(n * random.random())
#    k = (int(vc_size/10) + 1) * 10    
    
    vertex_list = list(vertices)
    vc = [vertex_list[i] for i in random.sample(xrange(len(vertex_list)), vc_size)]
    vc = set(vc)
    
    # generate edges for each vertex in the vertex cover
    
    print '\nVertex cover =', vc
    
    for start in vc:
        if not (start in edges):
            edges[start] = []
        no_of_edges = int(n * random.random())
        for i in xrange(0, no_of_edges):
            new_stop = int(n * random.random())
            new_stop_str = 'v_' + str(new_stop)
            if new_stop_str == start:
                continue
            if new_stop_str not in edges[start]:
                edges[start].append(new_stop_str)
                
    G = UndirectedGraph(vertices, edges)
    
    # save the vertex cover
    
    with open('ans.txt', 'a') as f:
        f.write('n = ' + str(n) + '\n')
        f.write('VC size = ' + str(len(vc)) + '\n')
        f.write(str(vc) + '\n\n')
        f.close()         
    
    return G
    
def run_all():
    
    """
    Generates test cases ranging from 25 to 625 for the value of n
    and n/10, 2n/10, 3n/10, 4n/10 and 5n/10 for the value of k
    """
    
    for n in xrange(10, 15, 1):
        print 'Running tests for graph of size', str(n) + '...' 
        for k in xrange(n/10, n/2, 1):
            G = generate_test_case(n, k)
            print 'Generated graph:'
            print G
            print 'Running tests for vertex cover of size', str(k) + '...'
            print 'Running brute force...'
            # run brute force here
            brute_vc = brute_force_VC(G)
            print brute_vc
            print 'Running parameterized...'
            # run parameterized here
            param_vc = parameterized_vc(G, k)
            print param_vc
    