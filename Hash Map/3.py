"""
Hash Map
Question 3 — Valid Anagram
LeetCode #242 — Easy ⭐ Common foundational problem
Problem Description
Given two strings s and t, return True if t is an anagram of s. Otherwise return False.
An anagram contains exactly the same characters with exactly the same frequencies,
but the characters may be in a different order.
Example 1
Input:
s = "anagram"
t = "nagaram"

Expected Output:
True
Both contain:
a → 3
n → 1
g → 1
r → 1
m → 1

Example 2
Input:
s = "rat"
t = "car"

Expected Output:
False

Example 3
Input:
s = "aacc"
t = "ccac"

Expected Output:
False
The frequencies differ:
s: a=2, c=2
t: a=1, c=3

Target Complexity
Time:  O(n)
Space: O(1)
"""

s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)
else:
    c = {}
    for i in s:
        c[i] = c.get(i, 0) + 1
    for i in t:
        if i not in c:
            print(False)
            break
        c[i] -= 1
        if c[i] < 0:
            print(False)
            break
    else:
        print(True)