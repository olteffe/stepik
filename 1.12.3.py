first, second, operation = float(input()), float(input()), input()
if operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "/":
    if second == 0:
        print("Деление на 0!")
    else:
        print(first / second)
elif operation == "*":
    print(first * second)
elif operation == "mod":
    if second == 0:
        print("Деление на 0!")
    else:
        print(first % second)
elif operation == "pow":
    print(first ** second)
elif operation == "div":
    if second == 0:
        print("Деление на 0!")
    else:
        print(first // second)

# so many beautiful if-elif
