"""
Sliding Window:
Question 9 — Find All Anagrams in a String
LeetCode #438 — Medium

This is a great follow-up to Question 8 because it uses almost the same fixed-size sliding-window pattern, but now you need to find all matching windows.
Problem Description
Given two strings s and p, return the starting indices of all substrings in s that are anagrams of p.

An anagram contains exactly the same characters with the same frequencies, but the order can be different.
Example 1
Input:
s = "cbaebabacd"
p = "abc"
Expected Output:
[0, 6]
Why?
At index 0:
cbaebabacd
^^^
cba
"cba" is an anagram of "abc".
At index 6:
cbaebabacd
      ^^^
      bac
"bac" is also an anagram of "abc".
Example 2
Input:
s = "abab"
p = "ab"
Expected Output:
[0, 1, 2]
Because all three windows are anagrams:
"ab" → index 0
"ba" → index 1
"ab" → index 2

"""
s = "cbaebabacd"
p = "abc"

n = len(p)
c = {}
w = {}
res = []
for i in p:
    c[i] = c.get(i, 0) + 1
for j in range(n):
    w[s[j]] = w.get(s[j], 0) + 1
if c == w:
    res.append(0)
for r in range(n, len(s)):
    w[s[r]] = w.get(s[r], 0) + 1
    o = s[r - n]
    w[o] -= 1
    if w[o] == 0:
        del w[o]
    if c == w:
        res.append(r - n + 1)
print(res)