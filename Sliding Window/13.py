"""
Sliding Window:
Question 13 — Minimum Window Substring
LeetCode #76 — Hard ⭐ Very important sliding-window problem
Problem Description
Given two strings s and t, return the smallest substring of s that contains every character from t, including duplicates.
If no such substring exists, return "".

Example 1
Input:
s = "ADOBECODEBANC"
t = "ABC"

Expected Output:
"BANC"
"BANC" contains:
A → 1
B → 1
C → 1
and there is no smaller substring containing all three.

Example 2
Input:
s = "a"
t = "a"

Expected Output:
"a"

Example 3 — Duplicates matter
Input:
s = "AAABBC"
t = "AABC"

Expected Output:
"AABBC"

Because t requires:
A → 2
B → 1
C → 1
So "ABBC" would not be valid because it only contains one A.

Target Complexity
Aim for:
Time:  O(n)
Space: O(number of distinct characters)
"""

s = "ADOBECODEBANC"
t = "ABC"

w = {}
n = {}

for i in t:
    n[i] = n.get(i, 0) + 1

l = 0
m = float("inf")
need = len(n)
h = 0
st = 0

for r in range(len(s)):
    c = s[r]
    w[c] = w.get(c, 0) + 1

    if c in n and w[c] == n[c]:
        h += 1

    while h == need:
        if (r - l + 1) < m:
            m = r - l + 1
            st = l

        ch = s[l]
        w[ch] -= 1

        if ch in n and w[ch] < n[ch]:
            h -= 1
        l += 1
if m == float("inf"):
    print("")
else:
    print(s[st:st+m])