#!/usr/bin/env python3
import sys

coord = sys.argv[1]
col = coord[0]
row = int(coord[1])

odd_cols = "aceg"

if col in odd_cols:
    if row % 2 == 1:
        print("schwarz")
    else:
        print("weiss")
else:
    if row % 2 == 1:
        print("weiss")
    else:
        print("schwarz")
