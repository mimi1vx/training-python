#!/usr/bin/python3

import sys
import csv

login = input("Login: ")
password = input("Password: ")

with open('example2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    users = list(reader)

for row in users:
    if login != row['Username']:
        continue
    if password != row['Password']:
        continue
    name = row['Name']
    break
else:
    sys.exit("Bad user name or password.")

print("Hello {}".format(name))
