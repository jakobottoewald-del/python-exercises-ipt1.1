#!/usr/bin/env python3
import sys

letter = sys.argv[1]

match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'y':
        print(f"{sys.argv[1]}, ist ein Vokal")
    case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n':
        print(f"{sys.argv[1]}, ist ein Konsonant")
    case _:
        print("unbekannt")
