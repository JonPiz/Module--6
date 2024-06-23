import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        date = datetime.now()
        print("{0}\t{1}".format(date, payment))
