def binary_search(arr, item):
    lo = 0
    hi = len(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        val = arr[mid]

        if val == item:
            return mid
        elif val > item:
            hi = mid
        else:
            lo = mid + 1

    return None


lst = list(range(1, 10, 2))
assert binary_search(lst, 3) == 1
assert binary_search(lst, -1) is None
