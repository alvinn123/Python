# Alvin Nguyen 2055636
user_input = input().split()

for n in user_input:
    count = 0
    for item in user_input:
        if n == item:
            count += 1
    print(n, count)

