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


# the whole idea with this algorithm is that you:
# 1) pick a pivot
# 2) sort smaller to the left, larger to the right
def qs_constant_space(arr):
    # recursive function that calls on divided arrays
    def qs(arr, lo, hi):
        if lo >= hi:
            return
        pivot = partition(arr, lo, hi)
        qs(arr, lo, pivot - 1)
        qs(arr, pivot + 1, hi)

    # picks the pivot and weak sorts the array properly (meaning the array is not entirely sorted)
    # but still is sorted in some (weak) manner by the pivot
    def partition(arr, lo, hi):
        pivot = arr[hi]
        idx = lo - 1
        for i in range(lo, hi):
            if arr[i] <= pivot:
                idx += 1
                arr[idx], arr[i] = arr[i], arr[idx]
        idx += 1
        arr[hi], arr[idx] = arr[idx], arr[hi]
        return idx

    qs(arr, 0, len(arr) - 1)
    return arr


def run():
    lst = [randint(0, 50) for _ in range(10)]
    print("sorting: ", lst)
    assert qs(lst) == sorted(lst)
    assert qs_rand_pivot(lst) == sorted(lst)
    assert qs_constant_space(lst) == sorted(lst)
    print("all sorts worked!", qs(lst))


if __name__ == "__main__":
    run()
