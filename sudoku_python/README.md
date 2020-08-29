# Sudoku Solver

## Note:
The sudoku solver code was based on the tutorial series by [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg):
  * [Part 1](https://youtu.be/eqUwSA0xI-s)
  * [Part 2](https://youtu.be/lK4N8E6uNr4)

I added the ability to use the script on the command line using the Click library.

## How to use:
On the command line enter:
  * python cli_solver.py
  
It will then prompt you to enter the sudoku puzzle. Enter it starting from the upper left corner, with spaces between numbers.
Enter 0 for values you want to solve for.

For example, using the first three grids:

```
0 0 0 | 2 6 0 | 7 0 1
6 8 0 | 0 7 0 | 0 9 0
1 9 0 | 0 0 4 | 5 0 0
- - - - - - - - - - -  and so on...
```
You would enter:

0 0 0 2 6 0 7 0 1 6 8 0 0 7 0 0 9 0 1 9 0 0 0 4 5 0 0 ...
