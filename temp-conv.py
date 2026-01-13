#!/usr/bin/env python3
import sys


wert = float(sys.argv[1])
einheit = sys.argv[2]

if einheit == "F" or einheit == "f":
    celsius = (wert - 32) * 5 / 9
    print(f"{wert}°F = {celsius:.1f}°C")

elif einheit == "C" or einheit == "c":
    fahrenheit = wert * 9 / 5 + 32
    print(f"{wert}°C = {fahrenheit:.1f}°F")

else:
    print("Unbekannt")

