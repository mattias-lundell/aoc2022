import itertools
from helpers import ints


def prep(data):
    return [[ints(c.split('-')) for c in b]
            for b in [a.split(',') for a in data.split('\n')]]


def split(data):
    return data[:len(data) // 2], data[len(data) // 2:]


def chars(start, end):
    return (chr(n) for n in range(ord(start), ord(end) + 1))


def points(c):
    return (dict(zip(chars('a', 'z'), range(1, 27))) |
            (dict(zip(chars('A', 'Z'), range(27, 53)))))[c]


def part1(data):
    print(data)
    s = 0
    for ((a0, a1), (b0, b1)) in data:
        if a0 <= b0 and a1 >= b1:
            s += 1
        elif b0 <= a0 and b1 >= a1:
            s += 1

    return s


def part2(data):
    print(data)
    s = 0
    for ((a0, a1), (b0, b1)) in data:
        if a0 >= b0 and a0 <= b1:
            s += 1
        elif a1 >= b0 and a1 <= b1:
            s += 1
        elif b0 >= a0 and b0 <= a1:
            s += 1
        elif b1 >= a0 and b1 <= a1:
            s += 1

    return s
