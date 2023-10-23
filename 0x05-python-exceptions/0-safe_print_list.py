#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lm8s = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            lm8s += 1
        except IndexError:
            break
    print()
    return lm8s
