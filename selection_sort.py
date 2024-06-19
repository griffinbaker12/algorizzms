import random

TEST_NUM = 10


def selection_sort(arr):
    """
    Select smallest value every time
    """
    sorted = []
    arr_copy = arr[:]
    for _ in range(len(arr)):
        smallest_idx = 0
        for j, val in enumerate(arr_copy):
            if val < arr_copy[smallest_idx]:
                smallest_idx = j
        sorted.append(arr_copy.pop(smallest_idx))
    return sorted


def random_arr_of(length=10, start=1, end=100):
    """
    Create arrays of random length
    """
    return [random.randint(start, end) for _ in range(length)]


for _ in range(TEST_NUM):
    rand_arr = random_arr_of(length=10)
    assert selection_sort(rand_arr) == sorted(rand_arr)

print("*** all tests passed ***")
