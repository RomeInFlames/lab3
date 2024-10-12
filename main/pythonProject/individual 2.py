#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    x1, y1 = map(int, input("Coordinates of first circle? ").split(maxsplit=2))
    x2, y2 = map(int, input("Coordinates of second circle? ").split(maxsplit=2))
    r1 = int(input("Radius of first circle? "))
    r2 = int(input("Radius of second circle? "))

    Coordinate1 = (x1, y1)
    Coordinate2 = (x2, y2)
    d = math.dist(Coordinate1, Coordinate2)

    if d < r1 + r2:
        point = 2
    elif d == r1 + r2:
        point = 1
    else:
        point = 0

    print(f"Number of common points = {point}")

