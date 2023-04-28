# DATES #

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#una marca formato standard para mandar 1 valor q represente un momento especifico
timestamp = now.timestamp()

print(timestamp)