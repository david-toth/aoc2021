# Alright, I'm giving in and using numpy
# for this one. Dealing with matrix-like data
# just makes sense in numpy.
import numpy as np

def check_bingo(card, numbers):
    for i in range(5):
        if all(np.isin(card[i,:], numbers)) or all(np.isin(card[:, i], numbers)):
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

#------- Part 1
def play_part1(boards, numbers):
    for i in range(4, len(numbers)):
        called = numbers[:i+1]
        for board in boards:
            if (check_bingo(board, called)):
                return board, called

winning_board, called_numbers = play_part1(boards, numbers)
win_number = called_numbers[-1]
uncalled_nums_in_board = np.isin(winning_board, called_numbers, invert=True)
print(win_number * sum(winning_board[uncalled_nums_in_board]))

#--------- Part 2
def play_part2(boards, numbers):
    for i in range(4, len(numbers)):
        called = numbers[:i+1]
        boards_ = boards
        for i, board in enumerate(boards_):
            if (check_bingo(board, called)):
                del boards_[i]
                if len(boards_) == 1:
                    return boards_[0], called

last_board, called_numbers = play_part2(boards, numbers)
win_number = called_numbers[-1]
uncalled_nums_in_board = np.isin(last_board, called_numbers, invert=True)
print(win_number * sum(last_board[uncalled_nums_in_board]))