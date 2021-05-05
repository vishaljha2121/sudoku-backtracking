def print_board(board):
    boardString = ""
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and (j + 1) != 9:
                boardString += "| "
            if j == 8:
                boardString += "\n"
            if j == 8 and (i + 1) % 3 == 0 and (i + 1) != 9:
                boardString += "- - - - - - - - - - - - -  \n"
    print(boardString)


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j


def valid_cell(board, pos, num):
    for i in range(9):
        if board[i][pos[1]] == num and (i, pos[1]) != pos:
            return False
    for j in range(9):
        if board[pos[0]][j] == num and (pos[0], j) != pos:
            return False

    start_i = pos[0] - pos[0] % 3
    start_j = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):
            if (
                board[start_i + i][start_j + j] == num
                and (start_i + i, start_j + j) != pos
            ):
                return False
    return True


def solve(board):
    empty = find_empty_cell(board)
    if not empty:
        return True  # Board solved

    for nums in range(9):
        if valid_cell(board, empty, nums + 1):
            board[empty[0]][empty[1]] = nums + 1

            if solve(board):
                return True
            board[empty[0]][empty[1]] = 0
    return False


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]
    print_board(board)
    solve(board)
    print_board(board)