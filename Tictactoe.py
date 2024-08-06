def did_I_win(player, board):
    # Check rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Example usage
board1 = [
    ['X', 'O', 'X'],
    ['X', 'X', 'O'],
    ['X', 'O', 'X']
]

board2 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]

board3 = [
    ['O', 'O', 'O'],
    ['X', 'X', 'O'],
    ['X', 'O', 'X']
]

print(did_I_win('X', board1))  # True (column win)
print(did_I_win('O', board1))  # False
print(did_I_win('X', board2))  # True (diagonal win)
print(did_I_win('O', board2))  # False
print(did_I_win('O', board3))  # True (row win)
print(did_I_win('X', board3))  # False
