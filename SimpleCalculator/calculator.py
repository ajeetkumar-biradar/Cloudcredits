def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"Result: {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {divide(num1, num2)}")

    except ValueError:
        print("Invalid input. Please enter numbers and select a valid operation.")

if __name__ == "__main__":
    calculator()
