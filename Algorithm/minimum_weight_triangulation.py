#!/usr/bin/python -tt

"""
Design a dynamic programming algorithm to calculate the
minimum-weight triangulation of a convex polygon.
The weight of a triangulation is the sum of the lengths
of the diagonals.
"""

import sys
import random


def create_convex_polygon(num_vertices):
    n = num_vertices
    sum_angles = (n - 2) * 180
    angles = []
    while n > 1:
        angle = random.random() * 180
        if angle == 0 or (sum_angles - angle) <= 0 or (sum_angles - angle) >= (n - 1) * 180:
            continue
        else:
            angles.append(angle)
            sum_angles -= angle
            n -= 1
    angles.append(sum_angles)
    print(angles)


#def minimum_weight_triangulation():



def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print 'usage: ./*.py num_vertices'
        sys.exit(1)

    create_convex_polygon(int(args[0]))


if __name__ == '__main__':
    main()

