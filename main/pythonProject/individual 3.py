#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    S = float(input("Payment amount? "))
    if S < 0:
        print("Illegal value of payment amount", file=sys.stderr)
        exit(1)

    banknotes = 0
    while S >= 500:
        S -= 500
        banknotes += 1
    while S >= 100:
        S -= 100
        banknotes += 1
    while S >= 10:
        S -= 10
        banknotes += 1
    while S >= 5:
        S -= 5
        banknotes += 1
    while S >= 1:
        S -= 1
        banknotes += 1
    print(f"Total banknotes = {banknotes}")