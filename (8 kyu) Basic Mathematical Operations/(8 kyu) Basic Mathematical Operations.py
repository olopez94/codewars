def basic_op(operator, value1, value2):
    #your code here
    try:
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        elif operator == "/":
            return value1 / value2
    except:
        return None
     
