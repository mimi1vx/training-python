#!/usr/bin/python

import urllib.request

request = urllib.request.urlopen("http://pavlix.net")
print(request.read().decode("utf-8"))
