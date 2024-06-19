def rec_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + rec_sum(arr[1:])


assert rec_sum(list(range(2, 7, 2))) == 12
