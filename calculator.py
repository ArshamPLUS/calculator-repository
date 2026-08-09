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
        return "Error: can not divide by zero."

def main():
    while True:

        print("Select operation:")
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. EXIT")

        operation = input("Choose an operation (1-5): ")

        if operation == "5":
            print("Exiting the calculator.")
            break
        try:
            numberA = float(input("Enter the first number: "))
            numberB = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        print("------------------------------")
        if operation == "1":
            print("addition result:", add(numberA, numberB))

        elif operation == "2":
            print("subtraction result:", subtract(numberA, numberB))

        elif operation == "3":
            print("multiplication result:", multiply(numberA, numberB))

        elif operation == "4":
            print("division result:", divide(numberA, numberB))

        else:
            print("Invalid operation. Please choose a valid option.")
        print("------------------------------")
        
if __name__ == "__main__":
    main()