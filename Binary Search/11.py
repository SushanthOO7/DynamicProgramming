"""
Binary Search
Question 11 — Successful Pairs of Spells and Potions
LeetCode #2300 — Medium
Problem Description
You are given two arrays:
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
and an integer:
success = 7
A spell and potion form a successful pair if:
spell × potion >= success
For each spell, return the number of potions that can form a successful pair with it.

Example 1
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7

Expected Output:
[4, 0, 3]
Why?
For spell 5:
5 × 1 = 5   ❌
5 × 2 = 10  ✅
5 × 3 = 15  ✅
5 × 4 = 20  ✅
5 × 5 = 25  ✅

4 successful potions

For spell 1:
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
1 × 4 = 4
1 × 5 = 5

0 successful potions

For spell 3:
3 × 1 = 3   ❌
3 × 2 = 6   ❌
3 × 3 = 9   ✅
3 × 4 = 12  ✅
3 × 5 = 15  ✅

3 successful potions
Therefore:
[4, 0, 3]

Example 2
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16

Expected Output:
[2, 0, 2]

Target Complexity
If:
n = number of spells
m = number of potions
aim for:
O(m log m + n log m)
"""
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16

potions.sort()
res = []
for s in spells:
    l = 0
    r = len(potions) - 1
    while l <= r:
        m = (l + r) // 2
        pair = s * potions[m]
        if pair >= success:
            r = m - 1
        else:
            l = m + 1
    res.append(len(potions) - l)
print(res)

