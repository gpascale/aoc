import numpy as np
import re


def transpose(arr):
    return [''.join(s) for s in zip(*arr)]


def simulate(B):
    for row in range(len(B)):
        for match in re.finditer(r"(?<=#)([.O]+)(?=#)", '#' + B[row] + '#'):
            start = match.span()[0] - 1
            l = match.span()[1] - match.span()[0]
            num_rocks = len(match[0].replace('.', ''))
            repl = ('O' * num_rocks) + ('.' * (l - num_rocks))
            B[row] = B[row][:start] + repl + B[row][start + l:]
    return B


def solve(board):
    ret = 0
    board = transpose(board)
    for row in range(len(board)):
        for match in re.finditer(r"(?<=#)([.O]+)(?=#)", '#' + board[row] + '#'):
            start = match.span()[0] - 1
            num_rocks = len(match[0].replace('.', ''))
            for j in range(start, start + num_rocks):
                ret += len(board) - j
    return ret


def print_board(board):
    for row in board:
        print(row)


def score(board):
    ret = 0
    for i in range(len(board)):
        num_rocks = len(board[i].replace('.', '').replace('#', ''))
        ret += num_rocks * (len(board) - i)
    return ret


def solve2(L):
    board = L.copy()
    scores = []
    for i in range(1000):
        # north
        board = transpose(board)
        board = simulate(board)
        board = transpose(board)

        # west
        board = simulate(board)

        # south
        board = transpose(board)
        board = [s[::-1] for s in board]
        board = simulate(board)
        board = [s[::-1] for s in board]
        board = transpose(board)

        # east
        board = [s[::-1] for s in board]
        board = simulate(board)
        board = [s[::-1] for s in board]

        scores.append(score(board))

    cycle_len = -1
    for c in range(4, 499, 1):
        if scores[999-c:999] == scores[999-2*c:999-c]:
            cycle_len = c
            break
    print(cycle_len)

    mod = 1000000000 % cycle_len
    for i in range(1000, 0, -1):
        if i % cycle_len == mod:
            return scores[i - 1]


# L = [s.strip() for s in open("./example.txt").readlines() if s]
L = [s.strip() for s in open("./input.txt").readlines() if s]

print('part 1:', solve(L.copy()))
print('part 2:', solve2(L.copy()))
