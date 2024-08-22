import random


def qs_const(arr, lo, high, shld_print=False):
    if lo >= high:
        return

    piv = arr[lo]
    new_lo = lo + 1
    for i in range(new_lo, high + 1):
        if arr[i] < piv:
            arr[new_lo], arr[i] = arr[i], arr[new_lo]
            new_lo += 1

    if shld_print:
        print(arr)

    arr[lo], arr[new_lo - 1] = arr[new_lo - 1], arr[lo]

    if shld_print:
        print(arr)

    qs_const(arr, lo, new_lo - 1)
    qs_const(arr, new_lo, high)

    return arr


print(qs_const([4, 49, 1, 40, 68], 0, 4, True))
print(qs_const([53, 85, 45, 86, 47], 0, 4, True))
print(qs_const([14, 69, 84, 6, 84], 0, 4, True))
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

    # there is no cool operator trick you can do here like in lisp right?
    lower, equal, upper = (
        [v for v in arr if v < piv],
        [v for v in arr if v == piv],
        [v for v in arr if v > piv],
    )
    return qs(lower) + equal + qs(upper)


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
