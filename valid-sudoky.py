import re


def getSubmatrix(matrix, x, y, size):
    return [row[x:x+size] for row in matrix[y:y+size]]


def flattenMatrix(matrix):
    return [item for row in matrix for item in row]


def validator(items):
    no_dots = [char for char in items if char != "."]
    items_valid_nums = all(
        bool(re.fullmatch(r'[1-9]', char)) for char in no_dots)
    items_distinct = len(no_dots) == len(set(no_dots))
    return items_distinct and items_valid_nums


def isValidSudoku(board):
    rows = board
    columns = [list(cols) for cols in zip(*board)]
    submatrixes = []
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            submatrixes.append(getSubmatrix(rows, x, y, 3))
    flattened_submatrixes = [flattenMatrix(matrix) for matrix in submatrixes]
    lines_to_check = [*rows, *columns, *flattened_submatrixes]
    return all(validator(line) for line in lines_to_check)

test_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(isValidSudoku(test_board))
