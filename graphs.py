##
# @file graph.py
# @author Adam Pinkos
# @date 12/01/2025
# @brief Builds a k-nearest-neighbor graph from a set of 2D points.
#
#


import math



##
# @brief Build a k-nearest-neighbor graph from 2D points.
# @param points List of (x, y) coordinates.
# @param k Number of nearest neighbors to connect.
# @return Adjacency list where adj[u] contains (v, distance) pairs.
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


            (x2, y2) = points[v]
            dx = x1 - x2
            dy = y1 - y2
            dist = math.sqrt(dx * dx + dy * dy)

            dlist.append((dist, v))

        # sort by smallest distance first
        dlist.sort(key=lambda item: item[0])

        # take the first k neighbors
        neighbors = dlist[:k]

        # add edges
        # undirected 
        for (dist, v) in neighbors:
            adj[u].append((v, dist))
            adj[v].append((u, dist))  # undirected graph

    return adj

