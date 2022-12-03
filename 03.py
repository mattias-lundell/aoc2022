import itertools


def prep(data):
    return [a for a in data.split('\n')]


def split(data):
    return data[:len(data) // 2], data[len(data) // 2:]


def chars(start, end):
    return (chr(n) for n in range(ord(start), ord(end) + 1))


def points(c):
    return (dict(zip(chars('a', 'z'), range(1, 27))) |
            (dict(zip(chars('A', 'Z'), range(27, 53)))))[c]


def part1(data):
    s = 0
    for d in data:
        a, b = split(d)
        i = list(set(a).intersection(set(b)))
        s += points(i[0])

    return s


def part2(data):
    s = 0
    for (a, b, c) in zip(data[0::3], data[1::3], data[2::3]):
        d = points(list((set(a).intersection(set(b)).intersection(set(c))))[0])
        print(d)
        s += d
        # return d
        # a, b = split(d)
        # i = list(set(a).intersection(set(b)))
        # s += points(i[0])

    return s
