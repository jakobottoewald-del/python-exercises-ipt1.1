#!/usr/bin/env python3
import sys

zahl = int(sys.argv[1])
length = int(sys.argv[2])

i = 1
while i <= length:
    print(zahl * i, end=" ")
    i = i + 1
