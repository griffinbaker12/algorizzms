def num_items_in_list(arr):
    if len(arr) == 0:
        return 0
    return 1 + num_items_in_list(arr[1:])


assert num_items_in_list(list(range(10))) == 10
