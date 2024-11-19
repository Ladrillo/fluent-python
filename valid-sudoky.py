def transpose(rows):
    columns = [list(col) for col in zip(*rows)]
    return columns


def isValidSudoku(board):
    rows = board
    columns = [list(cols) for cols in zip(*board)]
    submatrixes = []
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            submatrixes.append(getSubmatrix(rows, x, y, 3))
    return submatrixes[8]


def getSubmatrix(matrix, x, y, size):
    return [row[x:x+size] for row in matrix[y:y+size]]


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

test_transposed = transpose(test_board)

test_submatrix = isValidSudoku(test_board)

for row in test_board:
    print(row)

print("\n")

for row in test_submatrix:
    print(row)
