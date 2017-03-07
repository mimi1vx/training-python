#!/usr/bin/python

from __future__ import print_function

import sys

class Hello:
    def __init__(self, lang=None):
        self.data = {}
        self.lang = lang

    def hello(self):
        return self.data[self.lang]
    
    def set_defaults(self):
        self.data["en"] = "Hello!"
        self.data["cs"] = "Dobrý den!"
        self.data["sk"] = "Dobrý deň!"
        self.data["pl"] = "Dzień dobry!"
        self.data["it"] = "Buon giorno!"
        self.data["ru"] = "Добрый день!"

    def write_file(self, filename):
        with open(filename, "w") as stream:
            print("#", file=stream)
            print("# Hello in a few languages", file=stream)
            print("#", file=stream)
            print("", file=stream)
            for key, value in sorted(self.data.items()):
                print("{}: {}".format(key, value), file=stream)

    def read_file(self, filename):
        with open(filename) as stream:
            for line in stream:
                # Comment or empty line
                if line.startswith("#") or line.startswith("\n"):
                    continue
                # Missing colon
                if ':' not in line:
                    raise ValueError("Invalid line: {!r}".format(line))
                # Data line
                lang, text = line.split(":", 1)
                self.data[lang.strip()] = text.strip()

class Application:
    def usage(self):
        sys.exit("Usage: \n  {0} read|write\n  {0} hello LANG".format(sys.argv[0]))

    def write(self):
        hello = Hello()
        hello.set_defaults()
        hello.write_file("file.txt")

    def read(self):
        hello = Hello()
        try:
            hello.read_file("file.txt")
        except FileNotFoundError as e:
            sys.exit(e)
        print(hello.data)

    def hello(self, lang):
        hello = Hello(lang)
        hello.read_file("file.txt")
        print(hello.hello())

    def run(self):
        try:
            command = sys.argv[1]
        except IndexError:
            self.usage()

        if command == "write":
            self.write()
        elif command == "read":
            self.read()
        elif command == "hello":
            self.hello(sys.argv[2])
        else:
            self.usage()

if __name__ == '__main__':
    application = Application()
    application.run()
