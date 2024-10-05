#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    x1 = int(input("Rolls price? "))
    x2 = int(input("Cans of paint price? "))

    Sum = 8*x1 + 2*x2
    if 0 <= Sum < 200:
        print(Sum)
    elif 200 <= Sum < 500:
        print(0.97 * Sum)
    elif 500 <= Sum < 800:
        print(0.95 * Sum)
    elif 800 <= Sum < 1000:
        print(0.93 * Sum)
    elif Sum >= 1000:
        print(0.91 * Sum)
    else:
        print("Illegal value of price!", file=sys.stderr)
        exit(1)

