#!/usr/bin/python3
def no_c(my_string):
    mic_str = ""
for i in my_string:
    if i is not 'c' and i is not'C':
        mic_str += i
        return (mic_str)
# return my_string.translate({ord(c): None c in "cC"})
