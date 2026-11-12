"""
Question 18 — Valid Sudoku
LeetCode #36 — Medium ⭐ Common interview hash-set problem
Problem Description
You are given a 9 × 9 Sudoku board.
Determine whether the board is currently valid.
A valid Sudoku must satisfy:
1. Each row contains digits 1–9 without duplicates.
2. Each column contains digits 1–9 without duplicates.
3. Each 3×3 box contains digits 1–9 without duplicates.
4. "." represents an empty cell and should be ignored.
You do not need to determine whether the puzzle is solvable.

Example
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]


Expected Output:
True

Target Complexity
A Sudoku board is always 9×9, so technically it's constant-sized. More generally for an N×N board:

Time: O(N²)
Space: O(N²)
"""

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

flag = True
rows = [set() for i in range(9)]
col = [set() for i in range(9)]
box = [set() for i in range(9)]

for r in range(9):
    for c in range(9):
        v = board[r][c]
        if v == ".":
            continue
        box_n = (r // 3) * 3 + (c // 3)
        if v in rows[r] or v in col[c] or v in box[box_n]:
            flag = False
            break
        rows[r].add(v)
        col[c].add(v)
        box[box_n].add(v)
print(flag)
