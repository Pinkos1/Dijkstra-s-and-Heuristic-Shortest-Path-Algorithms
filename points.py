##
# @file points.py
# @author Adam Pinkos
# @date 12/01/2025
# @brief Functions for generating random points and selecting source/target.
#
# This module contains helper routines that generate points in [0,100]^2 and
# determine the lexicographically smallest and largest points (s and t).
#


import random

# random values 
DEFAULT_N = 100
DEFAULT_SEED = 0



##
# @brief Generate n random 2D points in the square [0,100]^2.
# @param n Number of points to generate.
# @param seed Optional seed for reproducibility.
# @return A list of (x, y) coordinates
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



##
# @brief Find source and target points using lexicographic order.
# @param points List of x, y tuples.
# @return s_index, t_index for the smallest and largest points.
def find_source_and_target(points):

    n = len(points)

    # initialize s and t
    s_index = 0
    t_index = 0


    # go through all points
    for i in range(1, n):
        (x, y) = points[i]
        (sx, sy) = points[s_index]
        (tx, ty) = points[t_index]


        # check if current point is lexicographically smaller than s
        if (x < sx) or (x == sx and y < sy):
            s_index = i

        # check if current point is lexicographically larger than t
        if (x > tx) or (x == tx and y > ty):
            t_index = i


    return s_index, t_index
