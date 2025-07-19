from enum import Enum

class enOperation(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_operation():
    while True:
        user_input = input("Enter operation (1:Add, 2:Sub, 3:Mul, 4:Div): ")
        if is_number(user_input):
            operation_type = int(user_input)
            if operation_type in [1, 2, 3, 4]:
                return operation_type
            else:
                print("Invalid operation. Please enter 1, 2, 3, or 4.")
        else:
            print("Invalid input. Please enter a number.")

def get_numbers():
    while True:
        num1_input = input("Enter first number: ")
        num2_input = input("Enter second number: ")
        if is_number(num1_input) and is_number(num2_input):
            return float(num1_input), float(num2_input)
        else:
            print("Invalid input. Please enter numeric values.")

def calculate():
    num1, num2 = get_numbers()
    operation_type = get_operation()

    # if operation_type == Enum.ADD:
#     #     result = num1 + num2
#     # elif operation_type == Enum.SUB:
#     #     result = num1 - num2
#     # elif operation_type == Enum.MUL:
#     #     result = num1 * num2
#     # elif operation_type == Enum.DIV:
#     #     if num2 == 0:
#     #         print("Error: Division by zero is not allowed.")
#     #         return
#     #     result = num1 / num2
#     # else:
#     #     print("Invalid operation selected.")
#     #     return
#     # print(f"Result: {result}")


    operations = {
        enOperation.ADD: lambda num1, num2: num1 + num2,
        enOperation.SUB: lambda num1, num2: num1 - num2,
        enOperation.MUL: lambda num1, num2: num1 * num2,
        enOperation.DIV: lambda num1, num2: num1 / num2
    }

    if operation_type == enOperation.DIV.value and num2 == 0:
        print("Error: Division by zero.")
        return

    result = operations[enOperation(operation_type)](num1, num2)
    print(f"Result: {result}")

def ask_repeat():
    while True:
        answer = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

def reapete_it():
    while True:
        calculate()
        if not ask_repeat():
            print("Exiting the calculator.")
            break

reapete_it()
