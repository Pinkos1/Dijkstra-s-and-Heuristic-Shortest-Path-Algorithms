"""
@Author - Adam Pinkos
@File - points.py
@Date - 12/01/2025
@Brief - Generate random points and picks target
"""


import random

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
