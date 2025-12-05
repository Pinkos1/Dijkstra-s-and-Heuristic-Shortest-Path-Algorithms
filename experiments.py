"""
@Author - Adam Pinkos
@File - experiments.py
@Date - 12/01/2025
@Brief - Run experiments and generate runtime plots 
"""

from points import generate_random_points, find_source_and_target
from graphs import build_k_nearest_graph
from algorithms import dijkstra, astar



import time
import matplotlib.pyplot as plt

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


             # dijkstra time 
            start = time.time()
            d_val = dijkstra(adj, s, t)
            end = time.time()
            dij_time = end - start

            print("Dijkstra time:", dij_time)
            dijkstra_times.append(dij_time)

            #astar time
            start = time.time()
            a_val = astar(adj, points, s, t)
            end = time.time()
            a_time = end - start

            print("A* time:", a_time)
            astar_times.append(a_time)

            ns_list.append(n)

        # save for plotting
        results[k] = (ns_list, dijkstra_times, astar_times)

    return results

    
def make_plots(results):

    # Loop over each k in the results dictionary
    for k in results:
        (ns_list, d_times, a_times) = results[k]

        # Modern style: light grid background
        plt.style.use("ggplot")

        # Create a new figure with a good size
        plt.figure(figsize = (8, 5))

        # Plot Dijkstra times
        plt.plot(
            ns_list,
            d_times,
            label = "Dijkstra",
            marker = 'o',
            markersize = 6,
            linewidth = 2,
            color = "#1f77b4"  
        )

        # Plot A* times
        plt.plot(
            ns_list,
            a_times,
            label = "A*",
            marker = 's',
            markersize = 6,
            linewidth = 2,
            color = "#ff7f0e"   
        )

        # Labels, title, and grid
        plt.xlabel("n (number of points)", fontsize = 12)
        plt.ylabel("Runtime (seconds)", fontsize = 12)
        plt.title("Runtime Comparison for k = " + str(k), fontsize = 14)

        # Slightly lighten the background
        ax = plt.gca()
        ax.set_facecolor("2a2a2a")  

        # Show legend with light border
        plt.legend(frameon = True, facecolor = "white", edgecolor = "black")

        # Save the plot
        filename = "plot_k_" + str(k) + ".png"
        plt.savefig(filename, dpi = 150, bbox_inches = "tight")
        print("Saved plot:", filename)

        # Show the plot on screen
        plt.show()

        # Close the figure
        plt.close()


def main():

    # run all experiments
    results = run_experiments()

    print("\nMaking plots...\n")

    # generate and save the four plots
    make_plots(results)

    print("All plots generated.")


if __name__ == "__main__":
    main()