def get_max_num(arr, max=float("-inf")):
    if len(arr) == 0:
        return max
    return get_max_num(arr[1:], arr[0] if arr[0] > max else max)


assert get_max_num([1, 2, 3]) == 3
assert get_max_num([5, 2, 8, 10, 20, 345, 1, -1]) == 345
