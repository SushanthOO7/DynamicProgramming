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

s = "pwwkew"
a = set()
l = 0
r = 1
m = 0
for i in range(len(s)):
    while s[i] in a:
        a.remove(s[l])
        l += 1
    a.add(s[i])
    m = max(m, i - l + 1)
print(m)
