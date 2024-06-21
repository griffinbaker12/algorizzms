# randint is inclusive on both ends
from random import randint

# time => avg = nlogn, worst = n2; depends on if the list is already (pretty much) sorted
# space => ins't it the same as the above


def qs(arr):
    if len(arr) < 2:
        return arr

    # can change how we select the pivot
    pivot = arr[0]
    # and this was the main thing...make the array smaller each time b/c we selected
    # this element off
    lower_arr = [v for v in arr[1:] if v <= pivot]
    higher_arr = [v for v in arr[1:] if v > pivot]

    return qs(lower_arr) + [pivot] + qs(higher_arr)


def get_pivot(arr):
    return arr[randint(0, len(arr) - 1)]


def qs_rand_pivot(arr):
    if len(arr) < 2:
        return arr

    pivot = get_pivot(arr)

    lower_arr = []
    same_arr = []
    higher_arr = []

    for v in arr:
        if v < pivot:
            lower_arr.append(v)
        elif v > pivot:
            higher_arr.append(v)
        else:
            same_arr.append(v)

    return qs(lower_arr) + same_arr + qs(higher_arr)


def run():

    lst = [randint(0, 50) for i in range(10)]
    print("sorting: ", lst)
    assert qs(lst) == sorted(lst)
    assert qs_rand_pivot(lst) == sorted(lst)
    print("both sorts worked!", qs(lst))


if __name__ == "__main__":
    run()
