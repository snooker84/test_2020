import random


def gen_tuples(tuple_length):
    a = []
    b = []
    for i in range(tuple_length):
        a += [random.randint(0, 5)]
        b += [random.randint(-5, 0)]
    a = tuple(a)
    b = tuple(b)
    return a, b


def num_counter_in_tuple(c: tuple, value):
    count = c.count(value)
    return count


a1, b1 = gen_tuples(10)
c1 = a1 + b1
print(c1)
print(num_counter_in_tuple(c1, 2))
