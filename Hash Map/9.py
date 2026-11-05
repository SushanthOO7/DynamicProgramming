"""
Hash Map
Question 9 — Ransom Note
LeetCode #383 — Easy
This reinforces the frequency-map / consume counts pattern you used in Valid Anagram.
Problem Description
Given two strings ransomNote and magazine, return True if ransomNote can be constructed using the letters from magazine.
Each character in magazine can be used only once.

Example 1
Input:
ransomNote = "a"
magazine = "b"

Expected Output:
False

Example 2
Input:
ransomNote = "aa"
magazine = "ab"

Expected Output:
False
There is only one "a" available, but we need two.

Example 3
Input:
ransomNote = "aa"
magazine = "aab"

Expected Output:
True
The magazine has enough characters:
magazine:
a → 2
b → 1
need:
a → 2

Target Complexity
Time: O(n + m)
Space: O(1) for the fixed lowercase English alphabet.
"""

ransomNote = "aa"
magazine = "ab"

md = {}
flag = True
for i in magazine:
    md[i] = md.get(i, 0) + 1
for i in ransomNote:
    if i not in md or md[i] == 0:
        flag = False
        break
    md[i] -= 1
print(flag)


