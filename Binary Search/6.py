"""
Binary Search
LeetCode #74 — Medium ⭐
Problem Description
You are given an m × n matrix where:
- Each row is sorted from left to right.
- The first element of each row is greater than the last element of the previous row.
For example:
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]]
target = 3

Return:
True because 3 exists.

Example 2
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]]
target = 13

Expected:
False

Target Complexity
Time: O(log(m × n))
Space: O(1)
"""

matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]]
target = 3

rows = len(matrix)
cols = len(matrix[0])
l = 0
r = (rows * cols) - 1
flag = False
while l <= r:
    m = (l + r) // 2
    row = m // cols
    col = m % cols
    if target == matrix[row][col]:
        flag = True
        break
    elif target > matrix[row][col]:
        l = m + 1
    else:
        r = m - 1
print(flag)