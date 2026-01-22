from operations import add, subtract, multiply, divide
from advanced import power, square_root


assert add(2,3) == 5,"הבדיקת חיבור נכשלה"
assert subtract(10, 4) == 6, "בדיקת חיסור נכשלה"
assert multiply(3,4) == 12, "בדיקת כפל נכשלה"
assert divide(20, 4) == 5, "בדיקת חילוק נכשלה"
assert power(2, 3) == 8, "בדיקת חזקה נכשלה"
assert square_root(16) == 4, "בדיקת שורש נכשלה"

print("הכל הבדיקות עברו בהצלחה!")