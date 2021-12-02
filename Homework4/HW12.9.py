# Alvin Nguyen 2055636

parts = input().split()
# takes input index of 0 only (takes only first name)
name = parts[0]
# list name and age
names = []

ages = []
# stops code when user inputs -1
while name != '-1':

    try:

        age = int(parts[1]) + 1

    except:

        age = 0

    # append name and age

    names.append(name)

    ages.append(age)

    # get next line

    parts = input().split()

    name = parts[0]
# for loop print for output name and ages
for i in range(0, len(names)):
    print('{} {}'.format(names[i], ages[i]))
