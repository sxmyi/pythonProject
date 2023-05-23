#1
x = 1
if x == 10:
    print("x is equal to 10")
else:
    print("x is not equal to 10")

x = 1
y = 2
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

x = 1
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

x = 10
y = 6
if x == 10 and y == 5:
    print("x is equal to 10 and y is equal to 5")
else:
    print("x and y are not equal to their respective values")

x = 10
y = 6
if x > 10 or y < 6:
    print("either x is greater than 10 or y is less than 5")
else:
    print("neither x is greater than 10 nor y is less than 5")