FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

a = float(input("Enter the temperature to convert:"))
b = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

def convert_to_celsius(fahrenheit):
    fahrenheit = (a - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit

def convert_to_fahrenheit(celsius):
    celsius = a * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return celsius

match b:
    case 'F' :
        print(f"{a}°F is {convert_to_celsius(a)}°C")
    case 'C' :
        print(f"{a}°C is {convert_to_fahrenheit(a)}°F")
    case _:
        print("Invalid temperature. Please enter a numeric value.")