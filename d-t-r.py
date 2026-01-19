#!/usr/bin/env python3
import sys

roman = sys.argv[1]

match roman:
	case '1':
		print("I")
	case '2':
		print("II")
	case '3':
		print("III")
	case '4':
		print("IV")
	case '5':
		print("V")
	case '6':
		print("VI")
	case '7':
		print("VII")
	case '8':
		print("VIII")
	case '9':
		print("IX")
	case '10':
		print("")
	case _:
		print(f"{sys.argv[1]}, ist unbekannt")
	
