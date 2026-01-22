from operations import add, subtract, multiply, divide
from advanced import *
from ui import *
from history import add_to_history, show_history, clear_history
from constants import *
from geometry import *
print("╔════════════════════════════╗")
print("║ welcome to the calculater! ║")
print("║          version 4.0       ║")
print("╚════════════════════════════╝")


while True:
    choice = show_menu()

    if choice == "0":
        print("goodbye")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number("enter a number")
        num2 = get_number("enter a second number")

        if choice =="1":
            result = add(num1, num2)
            print(f"result: {result}")
            add_to_history(f"{num1} + {num2}", result)


        elif choice == "2":
            result1 = subtract(num1, num1)
            print(f"result {result1}")
            add_to_history(f"{num1} - {num2}", result1)


        elif choice == "3":
            result2 = multiply(num1, num2)
            print(f"result {result2}")
            add_to_history(f"{num1} * {num2}", result2)


        elif choice == "4" :
            result3 = divide(num1, num2)
            print(f"result: {result3}")
            add_to_history(f"{num1} // {num2}", result3)


        elif choice == "5":
            result4 = power(num1, num2)
            print(f"result: {result4}")
            add_to_history(f"{num1} ** {num2}", result4)


    elif choice == "6":
        num = get_number("enter a number")
        print(f"result: {square_root(num)}")
        add_to_history(f"square root of {num} ==", num)


    elif choice == "7":
        num3 = get_number("enter a number")
        print(f"result: {factorial(num3)}")

    elif choice == "8":
        show_history()

    elif choice == "9":
        clear_history()

    elif choice == "10":
        show_constants()

    elif choice == "11":
        r = get_number("enter a number")
        print(f"result: {area_circle(r)}")

    elif choice == "12":
        hi = get_number("enter a number")
        lo = get_number("enter a number")
        print(f"result: {rectangle_area(lo, hi)}")

    elif choice == "13":
        base = get_number("enter a number")
        hei = get_number("enter a number")
        print(f"result: {triangle_area(base, hei)}")


    else:
        print("your choice it is not a legal")
