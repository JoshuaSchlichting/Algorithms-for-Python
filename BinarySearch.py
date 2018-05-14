# The binary search algorithm divides a sorted list in half until if finds a targeted value. Each time the list
# is divided, the algorithm determines which half of the sorted list to search next based on if the targeted value
# is less than or greater than the median value of that sorted list. This goes on until there is one value left.
# This binary search function will raise an exception in the event that the targeted value does not exist in the list.


def binary_search(sorted_list, search_target):

    if len(sorted_list) > 1:
        mid_val_index = int(round(len(sorted_list) / 2))

        if search_target == sorted_list[mid_val_index]:
            return mid_val_index
        elif search_target < sorted_list[mid_val_index]:
            return binary_search(sorted_list[:mid_val_index], search_target)
        else:
            return binary_search(sorted_list[mid_val_index:], search_target)+len(sorted_list[:mid_val_index])
    elif len(sorted_list) == 1 & sorted_list[0] == search_target:
        return 0
    else:
        raise IndexError("Value does not exist within this sorted list")


if __name__ == "__main__":
    my_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    for i in range(len(my_list)):
        print(str(my_list[i]) + " is located at " + str(i))

    print(str(binary_search(my_list, 2048)))
