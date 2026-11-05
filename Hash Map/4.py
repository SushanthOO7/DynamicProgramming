"""
Hash Map
Question 4 — Group Anagrams
LeetCode #49 — Medium ⭐ Very common interview problem
This is the natural next step after Valid Anagram.
Problem Description
Given an array of strings strs, group all strings that are anagrams of each other.
You can return the groups in any order.

Example 1
Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Expected Output:
[["eat", "tea", "ate"],["tan", "nat"],["bat"]]
Because:
eat, tea, ate → same character frequencies
tan, nat      → same character frequencies
bat           → no matching anagram

Example 2
Input:
strs = [""]

Expected Output:
[[""]]

Example 3
Input:
strs = ["a"]

Expected Output:
[["a"]]

Target Complexity
Time:  O(n × k)
Space: O(n × k)
where:
- n = number of strings
- k = average/max length of a string
"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

d = {}
res = []
for i in range(len(strs)):
    c = [0] * 26
    for j in range(len(strs[i])):
        o = ord(strs[i][j]) - ord('a')
        c[o] += 1
    k = tuple(c)
    d.setdefault(k, []).append(strs[i])
res = list(d.values())
print(res)