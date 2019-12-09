A = [5, 2, 4, 6, 1, 3, 2, 6]
p = 1
q = len(A)


def slow_rec(data, i, j):
    if i < j:
        m = (i + j) // 2
        slow_rec(data, i, m)
        slow_rec(data, m + 1, j)
        if data[m] > data[j]:
            data[m], data[j] = data[j], data[m]
        slow_rec(data, i, j - 1)
        return data
    if i >= j:
        return data


def slow(data):
    return slow_rec(data, 0, len(data) - 1)


print(slow(A))
