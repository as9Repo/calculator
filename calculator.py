# A simple Python calculator

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter Choice: "))

    if choice == 5:
        break

    num1 = float(input("Enter operand #1: "))
    num2 = float(input("Enter operand #2: "))

    if choice == 1:
        print("Result:", num1 - num2)
    elif choice == 2:
        print("Result:", num1 + num2)
    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        print("Result:", num1 / num2)