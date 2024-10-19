#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = float(input("Payment amount? "))
    if s < 0:
        print("Illegal value of payment amount", file=sys.stderr)
        exit(1)

    banknotes = 0
    while s >= 500:
        s -= 500
        banknotes += 1
    while s >= 100:
        s -= 100
        banknotes += 1
    while s >= 10:
        s -= 10
        banknotes += 1
    while s >= 5:
        s -= 5
        banknotes += 1
    while s >= 1:
        s -= 1
        banknotes += 1

    print(f"Total banknotes = {banknotes}")
