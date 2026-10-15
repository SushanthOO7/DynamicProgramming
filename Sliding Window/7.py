"""
Sliding Window:
Question 7 — Longest Repeating Character Replacement
LeetCode #424 — Medium
Problem Description
You are given a string s containing uppercase English letters and an integer k.
You can replace at most k characters with any other uppercase letter.
Return the length of the longest substring that can be made to contain only one repeated character after at most k replacements.
Example 1
Input:
s = "ABAB"
k = 2
Expected Output:
4
Replace the two Bs with As:
AAAA
Example 2
Input:
s = "AABABBA"
k = 1
Expected Output:
4
For example:
"AABA"
Replace the B:
"AAAA"
Length = 4
"""
s = "AABABBA"
k = 1

a = {}
m = 0
l = 0
mm = 0

for r in range(len(s)):
    a[s[r]] = a.get(s[r], 0) + 1
    m = max(m, a[s[r]])

    while (r - l + 1) - m > k:
        a[s[l]] -= 1
        l += 1

    mm = max(m, r - l + 1)
print(mm)