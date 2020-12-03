from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] != "-":
            return f"{board[0][0]} wins!"
    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] != "-":
            return f"{board[2][0]} wins!"
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] != "-":
            return f"{board[0][0]} wins!"
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] != "-":
            return f"{board[0][2]} wins!"
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] != "-":
            return f"{board[0][1]} wins!"
    if board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] != "-":
            return f"{board[1][0]} wins!"
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != "-":
            return f"{board[0][0]} wins!"
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != "-":
            return f"{board[2][0]} wins!"
    return "unfinished"
