def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    return a // b


x = float(input("A: "))
operator = input("Enter operator: ")
y = float(input("B: "))
print(calculator(x, y, operator))
