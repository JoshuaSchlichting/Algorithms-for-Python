# Selection Sort algorithm
# This algorithm finds the smallest value and moves it to the first position in the list. Then it finds the next
# smallest value and moves it to the position right of the previously filled position. This process is repeated
# until the end of the list has been reached. Each time a lower value is discovered and moved to the left, the
# value being replaced is moved to the low values old position.


def selection_sort(list_of_values):

    for j in range(0, len(list_of_values)-1):
        for i in range(j, len(list_of_values)):
            if list_of_values[i] <= list_of_values[j]:
                new_val = list_of_values[i]
                list_of_values[i] = list_of_values[j]
                list_of_values[j] = new_val

    return list_of_values


if __name__ == "__main__":
    list_of_numeric = [90, 8, 2, 6, 1, 3, 90, 12, 42, 12, 3]
    print(str(selection_sort(list_of_numeric)))

