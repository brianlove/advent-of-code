#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='The input file')
parser.add_argument('-p', '--print', action='store_true', help='Print board displays?')

args = parser.parse_args()

with open(args.filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = lines[0].split(',')
numbers = [int(number) for number in numbers]

raw_boards = [lines[i:i+5] for i in range(2, len(lines), 6)]


def create_board(raw):
    split = [line.split() for line in raw]
    board = []
    for line in split:
        board.append([{'val': int(cell), 'marked': False} for cell in line])

    return board

def print_board(board):
    for line in board:
        for cell in line:
            print(f"{cell['val']:2} {'X' if cell['marked'] else ' '} | ", end='')
        print()



boards = [create_board(b) for b in raw_boards]

print("== The Game! ==")


def mark_number(board, number):
    for line in board:
        for cell in line:
            if cell['val'] == number:
                cell['marked'] = True
                return True
    return False

def check_bingo(board):
    vertical = [True] * 5

    for line in board:
        horizontal = True
        for ix, cell in enumerate(line):
            if not cell['marked']:
                horizontal = False
                vertical[ix] = False
        if horizontal:
            return True
    if True in vertical:
        return True
    return False

def calculate_score(board, final_number):
    sum = 0
    for line in board:
        for cell in line:
            if not cell['marked']:
                sum += cell['val']
    print(f"sum={sum}; number={final_number}; multiplied={sum*final_number}")
    return sum * final_number


game_over = False

for round, number in enumerate(numbers):
    if args.print:
        print()
        print(f"==== Round {round}:  {number} ====")
        print()

    for board_ix, board in enumerate(boards):
        was_set = mark_number(board, number)
        if args.print:
            print_board(board)

        # Only bother checking for a win if this board marked a new number
        if was_set:
            if args.print:
                print("-- number marked")
            bingo = check_bingo(board)
            if bingo:
                print(f"BINGO!  Board {board_ix}")
                game_over = True
                break

        if args.print:
            print()


    if game_over:
        print()
        print(f"== GAME OVER: round {round}")
        score = calculate_score(board, number)
        print(f"Winning board: #{board_ix}")
        print(f"    Score: {score}")
        break



## Part 2 - the worst bingo board

print()
print()
print("== Part 2 - the worst bingo board ==")

game_over = False
board_victory = [False] * len(boards)

number_won = 0

for round, number in enumerate(numbers):
    if args.print:
        print()
        print(f"==== Round {round}:  {number} ====")
        print()

    for board_ix, board in enumerate(boards):
        if board_victory[board_ix]:
            continue

        was_set = mark_number(board, number)
        if args.print:
            print_board(board)

        # Only bother checking for a win if this board marked a new number
        if was_set:
            if args.print:
                print("-- number marked")
            bingo = check_bingo(board)
            if bingo:
                number_won += 1
                board_victory[board_ix] = True

                if number_won == len(boards):
                    print(f"The final board!  {board_ix}")
                    score = calculate_score(board, number)
                    print(f"    Score: {score}")
                    game_over = True

        if args.print:
            print()

    if game_over:
        break
