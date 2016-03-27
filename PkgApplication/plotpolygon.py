#!/usr/bin/python -tt

import numpy
import planar
import matplotlib.pyplot as plt


def main():
    points = numpy.random.rand(10, 2)
    hull = planar.Polygon.convex_hull(points)
    x = [vertex[0] for vertex in hull]
    y = [vertex[1] for vertex in hull]
    plt.plot(points[:,0], points[:,1], 'ko')
    plt.plot(x, y, 'rs')
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'b--')
    plt.show()


if __name__ == '__main__':
    main()
