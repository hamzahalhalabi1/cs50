"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_X = sum(row.count(X) for row in board)
    num_O = sum(row.count(O) for row in board)
    return X if num_X == num_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    player_mark = player(board)
    new_board = [row[:] for row in board]
    new_board[i][j] = player_mark
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    lines = (board +  # rows
        list(zip(*board)) +  # columns
        [[board[i][i] for i in range(3)],  # main diagonal
        [board[i][2 - i] for i in range(3)]])  # secondary diagonal
    for line in lines:
        if line.count(X) == 3:
            return X
        elif line.count(O) == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell != EMPTY for cell in row) for row in board)
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

    best_move = None
    if player(board) == X:
        max_utility = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for action in actions(board):
            value = min_value(result(board, action), alpha, beta)
            if value > max_utility:
                max_utility = value
                best_move = action
            alpha = max(alpha, value)
    else:
        min_utility = float('inf')
        alpha = float('-inf')
        beta = float('inf')
        for action in actions(board):
            value = max_value(result(board, action), alpha, beta)
            if value < min_utility:
                min_utility = value
                best_move = action
            beta = min(beta, value)
    return best_move