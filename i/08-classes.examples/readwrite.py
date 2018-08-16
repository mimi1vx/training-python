#!/usr/bin/python3

import sys

class Hello:
    def __init__(self):
        self.data = {}

    def clear(self):
        self.data.clear()

    def hello(self, lang):
        return self.data[lang]

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
    def __init__(self, filename):
        self.filename = filename

    def usage(self, name):
        print("Usage: \n  {0} read|write\n  {0} hello LANG".format(name))

    def cmd_write(self):
        hello = Hello()
        hello.set_defaults()
        hello.write_file(self.filename)

    def cmd_read(self):
        hello = Hello()
        hello.read_file(self.filename)
        print(hello.data)

    def cmd_hello(self, lang):
        hello = Hello()
        hello.read_file(self.filename)
        print(hello.hello(lang))

    def run(self, argv=sys.argv):
        try:
            command = argv[1]
        except IndexError:
            self.usage(argv[0])
            return

        if command == "write":
            self.cmd_write()
        elif command == "read":
            self.cmd_read()
        elif command == "hello":
            self.cmd_hello(argv[2])
        else:
            self.usage(argv[0])

if __name__ == '__main__':
    application = Application("file.txt")
    application.run()
