#!/usr/bin/python3
def divisible_by_2(my_list=[]):
fanlist = my_list[:]
for count, i in enumerate(my_list):
    if i % 2 == 0:
        fanlist[count] = True
    else:
        fanlist[count] = False
        return(fanlist)
