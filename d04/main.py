# Alright, I'm giving in and using numpy
# for this one. Dealing with matrix-like data
# just makes sense in numpy.
import numpy as np


def check_bingo(card, numbers):
    for i in range(5):
        if (all(np.isin(card[i, :], numbers)) or
                all(np.isin(card[:, i], numbers))):
            return True
    return False


file = open("input.txt", "r")
lines = file.readlines()
file.close()

numbers = list(map(int, lines[0].strip().split(",")))
boards = []
matrix = []

for line in lines[2:]:
    if line == "\n":
        boards.append(np.array(matrix))
        matrix = []
    else:
        line = [i for i in line.strip().split(" ") if i.isnumeric()]
        matrix.append(list(map(int, line)))


def play_part1(boards, numbers):
    for i in range(4, len(numbers)):
        called = numbers[:i+1]
        for board in boards:
            if (check_bingo(board, called)):
                return board, called


winning_board, called_numbers = play_part1(boards, numbers)
last_number = called_numbers[-1]
uncalled_nums_in_board = np.isin(winning_board, called_numbers, invert=True)
print(last_number * sum(winning_board[uncalled_nums_in_board]))


def play_part2(boards, numbers):
    for i in range(4, len(numbers)):
        called = numbers[:i+1]
        for i, board in enumerate(boards):
            if (check_bingo(board, called)):
                del boards[i]
                if len(boards) == 1:
                    return boards[0], called


last_board, called_numbers = play_part2(boards, numbers)
last_number = called_numbers[-1]
uncalled_nums_in_board = np.isin(last_board, called_numbers, invert=True)
print(last_number * sum(last_board[uncalled_nums_in_board]))
