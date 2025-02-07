# My First Calculator App

# Main class
class MyCalculator():

    # Addition
    def add(self, x, y):
        return x + y
    
    # Subtraction
    def subtract(self, x, y):
        return x - y

    # Multiplication
    def multiply(self, x, y):
        return x * y
    
    # Division
    def divide(self, x, y):
        # Zero division error
        if y == 0:
            return "Error! Division by zero."
        return x / y