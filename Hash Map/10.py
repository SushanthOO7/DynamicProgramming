"""
Hash Map
Question 10 — First Unique Character in a String
LeetCode #387 — Easy
Problem Description
Given a string s, find the index of the first non-repeating character.
A non-repeating character appears exactly once.
If there is no such character, return -1.

Example 1
Input:
s = "leetcode"

Expected Output:
0
Because "l" appears exactly once and is the first unique character.

Example 2
Input:
s = "loveleetcode"

Expected Output:
2
Because the character at index 2 is "v":
l o v e l e e t c o d e
    ↑
  index 2
and "v" appears only once.

Example 3
Input:
s = "aabb"

Expected Output:
-1
Every character repeats.

Target Complexity
Time: O(n)
Space: O(1) for lowercase English letters.
"""

s = "leetcode"

d = {}
r = -1
for i in s:
    d[i] = d.get(i, 0) + 1
for i in range(len(s)):
    if d[s[i]] == 1:
        r = i
        break
print(r)