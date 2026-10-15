"""
Sliding Window:
Question 1 — Longest Substring Without Repeating Characters
LeetCode #3 — Medium
Problem Description
Given a string s, find the length of the longest substring that contains no repeating characters.
A substring means the characters must be continuous/adjacent in the original string.
For example:
"abcabcbb"

Valid substrings without duplicates include:
"a"
"ab"
"abc"
"bca"
"cab"

Input:
s = "abcabcbb"
Expected Output:
3
Input:
s = "bbbbb"
Expected Output:
1
Input:
s = "pwwkew"
Expected Output:
3
"""

s = "abcabcbb"
c = set()
l = 0
m = 0

for r in range(len(s)):
    while s[r] in c:
        c.remove(s[l])
        l += 1
    m = max(m, r - l + 1)
    c.add(s[r])

print(m)