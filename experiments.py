"""
@Author - Adam Pinkos
@File - experiments.py
@Date - 12/01/2025
@Brief - Run experiments and generate runtime plots 
"""

from points import generate_random_points, find_source_and_target
from graphs import build_k_nearest_graph
from algorithms import dijkstra, astar


def run_experiments():

    test_ns = [100, 500, 1000, 2000, 5000] ## Will change over time ##

    # k values
    test_ks = [5, 10, 20, 50]

    # store results for plotting later
    results = {}


    for k in test_ks:
        print("Running experiments for k =", k)

        ns_list = []
        dijkstra_times = []
        astar_times = []



        # different n graphs
        for n in test_ns:
            print("\n--- n =", n, " ---")

            # generate random points
            points = generate_random_points(n, seed=0)

            # build k-NN graph
            adj = build_k_nearest_graph(points, k)

            # find s and t
            s, t = find_source_and_target(points)
