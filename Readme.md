
## Dijkstra vs A* on k-Nearest Neighbor Graphs

Author: Adam Pinkos  
Course: CS 4040 — Algorithms  
Date: December 2025

## About the program
This program compares the performance of Dijkstra’s algorithm and A* for computing shortest paths on random geometric graphs.  
- Generate `n` random points in the square \([0, 100]^2\)
- Build a k–nearest neighbor graph using Euclidean distances between points
- Choose the source `s` and target `t` based on lexicographic order
- Run Dijkstra’s algorithm from `s` to `t`
- Run A* from `s` to `t` using the Euclidean distance to `t` as the heuristic \(h(u)\)
- Measure the runtime of both algorithms for increasing values of `n`
- Generate four runtime plots (one for each k value)
- Analyze and compare the results

## How to run
Requires Python 3 and matplotlib:
pip install matplotlib