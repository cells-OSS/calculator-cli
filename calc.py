import os
import sys
import math

welcomeMessage = """
===============WELCOME===============

1 = +
2 = -
3 = *
4 = /
5 = Find a given number's multipliers
6 = Finding the given exponent of the given number
7 = Round a Number
8 = Find a percentage of a number
9 = Finding the possible base and the exponent(s) of the given number
10 = Finding the smallest possible n-th root of the given number
11 = Find a given number's multipliers

TIP: if you want to come back to this menu at any time, just type 'back'

"""
print(welcomeMessage)

chooseOption = int(
    input("Which option would you like to choose(1/2/3/4/5/6/7/8/9/10/11)?: "))

if chooseOption == 1:
    while True:
        firstInput = input("First number: ")
        if firstInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        firstNumber = float(firstInput)

        secondInput = input("Second number: ")
        if secondInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        secondNumber = float(secondInput)

        print(">", firstNumber + secondNumber)

if chooseOption == 2:
    while True:
        firstInput = input("First number: ")
        if firstInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        firstNumber = float(firstInput)

        secondInput = input("Second number: ")
        if secondInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        secondNumber = float(secondInput)

        print(">", firstNumber - secondNumber)

if chooseOption == 3:
    while True:
        firstInput = input("First number: ")
        if firstInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        firstNumber = float(firstInput)

        secondInput = input("Second number: ")
        if secondInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        secondNumber = float(secondInput)

        print(">", firstNumber * secondNumber)

if chooseOption == 4:
    while True:
        firstInput = input("First number: ")
        if firstInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        firstNumber = float(firstInput)

        secondInput = input("Second number: ")
        if secondInput.lower() == "back":
            print("Restarting script...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        secondNumber = float(secondInput)

        print(">", firstNumber / secondNumber)
        print("The remainder is:", firstNumber % secondNumber)

if chooseOption == 5:
    while True:
        userInput = input("Input the number: ")

        if userInput.lower() == "back":
            print("Going back...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        sqrt = float(userInput)
        print(">", sqrt * sqrt)

if chooseOption == 6:
    while True:
        firstInput = input("Bottom: ")

        if firstInput.lower() == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        bottomNumber = float(firstInput)
        secondInput = input("To the power of: ")

        if secondInput.lower() == ("back"):
            os.execl(sys.executable, sys.executable, *sys.argv)

        upperNumber = float(secondInput)
        print(">", bottomNumber, "to the power of ",
              upperNumber, "is: ", bottomNumber ** upperNumber)

if chooseOption == 7:
    while True:
        userInput = input("which number do you want to round?: ")

        if userInput.lower() == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        toRound = float(userInput)
        print(">", round(toRound))

if chooseOption == 8:
    while True:
        firstInput = input("Number: ")

        if firstInput.lower == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        Number = float(firstInput)

        secondInput = input("Percentage: ")

        if secondInput.lower == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        Percentage = float(secondInput)
        print(">", Percentage / 100 * Number)

if chooseOption == 9:
    while True:

        number = input("What's the Number?: ")
        found = False

        if number == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        number = int(number)

        for base in range(2, number + 1):
            for exponent in range(2, number + 1):
                if base ** exponent == number:

                    print(f"{number} is: {base}^{exponent}")
                    found = True
                    break

                if found:
                    break
        if not found:
            print(f"{number} cannot be expressed")

if chooseOption == 10:
    while True:
        num = input("Enter a number: ")

        if num == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        nInput = input("Enter the degree of the root: ")

        number = int(num)

        if nInput == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        n = int(nInput)

        a = 1
        b = number

        start = round(number ** (1/n))

        for i in range(start, 0, -1):
            if number % (i ** n) == 0:
                a = i
                b = number // (i ** n)
                break

        if b == 1:
            print(f"{n}-th root of {number} = {a}")
        else:
            print(f"{n}-th root of {number} = {a} * {n}-th_root({b})")

if chooseOption == 11:
    while True:
        userInput = input("Please enter the number: ")

        if userInput == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        num = int(userInput)
        for answer in range(1, num + 1):

            result = num / answer
            if result.is_integer():
                print(result)
