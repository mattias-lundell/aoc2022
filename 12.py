import itertools
from helpers import ints
from collections import defaultdict
import re


def prep(data):
    r = "Monkey\ (\d+):\n  Starting items: (.+)\n  Operation: new = old ([*|+]) (.+)\n  Test: divisible by (.+)\n    If true: throw to monkey (.+)\n    If false: throw to monkey (.+)"

    return re.findall(r, data)


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
    monkeys = defaultdict(list)
    ops = {}
    tests = {}

    for (i, items, op, val, test, true, false) in data:
        monkeys[i] = items.split(', ')
        if op == '+':
            if val == 'old':
                ops[i] = lambda x: x + x
            else:
                ops[i] = lambda x: x + int(val)
        if op == '*':
            if val == 'old':
                ops[i] = lambda x: x + x
            else:
                ops[i] = lambda x: x + int(val)

        tests[i] = lambda x, test, true, false
        print(data)


def t(x, test, true, false):
    if x / int(test) == 0:
        return true
    return false    

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
