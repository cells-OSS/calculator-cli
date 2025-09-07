import os
import sys
import math
import ast
import operator

welcomeMessage = """
===============WELCOME===============

0 = Basic math expressions
1 = Find the given exponent of the given number
2 = Round a Number
3 = Find the given percentage of a number
4 = Finding the possible base(s) and the exponent(s) of the given number
5 = Finding the smallest possible n-th root of the given number
6 = Find the given numbers multipliers

TIP: If you want to come back to this menu at any time, just type 'back'

"""
print(welcomeMessage)

chooseOption = int(
    input("Which option would you like to choose(0/1/2/3/4/5/6)?: "))

while True:

    if chooseOption == 0:
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.floordiv,
            ast.Mod: operator.mod,
            ast.FloorDiv: operator.floordiv,
            ast.Pow: operator.pow,
        }

        def safe_eval(expr):

            node = ast.parse(expr, mode="eval").body

            def _eval(node):
                if isinstance(node, ast.BinOp):
                    if type(node.op) not in operators:
                        raise ValueError("Operator not allowed")

                    left = _eval(node.left)
                    right = _eval(node.right)

                    if isinstance(node.op, ast.Div):
                        
                        quotient = left // right
                        remainder = left % right
                        return f"{left} ÷ {right} = {quotient} remainder {remainder}"

                    return operators[type(node.op)](left, right)

                elif isinstance(node, ast.Constant):
                    if isinstance(node.value, (int, float)):
                        return node.value
                    else:
                        raise ValueError("Only numbers are allowed")

                elif isinstance(node, ast.Constant):
                    if isinstance(node.value, (int, float)):
                        return node.value
                    else:
                        raise ValueError("Only numbers are allowed")

                elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                    return -_eval(node.operand)

                else:
                    raise ValueError("Expression not allowed")

            return _eval(node)

        while True:
            expr = input("> ")
            if expr == "back":
                os.execl(sys.executable, sys.executable, *sys.argv)

            try:
                result = safe_eval(expr)
                print("=", result)
            except Exception as e:
                print("Error:", e)

    if chooseOption == 1:
        firstInput = input("Base: ")

        if firstInput.lower() == "back":
            break

        base = float(firstInput)
        secondInput = input("Exponent: ")

        if secondInput.lower() == "back":
            os.execl(sys.executable, sys.executable, *sys.argv)

        exponent = float(secondInput)
        print(">", base ** exponent)

    if chooseOption == 2:
        while True:
            userInput = input("> ")

            if userInput.lower() == "back":
                os.execl(sys.executable, sys.executable, *sys.argv)

            toRound = float(userInput)
            print(">", round(toRound))

    if chooseOption == 3:
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

    if chooseOption == 4:
        while True:

            number = input("> ")
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

    if chooseOption == 5:
        while True:
            num = input("Enter the number: ")

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

    if chooseOption == 6:
        while True:
            userInput = input("> ")

            if userInput == "back":
                os.execl(sys.executable, sys.executable, *sys.argv)

            num = int(userInput)
            for answer in range(1, num + 1):

                result = num / answer
                if result.is_integer():
                    print(result)
