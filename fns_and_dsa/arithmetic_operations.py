
def perform_operation(num1, num2, operation):
        match operation:
            case "add" :
                result = num1 + num2
            case "subtract" :
                result = num1 - num2
            case "multiply" :
                result = num1 * num2
            case "divide" :
                  if(num2 != 0):
                       result = num1 / num2
                  elif num2 == 0:
                       result = "cannot divide by 0"
            case _:
                  result = "impossible"
        return result