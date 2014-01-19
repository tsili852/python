#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tsilivisn
#
# Created:     16/01/2014
# Copyright:   (c) tsilivisn 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calculate_fibonacci(par_number):
    print "Interative find"
    sequence = [0,1]
    for i in range(par_number):
        sequence.append(sequence[i] + sequence[i+1])
    return sequence

def recursive_fibonacci(par_number, j):
    if par_number <= 1:
        print "Recurcive find"
        return sequence
    else:
        sequence.append(sequence[j-1] + sequence[j])
        return recursive_fibonacci(par_number - 1, j + 1)

f_number = calculate_fibonacci(10)
print f_number[10]

sequence = [0,1]
par_number = input("Give wich fibonacci number in the sequance you want")
f_number_rec = recursive_fibonacci(par_number, 1)
print f_number_rec[par_number]

