def max_idx(a):
    m_i = 0
    for i, el in enumerate(a):
        if el > a[m_i]:
            m_i = i
    return m_i


def sel_sort(a):
    sorted = []
    for _ in range(len(a)):
        m_i = max_idx(a)
        sorted.append(a.pop(m_i))
    return sorted


print(sel_sort([3, 5, 1, 2, 8]))
