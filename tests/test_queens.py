import sys
sys.path.append(".")
from src.queens import solve_n_queens

print("4 皇后解数：", len(solve_n_queens(4)))
print("8 皇后解数：", len(solve_n_queens(8)))