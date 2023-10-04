#!/usr/bin/python3
char_end = ", "
for i in range(0, 100):
    second_digit = i % 10
    first_digit = i / 10
    if i < 10 and first_digit < second_digit:
        print("{}{}".format(0, i), end=char_end)
    elif first_digit < second_digit:
        if i == 89:
            char_end = "\n"
        print(i, end=char_end)
