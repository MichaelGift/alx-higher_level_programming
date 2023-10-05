#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    argc = len(sys.argv) - 1
    if argc == 1:
        print("1 argument", end="")
    elif argc != 1:
        print("{} arguments".format(argc), end="")
    if argc == 0:
        print(".")
    else:
        print(":")
    if(len(sys.argv) > 1):
        for a in sys.argv:
            if i > 0:
                print("{:d}: {}".format(i, a))
            i += 1
