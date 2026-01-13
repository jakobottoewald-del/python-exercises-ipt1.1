#!/usr/bin/env python3
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"x1={x1}, x2={x2}")

elif D == 0:
	x1 = -b / (2*a)
	print(f"x={x1}")

elif D < 0:
	print("keine lösung")

else:
	print("unbekannt")

