def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator, e.g. +, -, * or /: ")
    result = calculator(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")



def calculator(num1, num2, operator):
    if operator == "+":
        return round(num1 + num2, 2)
    elif operator == "-":
        return round(num1 - num2, 2)
    elif operator == "*":
        return round(num1 * num2, 2)
    elif operator == "/":
        return round(num1 / num2, 2)
    else:
        return "Usage: calculator(number 1, number 2, operator)"


if __name__ == "__main__":
    main()
