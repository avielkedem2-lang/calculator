from operations import add, subtract, multiply, divide
from advanced import *
from ui import *

print("!ברוכים הבאים למחשבון")
print("====================")

while True:
    choice = show_menu()

    if choice == "0":
        print("goodbye")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number("enter a number")
        num2 = get_number("enter a second number")

        if choice =="1":
            print(f"result: {add(num1, num2)}")

        elif choice == "2":
            print(f"result {subtract(num1, num1)}")

        elif choice == "3":
            print(f"result {multiply(num1, num2)}")

        elif choice == "4" :
            print(f"result: {divide(num1, num2)}")

        elif choice == "5":
            print(f"result: {power(num1, num2)}")

    elif choice == "6":
        num = get_number("enter a number")
        print(f"result: {square_root(num)}")

    elif choice == "7":
        num3 = get_number("enter a number")
        print(f"result: {factorial(num3)}")
    else:
        print("your choice it is not a legal")
