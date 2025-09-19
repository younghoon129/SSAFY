def is_valid_pos(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for j, k in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[j][k] == 1:
            return False
        
    for q, p in zip(range(row, -1, -1), range(col, n)):
        if board[q][p] == 1:
            return False


def n_queen(row, board):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_valid_pos(board, row, col):
            board[row][col] = 1
            n_queen(row + 1, board)
            board[row][col] = 0
 



n = 4
board = [[0]* n for _ in range(n)]
solutions = []

n_queen(0, board)

for solution in solutions:
    print(solution)