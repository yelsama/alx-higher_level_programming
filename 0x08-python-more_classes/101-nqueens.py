#!/usr/bin/python3
"""define a queens"""
import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col:
            return False

    """Check if there is a queen in the same diagonal
    (top-left to bottom-right)"""
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    """"Check if there is a queen in the same diagonal
    (top-right to bottom-left)"""
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    if row == len(board):
        solutions.append(board[:])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1


def print_solutions(solutions):
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)
