#!/usr/bin/python

import sys
import argparse

class Application:
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", action="store_true",
                help="Enable debugging")
        parser.add_argument("-V", "--version", action="store_true",
                help="Print version and exit")
        parser.add_argument("-n", "--name",
                help="Specify your name")
        args = parser.parse_args()
        if args.debug:
            print(args)
        if args.version:
            print("Test program version 0.0.1")
            sys.exit(0)
        print("Hello {}".format(args.name or "Somebody"))

if __name__ == '__main__':
    application = Application()
    application.run()
