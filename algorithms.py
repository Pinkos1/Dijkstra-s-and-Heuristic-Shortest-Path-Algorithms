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


    # priority queue Q keyed on du
    # store elements as distance, node
    Q = []
    heapq.heappush(Q, (0.0, s))




    # while q != empty
    while len(Q) > 0:
        (dist_u, u) = heapq.heappop(Q)

        # if already visited, skip
        if visited[u]:
            continue

        visited[u] = True

        # Stop early if t is extracted
        if u == t:
            return d[t]

        # for each v in Adj[u]
        neighbors = adj[u]
        for (v, w_uv) in neighbors:

            # RELAXATION
            if d[v] > d[u] + w_uv:
                d[v] = d[u] + w_uv

                # decrease-key: push updated pair
                heapq.heappush(Q, (d[v], v))

    # unreachable
    return float('inf') 



def astar(adj, points, s, t):

    n = len(adj)

    # distances
    d = []
    for _ in range(n):
        d.append(float('inf'))
    d[s] = 0.0



    #visits
    visited = []
    for _ in range(n):
        visited.append(False)

    
    (tx, ty) = points[t]

    # priority queue stores (fu, u)
    Q = []

    #initial 
    (sx, sy) = points[s]
    h_s = math.sqrt((sx - tx) * (sx - tx) + (sy - ty) * (sy - ty))

    heapq.heappush(Q, (h_s, s))




     # while Q != empty
    while len(Q) > 0:

        (f_u, u) = heapq.heappop(Q)

        if visited[u]:
            continue

        visited[u] = True

        # if t is extracted, stop and return dt
        if u == t:
            return d[t]

        # relax all neighbors
        neighbors = adj[u]
        (ux, uy) = points[u]

        for (v, w_uv) in neighbors:

            # normal relaxation
            if d[v] > d[u] + w_uv:
                d[v] = d[u] + w_uv

                # compute heuristic hv
                (vx, vy) = points[v]
                h_v = math.sqrt((vx - tx) * (vx - tx) + (vy - ty) * (vy - ty))

                f_v = d[v] + h_v   # f = g + h

                # decrease key simulated by pushing new value
                heapq.heappush(Q, (f_v, v))

    # unreachable
    return float('inf')