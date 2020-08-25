import numpy as np
import sudokuSolver

print("""Enter your values separated by spaces, by rows.
Enter 0 for values you don't know.""")
entries = list(map(int, input().split()))
board = np.array(entries).reshape(9, 9)
sudokuSolver.solve(board)
print()
sudokuSolver.print_board(board)
print()