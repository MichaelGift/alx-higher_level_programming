#!/usr/bin/python3
char_end = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=char_end)
    else:
        if i == 99:
            char_end = "\n"
            print(i, end=char_end)
