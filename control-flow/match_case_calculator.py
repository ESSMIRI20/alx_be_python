num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
match input("Choose the operation (+, -, *, /):"):
    case "+" :
        print("The result is {}.".format(num1 + num2))
    case "-" :
        print("The result is {}.".format(num1 - num2))
    case "*" :
        print(f"The result is {num1 * num2}.")
    case "/" :
        if num2 == 0:
            print("Cannot divide by zero.")
        else :
            print("The result is {}.".format(num1 / num2))
