import os
import sys
import subprocess
import ast
import operator
import pyfiglet
import requests
from packaging import version


__version__ = "v2.4"


def get_latest_release_tag():
    try:
        url = "https://api.github.com/repos/cells-OSS/pyculator/releases/latest"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["tag_name"].lstrip("v")
    except Exception as e:
        print("Failed to check for updates:", e)
        return __version__.lstrip("v")


def is_update_available(current_version):
    latest = get_latest_release_tag()
    return version.parse(latest) > version.parse(current_version.lstrip("v"))


def download_latest_script():
    latest_version = get_latest_release_tag()
    filename = f"pyculator-v{latest_version}.py"
    url = "https://raw.githubusercontent.com/cells-OSS/pyculator/main/calc.py"
    response = requests.get(url)
    lines = response.text.splitlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.rstrip() + "\n")
    print(
        f"Current version: {__version__}, Latest: v{get_latest_release_tag()}")
    print(
        f"Downloaded update as '{filename}'. You can now safely delete the old version.")

    input("Press Enter to exit...")
    exit()


if os.path.exists("welcome_message.conf"):
    with open("welcome_message.conf", "rb") as configFile:
        welcomeMessage = configFile.read().decode()
else:
    welcomeMessage = """
    ===============WELCOME===============
    """

if os.path.exists("figlet.conf"):
    with open("figlet.conf", "rb") as figlet_configFile:
        figlet_config = figlet_configFile.read().decode()
        if figlet_config == "True":
            welcomeMessage = pyfiglet.figlet_format(welcomeMessage)

if os.path.exists("auto_update.conf"):
    with open("auto_update.conf", "rb") as auto_update_configFile:
        auto_update_config = auto_update_configFile.read().decode()
        if auto_update_config == "True":
            if is_update_available(__version__):
                print("New version available!")
                download_latest_script()


menu = """

1 = Basic math expressions
2 = Find the given exponent of the given number
3 = Round a Number
4 = Find the given percentage of a number
5 = Finding the possible base(s) and the exponent(s) of the given number
6 = Finding the smallest possible n-th root of the given number
7 = Find the given numbers multipliers
8 = Settings

TIP: If you want to come back to this menu at any time, just type "back"
"""
print(welcomeMessage, menu)

chooseOption = int(
    input("Which option would you like to choose(0/1/2/3/4/5/6/7)?: "))

while True:

    if chooseOption == 1:
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
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            try:
                result = safe_eval(expr)
                print("=", result)
            except Exception as e:
                print("Error:", e)

    if chooseOption == 2:
        firstInput = input("Base: ")

        if firstInput.lower() == "back":
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

        base = float(firstInput)
        secondInput = input("Exponent: ")

        if secondInput.lower() == "back":
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

        exponent = float(secondInput)
        print(">", base ** exponent)

    if chooseOption == 3:
        while True:
            userInput = input("> ")

            if userInput.lower() == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            toRound = float(userInput)
            print(">", round(toRound))

    if chooseOption == 4:
        while True:
            firstInput = input("Number: ")

            if firstInput.lower() == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            Number = float(firstInput)

            secondInput = input("Percentage: ")

            if secondInput.lower() == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            Percentage = float(secondInput)
            print(">", Percentage / 100 * Number)

    if chooseOption == 5:
        while True:

            number = input("> ")
            found = False

            if number == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

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

    if chooseOption == 6:
        while True:
            num = input("Enter the number: ")

            if num == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            nInput = input("Enter the degree of the root: ")

            number = int(num)

            if nInput == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

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

    if chooseOption == 7:
        while True:
            userInput = input("> ")

            if userInput == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            num = int(userInput)
            for answer in range(1, num + 1):

                result = num / answer
                if result.is_integer():
                    print(result)

    if chooseOption == 8:
        settingsMenu = """
    ===============SETTINGS===============

    1 = Change welcome message
    2 = Figlet welcome message
    3 = Reset welcome message
    4 = Change auto-update settings
    """
        print(settingsMenu)

        chooseSetting = input(
            "Which setting would you like to change(1/2/3/4)?: ")

        if chooseSetting.lower() == "back":
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

        if chooseSetting == "1":
            new_welcomeMessage = input("New welcome message: ")

            if new_welcomeMessage.lower() == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            with open("welcome_message.conf", "wb") as configFile:
                configFile.write(new_welcomeMessage.encode())

                print("Changes saved successfully!")
                input("Press any key to restart...")
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

        if chooseSetting == "2":
            figletWelcome = """
        ===============FIGLET===============

        1 = Turn on
        2 = Turn off
        """

            print(figletWelcome)
            figletOption = input(
                "Which option would you like to choose(1/2)?: ")

            if figletOption.lower() == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            if figletOption == "0":
                with open("figlet.conf", "wb") as figlet_configFile:
                    figlet_configFile.write("True".encode())

                    print("Changes saved successfully!")
                    input("Press any key to restart...")
                    subprocess.Popen([sys.executable] + sys.argv)
                    sys.exit()

            if figletOption == "2":
                with open("figlet.conf", "wb") as figlet_configFile:
                    figlet_configFile.write("False".encode())

                    print("Changes saved successfully!")
                    input("Press any key to restart...")
                    subprocess.Popen([sys.executable] + sys.argv)
                    sys.exit()

        if chooseSetting == "3":
            if os.path.exists("welcome_message.conf"):
                os.remove("welcome_message.conf")
                print("Changes saved successfully!")
                input("Press any key to restart...")
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()
            else:
                print("You haven't changed the welcome message yet!")
                input("Press any key to restart...")
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

        if chooseSetting == "4":
            aUpdateMenu = """
    ===============AUTO-UPDATE===============

    1 = Turn on
    2 = Turn off
    """

            print(aUpdateMenu)
            aUpdateOption = input(
                "Which option would you like to choose(1/2)?: ")

            if aUpdateOption.lower() == "back":
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()

            if aUpdateOption == "1":
                with open("auto_update.conf", "wb") as auto_update_configFile:
                    auto_update_configFile.write("True".encode())

                    print("Changes saved successfully!")
                    input("Press any key to restart...")
                    subprocess.Popen([sys.executable] + sys.argv)
                    sys.exit()

            if aUpdateOption == "2":
                with open("auto_update.conf", "wb") as auto_update_configFile:
                    auto_update_configFile.write("False".encode())

                    print("Changes saved successfully!")
                    input("Press any key to restart...")
                    subprocess.Popen([sys.executable] + sys.argv)
                    sys.exit()
