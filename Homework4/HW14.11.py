# Alvin Nguyen 2055636
# function sort list descending order
def selection_sort_descend_trace(integer):
    for i in range(len(integer) - 1):
        a = i
        for n in range(i + 1, len(integer)):
            if integer[a] < integer[n]:
                a = n
        integer[i], integer[a] = integer[a], integer[i]
        for value in integer:
            print(value, end=" ")
        print()
    return integer


if __name__ == "__main__":
    integers = [int(x) for x in input("").split()]
    # call to sort list
    selection_sort_descend_trace(integers)
