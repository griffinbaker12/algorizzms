# thinking about this wrong, you want to do the internal loop n times
# each iteration you can move it over...hence the name bubble sort
def bubble_sort(arr):
    """
    Idea here is that you select the smallest value each time you loop through
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                if not swapped:
                    swapped = True
        if not swapped:
            break
    return arr


print(bubble_sort([1, 4, 5, 1, 2]))


def bubble_sort_2(arr):
    n = len(arr)
    _i = 0
    while True:
        swapped = False
        for i in range(0, n - _i - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                swapped = True
        if not swapped or _i >= n - 1:
            break
        else:
            _i += 0
    return arr


print(bubble_sort_2([1, 4, 5, 1, 2]))
