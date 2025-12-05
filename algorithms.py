"""
@Author - Adam Pinkos
@File - algorithms.py
@Date - 12/01/2025
@Brief - Implmentation of Dijkstra and A* shortest path algorithms
"""


import math
import heapq


def dijkstra(adj, s, t):

    n = len(adj)

    # distances d[v]
    d = []
    for _ in range(n):
        d.append(float('inf'))

    d[s] = 0.0

    # visited set
    visited = []
    for _ in range(n):
        visited.append(False)