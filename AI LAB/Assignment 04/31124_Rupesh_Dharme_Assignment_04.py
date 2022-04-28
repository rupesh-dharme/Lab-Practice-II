# Rupesh Dharme
# LP II Lab
# Assignment 04
# N-Queens Problem

N = 0

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQueens(board, col = 0):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col+1):
                return True
            board[i][col] = 0
    return False

def displayBoard(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

def main():
    global N 
    N = int(input("Enter n: "))
    board = [[0 for i in range(N)] for j in range(N)]
    if not solveNQueens(board):
        print("No solution exists.")
    else:
        displayBoard(board)

if __name__ == "__main__":
    main()