#!/usr/bin/env python3
import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

c = math.sqrt(a * a + b * b)

print("c=", round(c, 2))
