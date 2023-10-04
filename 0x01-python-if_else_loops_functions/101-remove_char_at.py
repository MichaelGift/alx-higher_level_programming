#!/usr/bin/python3
def remove_char_at(str, n):
    temp_str = ""
    cont = 0
    for c in str:
        if cont == n:
            pass
        else:
            temp_str += c
        cont += 1
    return temp_str
