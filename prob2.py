from datetime import datetime
from datetime import timedelta

#Add 1 day
print(datetime.now() + timedelta(days=-1))

#print(datetime.now() + timedelta(years=+2, seconds=-60))
print(datetime.now() + timedelta(weeks=(52 * 2), seconds=-60))