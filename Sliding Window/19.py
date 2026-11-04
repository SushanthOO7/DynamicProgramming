"""
Sliding Window:
Question 19 — Get Equal Substrings Within Budget
LeetCode #1208 — Medium
Problem Description
You're given two strings s and t of the same length, and an integer maxCost.
Changing s[i] into t[i] costs:
abs(ord(s[i]) - ord(t[i]))
Find the length of the longest contiguous substring of s that can be changed into the corresponding substring of t without exceeding maxCost.

Example 1
Input:
s = "abcd"
t = "bcdf"
maxCost = 3

Expected Output:
3
The individual conversion costs are:
s:     a  b  c  d
t:     b  c  d  f
cost:  1  1  1  2
The longest affordable window is:
[1, 1, 1]
total cost = 3
length = 3

Example 2
Input:
s = "abcd"
t = "cdef"
maxCost = 3

Expected Output:
1
Each conversion costs 2, so any two-character window would cost 4, exceeding the budget.

Target Complexity
Time: O(n)
Space: O(1)
"""
s = "abcd"
t = "bcdf"
maxCost = 3

l = 0
m = 0
tc = 0
for r in range(len(s)):
    c = abs(ord(t[r]) - ord(s[r]))
    tc += c
    while tc > maxCost:
        tc -= abs(ord(t[l]) - ord(s[l]))
        l += 1
    m = max(m, r - l + 1)
print(m)

