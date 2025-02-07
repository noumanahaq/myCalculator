from main import MyCalculator

calculator = MyCalculator()

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", calculator.add(num1, num2))
        elif op == "-":
            print("Result:", calculator.subtract(num1, num2))
        elif op == "*":
            print("Result:", calculator.multiply(num1, num2))
        elif op == "/":
            print("Result:", calculator.divide(num1, num2))
        else:
            print("Invalid operation!")

    except ValueError:
        print("Error! Please enter valid numbers.")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        break
