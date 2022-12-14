import itertools
from helpers import ints


def prep(data):
    return data


def split(data):
    return data[:len(data) // 2], data[len(data) // 2:]


def chars(start, end):
    return (chr(n) for n in range(ord(start), ord(end) + 1))


def points(c):
    return (dict(zip(chars('a', 'z'), range(1, 27))) |
            (dict(zip(chars('A', 'Z'), range(27, 53)))))[c]


def part1(data):
    print(data)
    for i in range(len(data) - 3):
        if len(set(data[i:i + 4])) == 4:
            print(data[i:i + 4])
            return i + 4


def part2(data):
    print(data)
    for i in range(len(data) - 13):
        if len(set(data[i:i + 14])) == 14:
            print(data[i:i + 14])
            return i + 14
