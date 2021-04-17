import time

board = [[0, 4, 0, 0, 9, 0, 0, 0, 1],
         [0, 2, 0, 5, 0, 0, 0, 8, 6],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [4, 0, 0, 0, 0, 0, 8, 0, 0],
         [6, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 3, 0, 7, 8, 5, 6, 0],
         [0, 0, 0, 0, 2, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 6, 0, 5, 0],
         [0, 0, 0, 0, 3, 4, 9, 0, 8]]


def possible_column(row_index, value):
    for index in range(9):
        if board[index][row_index] == value:
            return False
    return True


def possible_row(column_index, value):
    for index in range(9):
        if board[column_index][index] == value:
            return False
    return True


def possible_box(row_index, column_index, value):
    row = (row_index // 3) * 3
    column = (column_index // 3) * 3
    for y in range(3):
        for x in range(3):
            if board[column + y][row + x] == value:
                return False
    return True


def possible(column, row, value):
    return possible_column(row, value) and possible_row(column, value) and possible_box(row, column, value)


def solve():
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print("Solution:")
    print_board()
    input("More?")


def print_board():
    output = "   "
    for y_index in range(9):
        for x_index in range(9):
            output += str(board[y_index][x_index]) + " "
        output += "\n   "
    print(output)


if __name__ == '__main__':
    print("Given board:")
    print_board()
    t0 = time.time()
    solve()
    print(f"Compiled in: {time.time() - t0}seconds")
