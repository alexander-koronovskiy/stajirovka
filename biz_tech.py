def merge(data, p, q, r):
    if data[q] > data[r]:
        data[q], data[r] = data[r], data[q]
    slow_rec(data, p, r - 1)
    return data


def slow_rec(A, p, r):
    if p < r:
        q = (p + r) // 2
        slow_rec(A, p, q)
        slow_rec(A, q + 1, r)
        merge(A, p, q, r)
    return A


def slow(data):
    return slow_rec(data, 0, len(data) - 1)


A = [5, 2, 4, 6, 1, 3, 2, 6]
print(slow(A))
