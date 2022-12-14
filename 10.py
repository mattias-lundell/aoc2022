import itertools
from helpers import ints


def prep(data):
    print(data)
    return data.split('\n')


def transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def split(data):
    return data[:len(data) // 2], data[len(data) // 2:]


def chars(start, end):
    return (chr(n) for n in range(ord(start), ord(end) + 1))


def points(c):
    return (dict(zip(chars('a', 'z'), range(1, 27))) |
            (dict(zip(chars('A', 'Z'), range(27, 53)))))[c]


def part1(data):
    x = 1
    tape = [1]
    pos = 0
    for row in data:
        if row == 'noop':
            tape.append(x)
            pos += 1
            print('nop', pos, x)
            continue

        op, val = row.split(' ')
        if op == 'addx':
            pos += 1
            print('pre', pos, x)
            tape.append(x)
            x += int(val)
            tape.append(x)
            pos += 1
            print('inc', pos, x)

    print(tape)
    print(tape[19], tape[59], tape[99], tape[139], tape[179], tape[219])

    return 20 * tape[19] + 60 * tape[59] + 100 * tape[99] + 140 * tape[
        139] + 180 * tape[179] + 220 * tape[219]


def points(v, vals):
    s = 0
    for x in vals:
        s += 1
        if x >= v:
            break
    return s


def part2(data):
    x = 1
    tape = [1]
    pos = 0
    for row in data:
        if row == 'noop':
            tape.append(x)
            pos += 1
            print('nop', pos, x)
            continue

        op, val = row.split(' ')
        if op == 'addx':
            pos += 1
            print('pre', pos, x)
            tape.append(x)
            x += int(val)
            tape.append(x)
            pos += 1
            print('inc', pos, x)

    s = ""

    for i, x in enumerate(tape, 1):
        pos = i - 1
        if x - 1 <= pos % 40 <= x + 1:
            s += "#"
        else:
            s += "."
        if len(s) == 40:
            print(s)
            s = ""

    print(s)

    return 0
