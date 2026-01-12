#!/usr/bin/env python3
import sys
import math

r = float(sys.argv[1])

A = math.pi * r * r
U = 2 * math.pi * r

print("A=", round(A, 2))
print("U=", round(U, 2))

