import re


numbers = [] #List of numbers, separated by operators.

#Divisions and multiplications are done before pluss and minus. Variables stores these two numbers to be calculateed first.
set1 = 0
set2 = 0
setResult = 0

operator = ""

number = ""


while True:
    equation = input()

    x = 1
    listPos = 0

    for i in equation:
        if i.isdigit():
            number = number + i

        if not i.isdigit() or x == len(equation):
            if not number == "":
                numbers.append(number)
            number = ""

        if i == "+" or i == "-" or i == "*" or i == "/":
            numbers.append(i)

        x = x + 1

    print(numbers)

    
    #Calculates "/" and "*" before "+" and "-".

    #Stores divisions and multiplications. Each item in the lists are plused or minused with each other.
    plusThese = []
    divideMinusThese = []
    multiplyPlusThese = []
    multiplyMinusThese = []
    
    numberTemp = ""

    secondHalf = False #Checks the second half of an operation
    operator = "" #What operator are we using?

    for i in numbers:

        if i == "+" or i == "-":
            secondHalf == True
            
        while secondHalf == True:
            numberTemp = numberTemp + i

    
    #print(result)