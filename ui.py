def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("error: enter a number!")
def show_menu():
    print("\n=== menu === ")

    print("connection 1 ")
    print("subtract 2")
    print("multiply 3")
    print("divide 4")
    print("power 5")
    print("square_root 6")
    print("factorial 7")
    print("--- היסטוריה ---")
    print("הצג היסטוריה .8")
    print("נקה היסטוריה .9")
    print("הצג קבועים 10.")
    print("exit 0")
    return input("choose")

