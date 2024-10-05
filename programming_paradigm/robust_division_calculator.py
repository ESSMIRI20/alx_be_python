def safe_divide(numerator, denominator):
    try:
        num1 = int(numerator)
        num2 = int(denominator)
        if num2 != 0:
            return f"The result of the division is {num1 / num2}"
        else:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
