"""
@Author - Adam Pinkos
@File - points.py
@Date - 12/01/2025
@Brief - 
"""

import random
import math
import heapq
import time
import matplotlib.pyplot as plt


# random values 
DEFAULT_N = 100
DEFAULT_SEED = 0


def generate_random_points(n, seed = None):
    
    if seed is not None:
        random.seed(seed)

    points = []

    i = 0
    while i < n:

        # sample directly, no rounding
        x = random.uniform(0.0, 100.0)
        y = random.uniform(0.0, 100.0)
        points.append((x, y))
        i += 1

    return points




def main():
    
    # just use the defaults
    n = DEFAULT_N
    seed = DEFAULT_SEED

    pts = generate_random_points(n, seed)

    # print them out
    print("Number of points:", len(pts))
    for idx, (x, y) in enumerate(pts):
        print(idx, x, y)


if __name__ == "__main__":
    main()