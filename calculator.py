from math import *
from divisions import division
from operator import multiplication
from operator import addition
from operator import subtraction

print("これは電卓です")
num1 = input("number: ")
num2 = input("number: ")

oprompt = ["division\n a.yes\n b.no\n",
           "multiplication\n a.yes\n b.no\n",
          "addition\n a.yes\n b.no\n",
          "subtraction\n a.yes\n b.no\n",]
          

division1  = [
    division(oprompt[0] , "a"),
]
multiplication1  = [
    multiplication(oprompt[1] , "a"),
]
addition1  = [
    addition(oprompt[2] , "a"),
]
subtraction1 = [
    subtraction(oprompt[3] , "a"),
]


def calc(division1):
    for division in division1:
        selection = input(division.prompt)
        if selection == division.selection:
             print(float(num1) / float(num2))
        if selection != division.selection:
             calc2(multiplication1)

def calc2(multiplication1):
    for multiplication in multiplication1:
        selection = input(multiplication.prompt)
        if selection == multiplication.selection:
             print(float(num1) * float(num2))
        if selection!= multiplication.selection:
            calc3(addition1)


def calc3(addition1):
    for addition in addition1:
        selection = input(addition.prompt)
        if selection == addition.selection:
           print(float(num1) + float(num2))
        if selection != addition.selection:
             calc4(subtraction1)
        


def calc4(subtraction1):
    for subtraction in subtraction1:
        selection = input(subtraction.prompt)
        if selection == subtraction.selection:
           print(float(num1) - float(num2))

    

calc(division1)

        
