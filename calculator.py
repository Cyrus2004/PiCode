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


    i = 0
    marker = 0 #Index marker while temporarily jumping back and forth.
    prevNumber = -1 #Records position of previous number to prevent duplicates.

    number1 = 0
    number2 = 0

    while i < len(numbers):
        if numbers[i] == "/":
            marker = i
            
            #Number to left side of "*" or "/":
            while not numbers[i].isdigit():
                i = i - 1
                if not i == prevNumber:
                    number1 = numbers[i]

            i = marker
            
            #Number to right side of "*" or "/":
            while not numbers[i].isdigit():
                i = i + 1
            number2 = numbers[i]
            prevNumber = i

            print(number1)
            print(number2)
                

        i = i + 1