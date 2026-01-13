#!/usr/bin/env python3
import sys

brutto = float(sys.argv[1])

ahv = brutto * 0.087
iv = brutto * 0.014
eo = brutto * 0.005
alv = brutto * 0.011
nbu = brutto * 0.0073
pk = brutto * 0.0089

netto = brutto - ahv - iv - eo - alv - nbu - pk

print("Bruttolohn", brutto)
print("AHV", ahv)
print("IV", iv)
print("EO", eo)
print("ALV", alv)
print("NBU", nbu)
print("PK", pk)
print("Nettolohn", netto)
