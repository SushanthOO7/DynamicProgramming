"""
Hash Map
Question 17 — Brick Wall
LeetCode #554 — Medium
Problem Description
You have a rectangular brick wall. Each row contains bricks of different widths, but every row has the same total width.
You need to draw one vertical line from top to bottom.
The goal is to cross the minimum number of bricks.
If your line passes exactly through the gap between two bricks, that brick is not crossed.
You cannot draw the line along the far left or far right edge of the wall.

Example
Input:
wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]]

Expected Output:
2
How to think about the wall
Take the first row:
[1, 2, 2, 1]
The brick boundaries occur after cumulative widths:
1
1 + 2 = 3
1 + 2 + 2 = 5
So its internal gaps are at:
1, 3, 5
We do not count the final boundary at 6, because that's the right edge of the entire wall.
Another row:
[3, 1, 2]
has internal gaps:
3, 4
Now imagine counting:
gap position → number of rows having a gap there
If a position has a gap in 4 out of 6 rows, drawing the line there crosses only:
6 - 4 = 2 bricks.
Target Complexity
If the total number of bricks across the wall is B:
Time: O(B)
Space: O(B)
"""

wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]]

d = {}
total_r = len(wall)
m = 0
for r in wall:
    s = 0
    for b in range(len(r) - 1):
        s += r[b]
        d[s] = d.get(s, 0) + 1
for i in d:
    m = max(m, d[i])
print(total_r - m)