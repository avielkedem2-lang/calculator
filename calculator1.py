from operations import add, subtract, multiply, divide

print("!ברוכים הבאים למחשבון")
print("====================")


result1 = add(5, 3)
print(f"5 + 3 = {result1}")


result2 = subtract(10, 4)
print(f"10 - 4 = {result2}")

print(f"6 * 7 = {multiply(6, 7)}")
print(f"20 / 4 = {divide(20, 4)}")
print(f"10 / 0 = {divide(10, 0)}")
