#Calculator
from operations import add, subtract, multiply, divide, operations
from clear import clear_console
from art import logo

def calculator():
    """The calculator() function starts the calculator program. It has a reset feature for a brand new operation, continued sequence of operations using previous result as num1, and can exit program"""

    while True:
        clear_console()
        print(F"{logo}\nWelcome to Calculator!")

        while True:
            num1 = input("What's the first number?:\n")
            try:
                num1 = float(num1)
                break
            except ValueError as e:
                print(F"Error: {e} - Please proivde a valid number")

        while True:
            while True:
                num2 = input("What's the second number?:\n")
                try:
                    num2 = float(num2)
                    break
                except ValueError as e:
                    print(F"Error: {e} - Please proivde a valid number")

            for key in operations:
                print(key)
            while True:
                symbol = input("Choose an operation:\n")
                if symbol not in operations:
                    print("Please provide a valid symbol")
                else:
                    break

            if symbol in operations:
                function = operations[symbol]
                result = function(num1, num2)
                print(F"{num1} {symbol} {num2} = {result}")
            else:
                print("Please choose a valid operator")

            loop = input(F"Would you like to continue calculating with {result}? - Type Y for yes or N for new opeartion or anything else to exit\n").lower()
            if loop == "n":
                #Recursion to start new operation with two new number inputs
                break
            elif loop == "y":
                num1 = result
            else:
                print("Exiting...")
                return

calculator()
