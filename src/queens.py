def solve_n_queens(n: int):
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            conflict = False
            for i in range(row):
                if board[i] == col or abs(i - row) == abs(board[i] - col):
                    conflict = True
                    break
            if not conflict:
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions