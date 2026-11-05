"""
Hash Map
Question 7 — Isomorphic Strings
LeetCode #205 — Easy
Problem Description
Given two strings s and t, determine whether they are isomorphic.
Two strings are isomorphic if every character in s can be replaced to get t, while preserving the character order.
The mapping must be consistent:
- One character in s must always map to the same character in t.
- Two different characters in s cannot map to the same character in t.

Example 1
Input:
s = "egg"
t = "add"

Expected Output:
True
Because:
e → a
g → d
So:
egg
↓↓↓
add

Example 2
Input:
s = "foo"
t = "bar"

Expected Output:
False
Because o would need to map to both a and r:
f → b
o → a
o → r   ❌

Example 3
Input:
s = "badc"
t = "baba"

Expected Output:
False
You can't have two different characters mapping to the same target character.

Target Complexity
Time: O(n)
Space: O(n)
"""

s = "badc"
t = "baba"

sd = {}
td = {}
flag = True
for i in range(len(s)):
    if s[i] in sd and sd[s[i]] != t[i]:
        flag = False
        break
    if t[i] in td and td[t[i]] != s[i]:
        flag = False
        break
    sd[s[i]] = t[i]
    td[t[i]] = s[i]
print(flag)

