list_of_operations = ['+', '-', '*', '/']
while True:
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        op = input("Choose operation + - * /")
        if op in list_of_operations:
            if op == "+":
                print(a + b)
            elif op == "-":
                print(a-b)
            elif op == "-":
                print(a - b)
            elif op == "*":
                print(a * b)
            elif op == "/":
                print(round(a/b, 2))
        else:
            print("Choose another operation")
    except(ZeroDivisionError, ValueError):
        print("Choose another numbers")
    else:
        print("...")