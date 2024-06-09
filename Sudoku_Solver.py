def printMatrix(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def isPossible(board, x, y, value):
    # Same row checking 
    for col in range(9):
        if board[x][col] == value:
            return False
 
    # Same col checking
    for row in range(9):
        if board[row][y] == value:
            return False
 
    # Same 3 * 3 matrix checking 
    topRow = (x // 3) * 3 
    topCol = (y // 3) * 3 
 
    for i in range(3):
        for j in range(3):
            if board[topRow + i][topCol + j] == value:
                return False
    return True

def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for value in range(1, 10):
                    if isPossible(board, i, j, str(value)):
                        board[i][j] = str(value)
                        if solveSudoku(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

if solveSudoku(board):
    print("Sudoku solved:")
    printMatrix(board)
else:
    print("No solution exists.")
