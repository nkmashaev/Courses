from typing import List


def tic_tac_toe_checker(board: List[List], win_seq_size: int = 3) -> str:
    link_numb = win_seq_size - 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "-":
                continue
            # column check
            if check(board, i, j, 1, 0, link_numb):
                return f"{board[i][j]} wins!"
            # row check
            if check(board, i, j, 0, 1, link_numb):
                return f"{board[i][j]} wins!"
            # diag1 check
            if check(board, i, j, 1, 1, link_numb):
                return f"{board[i][j]} wins!"
            # diag2 check
            if check(board, i, j, 1, -1, link_numb):
                return f"{board[i][j]} wins!"
    return "unfinished"


def check(board: List[List], i: int, j: int, si: int, sj: int, fuel: int) -> bool:
    if not fuel:
        return True
    new_i = i + si
    new_j = j + sj
    if not (0 <= new_i < len(board)):
        return False
    if not (0 <= new_j < len(board[i])):
        return False
    if board[i][j] == board[new_i][new_j]:
        return check(board, i + si, j + sj, si, sj, fuel - 1)
    else:
        return False
