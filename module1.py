#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tsilivisn
#
# Created:     15/01/2014
# Copyright:   (c) tsilivisn 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("--------> This is main <---------")
    a = -4
    b = 6
    c = (a + b) * 2
    d = [1,2,3,4,5]
    e = d[1:3]

    if (a > 0):
        print("a>0")
        print(c-a)
        d[1] = "second element"
    else:
        print("a<0")
        d[2] = "third element"
        print(c)

    print(d)
    e.append("new element")
    print(e)
    print ("End of programm")

def forAndRange():
    print("--------> This is forAndRange <---------")

    print(range(6))
    print(range(3,31,2))

    sum = 0
    for i in range(5):
        sum = sum + i
    print sum

def whileLoop():
    print("--------> This is whileLoop <---------")
    sum = 0
    i = 0

    while i<5:
        sum = sum + i
        i = i + 1

    print(sum)

def funWithStrings():
    print("--------> This is funWithStrings <---------")
    a = "My first string"
    b = 'My second string'
    c = "Nick's string"
    expression_string = "a+' '+b+' end'"
    print(len(c))

    a_with_b = a + " " + b
    print(a_with_b)

    print(b.split(' '))

    print(c.find("'"))

    d = c.replace('i', 'o')
    print(d)

    # eval() Evaluates the expression inside the string
    e = "1*10+2+4"
    print(eval(e))
    print(eval(e + '4'))
    print(eval(e + '+4'))
    print(eval(expression_string))

def factorial(number):
    print("--------> This is factorial <---------")

    if number <= 1:  #base case
        return 1
    else:
        return number*factorial(number-1)

if __name__ == '__main__':
    main()
    forAndRange()
    whileLoop()
    funWithStrings()

    number = input("Enter a non negative integer to take the factorial: ")
    factorial_of_number = factorial(number)
    print(factorial_of_number)