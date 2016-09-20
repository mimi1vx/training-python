#!/usr/bin/python

import datetime

current_year = datetime.date.today().year

for year in range(current_year, current_year + 10):
    print(datetime.date(year, 9, 1).strftime("%Y: %A"))
