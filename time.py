#!/usr/bin/env python3
import sys

sekunden = int(sys.argv[1])

stunden = sekunden // 3600
sekunden = sekunden % 3600

minuten = sekunden // 60
sekunden = sekunden % 60

print(str(stunden) + "h" + str(minuten) + "m" + str(sekunden) + "s")
