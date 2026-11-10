"""
Hash Map
Question 14 — Longest Substring Without Repeating Characters
LeetCode #3 — Medium ⭐ Very common interview problem
Problem Description
Given a string s, return the length of the longest substring without repeating characters.
Remember: a substring must be contiguous.

Example 1
Input:
s = "abcabcbb"

Expected Output:
3
Because "abc" has no repeated characters.

Example 2
Input:
s = "bbbbb"

Expected Output:
1

Example 3
Input:
s = "pwwkew"

Expected Output:
3
One longest valid substring is "wke".

Target Complexity
Time: O(n)
Space: O(n)
"""

s = "pwwkew"

d = {}
l = 0
m = 0
for r in range(len(s)):
    d[s[r]] = d.get(s[r], 0) + 1
    while d[s[r]] > 1:
        w = s[l]
        d[w] -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)