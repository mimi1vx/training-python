import os, sys

def myprint(*args, sep=" ", end="\n", fd=1):
    for i, value in enumerate(args):
        if i:
            os.write(fd, sep.encode("utf-8"));
        os.write(fd, str(value).encode("utf-8"));
    os.write(fd, end.encode("utf-8"))

def myprint2(*args, sep=" ", end="\n", fd=1):
    os.write(fd, (sep.join([str(arg) for arg in args]) + end).encode("utf-8"))

def myprint3(*args, **kwargs):
    sep = kwargs.pop('sep', " ")
    end = kwargs.pop('end', "\n")
    fd = kwargs.pop('fd', 1)
    if kwargs:
        raise Exception("Unknown keyword args: {}".format(kwargs.keys()))
    os.write(fd, (sep.join([str(arg) for arg in args]) + end).encode("utf-8"))

if __name__ == '__main__':
    myprint(1, 2, 3.5, 4.1, sep="-", end="\n****\n")
    myprint2(1, 2, 3.5, 4.1, sep="-", end="\n****\n")
    myprint3(1, 2, 3.5, 4.1, sep="-", end="\n****\n")
    myprint3(1, 2, 3.5, 4.1, sep="-", end="\n****\n", nonsense=6)
