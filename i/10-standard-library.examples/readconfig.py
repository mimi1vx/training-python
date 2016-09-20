#!/usr/bin/python

import configparser

config = configparser.ConfigParser()
config.read("example.conf")
print(config["main"]["text"])
