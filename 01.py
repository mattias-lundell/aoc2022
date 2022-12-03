import itertools


def prep(data):
    return data


def part1(data):
    return max([sum([int(b) for b in a.split()]) for a in data.split('\n\n')])


def part2(data):
    return (sum(
        sorted([sum([int(b) for b in a.split()])
                for a in data.split('\n\n')])[-3:]))
