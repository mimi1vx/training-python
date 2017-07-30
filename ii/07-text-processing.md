# Text processing

## Reading a text file at once

    with open("file.txt") as stream:
        text = stream.read()

## Reading a text file by line

    with open("file.txt") as stream:
        for line in stream
            print(repr(line))

## Reading from stdin by line

    import sys

    for line in sys.stdin:
        print(repr(line))

## Regular expression matching and parsing

    import sys, re

    re_cz_date = re.compile(r"([0-9]{1,2})\.([0-9]{1,2}).([0-9]{4})")

    for line in sys.stdin:
        print(tuple(int(field) for field in re_cz_date.match(line.strip()).groups()))


TODO: Notes on format, jinja2, mako, notes on re, parser libraries, etc...

## Text formats

Example: markdown

Example: mako, jinja2

