
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
1.) Install libaries
Requires Python 3 and matplotlib:  
```bash
pip install matplotlib 
``` 
2.) Run the Experiment Script  
From the project folder:  
```bash
python experiments.py
```
This will:

-Generate random point sets  
-Build k-NN graphs  
-Run Dijkstra and A*  
-Print timing results  
-Display plots on-screen  
-Save plots as PNG files in the project folder

## Experimental Values
You can adjust values based on the performance of your device. For now, the values are scaled for regular python performance.  
**k values:**  
```bash
5, 10, 20, 50
```
**n values:**  
```bash
100, 500, 1000, 2000, 5000
```
## Algorithm Descriptions
**Dijkstra:**    
-Uses a min-heap priority queue (heapq)  
-Stops early when the target t is extracted  
-Time complexity: 𝑂(𝑚log𝑛)

**Astar**  
-Same priority queue structure as Dijkstra  
-Uses heuristic ℎ(𝑢) = Euclidean distance to target 𝑡  
-Prioritizes nodes closer to 𝑡 reducing exploration  
-Expected to run faster, especially for larger k

##Summary of Findings  
-As n increases, both algorithms slow down, but Dijkstra grows faster.  
-As k increases, the graph becomes denser → more edges → higher runtimes.  
-A* consistently outperforms Dijkstra because the heuristic directs search toward the target.
