import itertools


def prep(data):
    return [a.split() for a in data.split('\n')]


def part1(data):
    print(data)
    for (x, y) in data:
        print(x, y, win(x, y), points(y, win(x, y)))

    return sum(points(y, win(x, y)) for (x, y) in data)


#return max([sum([int(b) for b in a.split()]) for a in data.split('\n\n')])
def points(my_hand, outcome):
    return {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'A': 1,
        'B': 2,
        'C': 3
    }[my_hand] + {
        'L': 0,
        'D': 3,
        'W': 6
    }[outcome]


def t(hand):
    return {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}[hand]


def win(your_hand, my_hand):
    return {
        'X': {
            'A': 'D',
            'B': 'L',
            'C': 'W'
        },
        'Y': {
            'A': 'W',
            'B': 'D',
            'C': 'L'
        },
        'Z': {
            'A': 'L',
            'B': 'W',
            'C': 'D'
        }
    }[my_hand][your_hand]


def win2(your_hand, my_hand):
    return {
        'R': {
            'X': ('L', 'S'),
            'Y': ('D', 'R'),
            'Z': ('W', 'P'),
        },
        'P': {
            'X': ('L', 'R'),
            'Y': ('D', 'P'),
            'Z': ('W', 'S'),
        },
        'S': {
            'X': ('L', 'P'),
            'Y': ('D', 'S'),
            'Z': ('W', 'R'),
        }
    }[your_hand][my_hand]


#return max([sum([int(b) for b in a.split()]) for a in data.split('\n\n')])
def points2(outcome, my_hand):
    return {
        'R': 1,
        'P': 2,
        'S': 3,
    }[my_hand] + {
        'L': 0,
        'D': 3,
        'W': 6
    }[outcome]


def part2(data):
    print(data)
    for (x, y) in data:
        print(x, y, win2(t(x), y), points2(*win2(t(x), y)))

    return sum(points2(*win2(t(x), y)) for (x, y) in data)
    #return sum(points(y, win(x, y)) for (x, y) in data)
