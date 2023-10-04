#!/usr/bin/python3
def uppercase(str):
    temp_str = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            temp_str += chr(ord(c)-32)
        else:
            temp_str += c
            print("{}".format(temp_str))
