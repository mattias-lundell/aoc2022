import itertools
from helpers import ints


def prep(data):
    print(data)
    rows = data.split('\n')
    cols = transpose(rows)
    rows = transpose(cols)

    print(rows)
    print(cols)

    return (rows, cols)


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
    c = 0
    rows, cols = data
    for i in range(1, len(rows) - 1):
        for j in range(1, len(cols) - 1):
            row_before = rows[i][:j]
            row_after = rows[i][j + 1:]
            col_before = cols[j][:i]
            col_after = cols[j][i + 1:]

            _m = [
                max(row_before),
                max(row_after),
                max(col_before),
                max(col_after)
            ]

            if any([x < rows[i][j] for x in _m]):
                print('visible', i, j, rows[i][j])
                c += 1

    #        print(row_before, rows[i][j], row_after)
    #        print(col_before, rows[i][j], col_after)
    #    print()

    return 2 * len(rows) + 2 * len(cols) + c - 4


def points(v, vals):
    s = 0
    for x in vals:
        s += 1
        if x >= v:
            break
    return s


def part2(data):
    c = 0
    scores = []
    rows, cols = data
    for i in range(1, len(rows) - 1):
        for j in range(1, len(cols) - 1):
            v = rows[i][j]

            row_before = list(reversed(rows[i][:j]))
            row_after = rows[i][j + 1:]
            col_before = list(reversed(cols[j][:i]))
            col_after = cols[j][i + 1:]

            scores.append(
                points(v, row_before) * points(v, row_after) *
                points(v, col_before) * points(v, col_after))

            # if any([x < v for x in _m]):
            #     print('visible', i, j, v)
            #     c += 1

    #        print(row_before, rows[i][j], row_after)
    #        print(col_before, rows[i][j], col_after)
    #    print()


#    print(scores)
    return max(scores)
