#!/usr/bin/env python3
import sys

zahl = int(sys.argv[1])
length = int(sys.argv[2])
i = 0
for arg in range(0, length):
	i += zahl
	print(i, end=" ")
print("")
