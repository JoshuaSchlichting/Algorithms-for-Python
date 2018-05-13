# The bubble sort algorithm starts from the right side of a list and moves left with a scale.
# The scale holds 2 values, and determines which is higher than the other. If the left value it is holding
# turns out to be higher than the right value, the two values are swapped, and the scale iterates 1 position
# to the left and performs the same measurement.


def bubble_sort(list_of_values):

    value_count = len(list_of_values)
    for index in range(0, value_count-1):
        for j in range(1, value_count-index):
            right_value = list_of_values[value_count-j]
            left_value = list_of_values[value_count-j-1]
            if left_value > right_value:
                list_of_values[value_count-j] = left_value
                list_of_values[value_count-j-1] = right_value

    return list_of_values


if __name__ == "__main__":
    list_of_int = [500, 1000, 800, 100, 80, 20, 100, .5,  90, 30, 50, 10, 1, 32, 190, .01, 67, 500]
    print(str(bubble_sort(list_of_int)))
