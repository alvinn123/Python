# Alvin Nguyen 2055636

num_calls = 0


def partition(user_ids, i, a):
    sort = user_ids[a]
    index = i - 1
    for j in range(i, a):
        if user_ids[j] <= sort:
            index += 1
            user_ids[index], user_ids[j] = user_ids[j], user_ids[index]
    user_ids[index + 1], user_ids[a] = user_ids[a], user_ids[index + 1]
    return index + 1


# def quicksort
def quicksort(user_ids, i, a):
    if i < a:
        sort = partition(user_ids, i, a)
        quicksort(user_ids, i, sort - 1)
        quicksort(user_ids, sort + 1, a)


# main function
if __name__ == "__main__":
    # user id list
    user_ids = []
    # user inputs ids
    user_id = input()
    # stop at -1
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    # calling quicksort()
    quicksort(user_ids, 0, len(user_ids) - 1)
    num_calls = int(2 * len(user_ids) - 1)
    # output num_calls
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
