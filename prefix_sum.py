a = [5, 10, 30, 4, 5]

prefix_sum = [0]
for i, n in enumerate(a):
    prefix_sum.append(prefix_sum[-1] + n)

print(prefix_sum)


def get_sum(i, j):
    return prefix_sum[j + 1] - prefix_sum[i]


print(get_sum(1, 2))


def subarray_sum(nums, k):
    prefix_sums = {0: 1}
    count = 0
    curr = 0

    for num in nums:
        curr += num
        print(curr, "curr is")
        if curr - k in prefix_sums:
            count += prefix_sums[curr - k]
        prefix_sums[curr] = prefix_sums.get(curr, 0) + 1

    print(prefix_sums)
    return count


print(
    subarray_sum(
        [
            1,
            1,
            1,
        ],
        2,
    )
)

a = [1, 2, 4, 6]

prefix = [0] * len(a)
prefix[0] = 1
for i in range(1, len(a)):
    prefix[i] = prefix[i - 1] * a[i - 1]
print(prefix)
