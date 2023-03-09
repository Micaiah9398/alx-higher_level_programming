#!/usr/bin/python3
'''print alphabet in lowercase, not followed by a newline'''
for letter in range(97,123):
    print("{}".format(chr(letter))end="")
