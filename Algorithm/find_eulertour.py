#!/usr/bin/python -tt
"""
Design an algorithm to find an Euler tour of a directed graph G with
n vertices and m edges in O(n+m) running time.
An Euler tour is a cycle that traverses each edges of G exactly once
according to its direction. Such a tour always exists if G is 
connected and the in-degree equals the out-degree of each vertex in 
G.
"""

import os, sys
import random
import networkx
import matplotlib.pyplot as plt


def find_eulertour(G, v, T, S):
    if G.out_degree(v) != 0:
        T.append(v)
        e = G.out_edges(v)[0]
        w = e[1]
        G.remove_edge(v, w)
        find_eulertour(G, w, T, S)
    else:
        S.append(v)
        if len(T) > 0:
            w = T.pop(-1)
            find_eulertour(G, w, T, S)
        else:
            return 


def main():
    G = networkx.DiGraph()
    G.add_nodes_from(range(1,10))
    G.add_path([1, 6, 9, 1, 2, 3, 4, 2, 8, 7, 5, 8, 1])
    networkx.draw(G)
    v = random.randint(0, len(G.nodes())-1)
    T = []
    S = []
    find_eulertour(G, v, T, S)
    S.reverse()
    print v, S
    plt.show()


if __name__ == '__main__':
    main()
