# Alvin Nguyen 2055636
# User inputs
a = int(input())
b = int(input())
c = int(input())

a2 = int(input())
b2 = int(input())
c2 = int(input())
# Solution set to false by default
solution = False
# check if dateUser and y satisfy the equations
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and a2 * x + b2 * y == c2:
            print(x, y)
            solution = True  # satisfied set to true

if not solution:
    print("No solution")
