# Tic-Tac-Toe AI using Minimax
![alt text](game.png)

## Introduction
This project implements an AI player using the Minimax algorithm to play Tic-Tac-Toe optimally. The AI is implemented in Python and provides a graphical interface to play against it.

## Files
- **runner.py**: Contains the code to run the graphical interface for the game. You can run `python runner.py` to play against the AI.
- **tictactoe.py**: Contains all the logic for playing the game and making optimal moves. You need to complete the implementations of certain functions in this file.

## Understanding
In `tictactoe.py`, we define three variables: `X`, `O`, and `EMPTY`, to represent possible moves of the board.

The `initial_state` function returns the starting state of the board as a list of three lists, where each internal list contains three values that are either `X`, `O`, or `EMPTY`.

## Specification
Complete the implementations of the following functions in `tictactoe.py`:
1. `player(board)`: Determine which player's turn it is.
2. `actions(board)`: Return a set of all possible actions.
3. `result(board, action)`: Return the new board state after applying the action.
4. `winner(board)`: Determine the winner of the game.
5. `terminal(board)`: Check if the game is over.
6. `utility(board)`: Calculate the utility value of the terminal board.
7. `minimax(board)`: Determine the optimal move for the player using Minimax algorithm.

## Hints
- You can test your functions in a separate Python file by importing them.
- You can add additional helper functions to `tictactoe.py` as long as their names don't collide with existing ones.

## Note
Since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI if you play optimally as well. Enjoy playing!