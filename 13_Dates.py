### Dates ###

from datetime import datetime

now = datetime.now()

def print_date(date):

    print(date.day)
    print(date.month)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1 , 1)
print_date(year_2023)

from datetime import time

current_time = time(21, 6 , 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

diff = year_2023 - now
print(diff)