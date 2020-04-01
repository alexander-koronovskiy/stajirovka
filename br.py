from pythonds.basic.stack import Stack


def min_o_n(test_list):
    mn = test_list[0]
    for i in test_list:
        if mn > i:
            mn = i
    return mn


def num_to_base_s(num, base = 8):
    t_l = Stack()
    bin_s = ''
    num1 = num

    while num1 > 0:
        t_l.push(num1 % base)
        num1 = num1 // base
    while not t_l.isEmpty():
        bin_s += str(t_l.pop())
    return bin_s


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n - 1)


test_list = [39, 11, 17, 41, 22, 59, 88, 34, 11, 88, 16]
print('defragmentation', num_to_base_s(664, 8))
print('minimum search', min_o_n(test_list))
print('fact 5:', fact(5))
