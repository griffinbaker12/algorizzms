import random

# def qs_const(arr, lo, high, shld_print=False):
#     if lo >= high:
#         return
#
#     piv = arr[lo]
#     idx = lo
#     for i in range(idx + 1, high + 1):
#         if arr[i] <= piv:
#             idx += 1
#             arr[idx], arr[i] = arr[i], arr[idx]
#
#     if shld_print:
#         print(arr)
#
#     arr[lo], arr[idx] = arr[idx], arr[lo]
#
#     if shld_print:
#         print(arr)
#
#     qs_const(arr, lo, idx - 1)
#     qs_const(arr, idx + 1, high)
#
#     return arr


# def qs_const(arr, lo, high, shld_print=False):
#     if lo >= high:
#         return
#
#     piv = arr[lo]
#     idx = lo + 1
#     for i in range(idx, high + 1):
#         if arr[i] <= piv:
#             arr[idx], arr[i] = arr[i], arr[idx]
#             idx += 1
#
#     if shld_print:
#         print(arr)
#
#     arr[lo], arr[idx - 1] = arr[idx - 1], arr[lo]
#
#     if shld_print:
#         print(arr)
#
#     qs_const(arr, lo, idx - 2)
#     qs_const(arr, idx, high)
#
#     return arr


def qs_const(arr, lo, high, shld_print=False):
    if lo >= high:
        return

    piv = arr[lo]
    idx = lo + 1
    print(arr, lo, high)
    for i in range(idx, high + 1):
        if arr[i] <= piv:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1

    if shld_print:
        print(arr)

    arr[lo], arr[idx - 1] = arr[idx - 1], arr[lo]

    if shld_print:
        print(arr)

    qs_const(arr, lo, idx - 1)
    qs_const(arr, idx + 1, high)

    return arr


print(qs_const([5, 1, 5, 9, 7], 0, 2))
print(qs_const([84, 6, 84], 0, 2))
# exit()

# print(qs_const([4, 49, 1, 40, 68], 0, 4, True))
# print(qs_const([53, 85, 45, 86, 47], 0, 4, True))
# print(qs_const([84, 84, 6], 0, 2, True))
# print(qs_const([84, 6, 84], 0, 2, True))
# print(qs_const([14, 69, 84, 6, 84], 0, 4, True))
# exit()


# time and space would both be nlogn?
# time because unless the items are all sorted already,
# and we assume that the values are randomly distributed,
# then each branch will but the search space in half
# and then I think space is the same because we are re-allocating
# in total N elements across log n levels
def qs(arr):
    if len(arr) == 0:
        return arr

    # arb selection
    piv = arr[0]

    return (
        [v for v in arr if v < piv]
        + [v for v in arr if v == piv]
        + [v for v in arr if v > piv],
    )


def main():
    ARRAY_LEN, TESTS = 5, 10
    for n in ("constant", "logn"):
        print(f"testing implemenation: {n}")
        for i in range(TESTS):
            arr = [random.randint(0, 100) for _ in range(ARRAY_LEN)]
            fn = lambda: (
                qs(arr[:]) if n == "logn" else qs_const(arr[:], 0, len(arr) - 1)
            )
            try:
                res = fn()
            except Exception:
                print("failed with", arr)
            did_pass = sorted(arr) == res
            if not did_pass:
                print(arr, res)

            print(
                f"{"🟢" if did_pass else "🔴"} test {i} {"passed" if did_pass else "did not pass"}"
            )


if __name__ == "__main__":
    # pass
    main()
