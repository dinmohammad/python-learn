num1 = float(input('Type First Number : '))
op = input('Type operator : ')
num2 = float(input('Type Second Number : '))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print('Invalid Operator')