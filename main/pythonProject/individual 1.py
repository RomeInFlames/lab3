#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    x1 = int(input("Rolls price? "))
    x2 = int(input("Cans of paint price? "))

    summa = 8*x1 + 2*x2
    if 0 <= summa < 200:
        print(summa)
    elif 200 <= summa < 500:
        print(0.97 * summa)
    elif 500 <= summa < 800:
        print(0.95 * summa)
    elif 800 <= summa < 1000:
        print(0.93 * summa)
    elif summa >= 1000:
        print(0.91 * summa)
    else:
        print("Illegal value of price!", file=sys.stderr)
        exit(1)

