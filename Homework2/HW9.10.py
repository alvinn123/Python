# Alvin Nguyen 2055636
# import module
import csv

filename = input()
# open given files
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    dictionary = dict()
    for i in reader:
        for a in i:
            if a in dictionary:
                dictionary[a] += 1
            else:
                dictionary[a] = 1
    for n in list(dictionary.keys()):
        print("{} {}".format(n, dictionary[n]))
