# ============================================
# COS202 MATHEMATICAL CALCULATOR
# Developed in Python
# ============================================

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    while True:
        print("=" * 50)
        print("        MATHEMATICAL CALCULATOR")
        print("=" * 50)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Floor Division (//)")
        print("6. Exponent (**)")
        print("7. Modulus (%)")
        print("8. Clear Screen (C)")
        print("9. OFF (Exit)")
        print("=" * 50)

        choice = input("Select an operation (1-9): ")

        if choice == "9":
            print("\nCalculator is OFF.")
            print("Thank you for using the Mathematical Calculator!")
            break

        elif choice == "8":
            clear_screen()
            continue

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                    print(f"\nResult: {num1} + {num2} = {result}")

                elif choice == "2":
                    result = num1 - num2
                    print(f"\nResult: {num1} - {num2} = {result}")

                elif choice == "3":
                    result = num1 * num2
                    print(f"\nResult: {num1} * {num2} = {result}")

                elif choice == "4":
                    if num2 == 0:
                        print("\nError! Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        print(f"\nResult: {num1} / {num2} = {result}")

                elif choice == "5":
                    if num2 == 0:
                        print("\nError! Division by zero is not allowed.")
                    else:
                        result = num1 // num2
                        print(f"\nResult: {num1} // {num2} = {result}")

                elif choice == "6":
                    result = num1 ** num2
                    print(f"\nResult: {num1} ** {num2} = {result}")

                elif choice == "7":
                    if num2 == 0:
                        print("\nError! Division by zero is not allowed.")
                    else:
                        result = num1 % num2
                        print(f"\nResult: {num1} % {num2} = {result}")

            except ValueError:
                print("\nInvalid input! Please enter numbers only.")

        else:
            print("\nInvalid choice! Please select from 1 to 9.")

        input("\nPress Enter to continue...")
        clear_screen()


# Program starts here
clear_screen()
print("=" * 50)
print("        WELCOME TO PYTHON CALCULATOR")
print("=" * 50)
input("Press Enter to turn ON the calculator...")

clear_screen()
calculator()