#Add
def add(n1, n2):
    """The add() function takes in two numbers and performs an addition operation. It returns the result"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """The subtract() function takes in two numbers and performs a subtraction operation. It returns the result"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """The mulitply() function takes in two numbers and performs a multiplication operation. It returns the result"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """The divide() function takes in two numbers and performs a division operation. It returns the result"""
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError as e:
        return F"Error: {e}"

#We can use the NAME of the function in a KEY-VALUE pair inside a Dictionary to store the function --> NOTE: We can later access the function with square bracket notaiton through the KEY and store it inside a variable, which we can treat as a function and pass arguments to it inside a set of parenthesis
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}