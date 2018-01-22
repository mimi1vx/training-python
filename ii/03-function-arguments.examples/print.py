import sys

def myprint(*args, sep=" ", end="\n", file=sys.stdout):
    for i, value in enumerate(args):
        if i:
            file.write(sep);
        file.write(str(value));
    file.write(end)

if __name__ == '__main__':
    myprint(1, 2, 3.5, 4.1, sep="-", end="\n****\n")
    myprint(1, 2, 3.5, 4.1, sep="-", end="\n****\n")
    myprint(1, 2, 3.5, 4.1, sep="-", end="\n****\n")
