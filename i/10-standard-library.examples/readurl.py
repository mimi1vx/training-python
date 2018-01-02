#!/usr/bin/python

import urllib.request

request = urllib.request.urlopen("http://github.com/")
print(request.read().decode("utf-8"))
