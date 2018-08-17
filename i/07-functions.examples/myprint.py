import sys

def myprint(*args, sep=" ", end="\n", file=sys.stdout):
    for idx, arg in enumerate(args):
        if idx != 0:
            file.write(sep)
        file.write(str(arg))
    file.write(end)
