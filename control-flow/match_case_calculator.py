n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
match input("Choose the operation (+, -, *, /):"):
    case "+" :
        print("The result is {}.".format(n1 + n2))
    case "-" :
        print("The result is {}.".format(n1 - n2))
    case "*" :
        print(f"The result is {n1 * n2}.")
    case "/" :
        if n2 == 0:
            print("Cannot divide by zero.")
        else :
            print("The result is {}.".format(n1 / n2))
