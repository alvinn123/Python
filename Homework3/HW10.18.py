# Alvin Nguyen 2055636
numbers = input()
my_list = numbers.split()

new_list = []

for i in my_list:
    # checking if negative
    if int(i) > -1:
        new_list.append(int(i))
# sort the list smallest to biggest
new_list.sort()

for x in new_list:
    print(x, end=' ')

