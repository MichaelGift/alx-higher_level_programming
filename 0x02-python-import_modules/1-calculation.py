#!/usr/bin/python3
if __name__ == "__main__":
from calculator_1 import add, sub, mul, div
    i = 10
    j = 5
    print("{:d} + {:d} = {:d}".format(i, j, add(i, j)))
    print("{:d} - {:d} = {:d}".format(i, j, sub(i, j)))
    print("{:d} * {:d} = {:d}".format(i, j, mul(i, j)))
    print("{:d} / {:d} = {:d}".format(i, j, div(i, j)))
