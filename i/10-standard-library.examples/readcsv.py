#!/usr/bin.python

import csv

with open('example.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
