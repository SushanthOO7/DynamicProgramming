"""
Hash Map
Question 16 — Longest Harmonious Subsequence
LeetCode #594 — Easy
Problem Description
A harmonious subsequence is a subsequence where the difference between the maximum value and minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence.
A subsequence does not need to be contiguous.

Example 1
Input:
nums = [1, 3, 2, 2, 5, 2, 3, 7]

Expected Output:
5
Why?
We can use:
[3, 2, 2, 2, 3]
It contains:
2 → 3 times
3 → 2 times
and:
max - min
= 3 - 2
= 1
So:
length = 3 + 2 = 5

Example 2
Input:
nums = [1, 2, 3, 4]

Expected Output:
2
Possible harmonious subsequences include [1,2], [2,3], or [3,4].

Example 3
Input:
nums = [1, 1, 1, 1]

Expected Output:
0
This is important. You cannot use only 1s because:
max - min = 0
but the problem requires exactly 1.

Target Complexity
Time: O(n) average
Space: O(n)
"""

nums = [1, 1, 1, 1]

d = {}
s = set()
res = 0
for n in nums:
    s.add(n)
    d[n] = d.get(n, 0) + 1
for n in s:
    need = n - 1
    if need in d:
        res = max(res, d[n] + d[need])
print(res)

