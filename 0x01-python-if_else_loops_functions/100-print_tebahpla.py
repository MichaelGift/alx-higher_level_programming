#!/usr/bin/python3
temp_str = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        temp_str += chr(i)
    else:
        temp_str += chr(i-32)
print("{}".format(strtmp), end="")
