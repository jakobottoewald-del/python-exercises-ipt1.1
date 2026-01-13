#!/usr/bin/env python3
import sys

amount = float(sys.argv[1])
cur = sys.argv[2]
CHF = 0

if cur == "USD":
	CHF = amount / 100 * 80
	print(f"CHF, {CHF:.2f}")
elif cur == "EUR":
	CHF = amount / 100 * 93
	print(f"CHF, {CHF:.2f}")
elif cur == "GBP":
	CHF = amount / 100 * 107
	print(f"CHF, {CHF:.2f}")
else:
	print("unbekannt")

