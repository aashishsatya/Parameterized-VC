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

n = 400  # number of vertices
UPPER_LIMIT = 4
LOWER_LIMIT = 8
#k = 500   # parameter

vertices = set([])
edges = {}

# add all vertices to the vertex set
for i in xrange(0, n):
    vertices.add('v_' + str(i))
    
# select the vertex cover

vc_size = int(n/UPPER_LIMIT)
while vc_size >= int(n/UPPER_LIMIT) or vc_size < int(n/LOWER_LIMIT):
    vc_size = int(n * random.random())
vertex_list = list(vertices)
vc = [vertex_list[i] for i in random.sample(xrange(len(vertex_list)), vc_size)]
vc = set(vc)

# generate edges for each vertex in the vertex cover

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
            
# save the vertex cover

f = open('ans.txt', 'w')
f.write('VC size = ' + str(len(vc)) + '\n')
f.write(str(vc))
f.close()
 
k = (int(vc_size/10) + 1) * 10               
print k
for start in edges.keys():
    stops = edges[start]
    for stop in stops:
        print start + ' ' + stop