#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nick
#
# Created:     18/01/2014
# Copyright:   (c) nick 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def insertion_sort(list):
    for index in range(len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
            list[i+1] = list[i]
            list[i] = value
            i = i -1

