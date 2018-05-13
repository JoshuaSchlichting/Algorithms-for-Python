# Insertion Sort


def insertion_sort(list_of_values):

    for i in range(1, len(list_of_values)):
        if list_of_values[i] < list_of_values[i-1]:
            current_val = list_of_values[i]
            for j in range(1, i+1):
                if current_val < list_of_values[i-j]:
                    tmp = list_of_values[i-j]
                    list_of_values[i-j] = current_val
                    list_of_values[i-j+1] = tmp
                else:
                    break

    return list_of_values


if __name__ == "__main__":
    my_list = [90, 1000, 4, 5, 1, .5, 10, 999, 3]
    print(insertion_sort(my_list))
