"""
@Author - Adam Pinkos
@File - graph.py
@Date - 12/01/2025
@Brief - Build k-nearest-neighbor graph
"""

import math


def build_k_nearest_graph(points, k):

    n = len(points)
    adj = []

    # initialize empty neighbor lists
    for _ in range(n):
        adj.append([])

    # for each point 
    # compute distances to all other points
    for u in range(n):
        dlist = []

        (x1, y1) = points[u]

        # compare u to every other point v
        for v in range(n):
            if u == v:
                continue
