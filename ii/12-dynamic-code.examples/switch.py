#!/usr/bin/python

import sys

class Switch(object):
    def command_add(self, name):
        print("Add: {}".format(name))

    def command_remove(self, name):
        print("Remove: {}".format(name))

    def run(self):
        program, command, name = sys.argv
        method = getattr(self, "command_{}".format(command))
        method(name)

if __name__ == "__main__":
    switch = Switch()
    switch.run()
