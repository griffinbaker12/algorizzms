def qs(arr, lo, high):
    if lo >= high:
        return

    p = partition(arr, lo, high)
    qs(arr, lo, p - 1)
    qs(arr, p + 1, high)

    return arr


def partition(arr, lo, high):
    pivot = arr[high]

    idx = lo - 1

    for i in range(lo, high):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    idx += 1
    arr[high], arr[idx] = arr[idx], arr[high]
    return idx


def quick_sort(arr):
    return qs(arr, 0, len(arr) - 1)


print(quick_sort([84, 6, 84]))
