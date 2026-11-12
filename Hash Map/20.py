"""
Hash Map
Question 20 — Longest Palindrome
LeetCode #409 — Easy
Problem Description
Given a string s containing lowercase and uppercase English letters, return the length of the longest palindrome that can be built using those characters.
Characters are case-sensitive:
"A" != "a"
You can rearrange the characters however you want.

Example 1
Input:
s = "abccccdd"

Expected Output:
7
One possible palindrome is:
dccaccd
Length = 7.

Example 2
Input:
s = "a"

Expected Output:
1

Example 3
Input:
s = "bb"

Expected Output:
2
What you need to figure out
A palindrome has matching characters on both sides:
a b c _ c b a
↑ ↑ ↑   ↑ ↑ ↑
So characters are mostly used in pairs.
For example, if:
a appears 4 times → all 4 can be used
b appears 3 times → only 2 can form a pair
c appears 2 times → all 2 can be used
But a palindrome can also have one unpaired character in the center:
a b c X c b a
      ↑
   one center

Target Complexity
Time: O(n)
Space: O(1) for the fixed English-letter alphabet.
"""

s = "abccccdd"

d = {}
res = 0
odd = False
for i in s:
    d[i] = d.get(i, 0) + 1
for i in d:
    if d[i] % 2 == 0:
        res += d[i]
    else:
        res += (d[i] - 1)
        odd = True
if odd:
    res += 1
print(res)

