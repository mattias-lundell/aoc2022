import itertools
from helpers import ints
from collections import defaultdict
from functools import cache


def prep(data):
    return data.split('\n')


def part1(data):
    curr = []

    tree = defaultdict(list)

    for cmd in data:
        if '$ cd' in cmd:
            if '..' in cmd:
                curr.pop()
                continue
            if '/' in cmd:
                curr = []
                continue
            ls = False
            (_, _, d) = cmd.split(' ')
            curr.append(d)
            continue
        elif '$ ls' in cmd:
            ls = True
            continue
        else:
            (a, b) = cmd.split(' ')
            if a == 'dir':
                tree['/'.join(curr)].append((None, '/'.join(curr + [b])))
                continue
            else:
                tree['/'.join(curr)].append((int(a), b))

        print(cmd)

    print(tree)

    _tree = [(a, b) for (a, b) in tree.items()]
    _tree.sort(key=lambda x: sum((1 for (a, _) in x[1] if a is None)))
    tree = dict(_tree)
    print(tree)

    cache = {}

    s = 0
    for d in tree:
        print(cache, d, tree[d])
        _size = size(d, tree, cache)
        if _size < 100000:
            s += _size

    print(cache)

    return s


def size(d, tree, cache):
    s = 0
    for (a, b) in tree[d]:
        if a is None:
            #print(b, cache)
            if b in cache:
                s += cache[b]
            else:
                print()
                print(b)
                print()
                _size = size(b, tree, cache)
                cache[b] = _size
                s += _size
        else:
            s += a
    cache[d] = s
    return s


def part2(data):
    curr = []

    tree = defaultdict(list)

    for cmd in data:
        if '$ cd' in cmd:
            if '..' in cmd:
                curr.pop()
                continue
            if '/' in cmd:
                curr = []
                continue
            ls = False
            (_, _, d) = cmd.split(' ')
            curr.append(d)
            continue
        elif '$ ls' in cmd:
            ls = True
            continue
        else:
            (a, b) = cmd.split(' ')
            if a == 'dir':
                tree['/'.join(curr)].append((None, '/'.join(curr + [b])))
                continue
            else:
                tree['/'.join(curr)].append((int(a), b))

        print(cmd)

    print(tree)

    _tree = [(a, b) for (a, b) in tree.items()]
    _tree.sort(key=lambda x: sum((1 for (a, _) in x[1] if a is None)))
    tree = dict(_tree)
    print(tree)

    cache = {}

    s = 0
    for d in tree:
        print(cache, d, tree[d])
        _size = size(d, tree, cache)
        if _size < 100000:
            s += _size

    print(cache)

    tot = max(cache.values())
    potentials = []
    for a, b in cache.items():
        print(70000000 - b, b)
        if 70000000 - tot + b >= 30000000:
            potentials.append(b)

    print(potentials)
    return min(potentials)
