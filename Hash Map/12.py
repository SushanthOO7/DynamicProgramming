"""
Hash Map
Question 12 — Subarray Sum Equals K
LeetCode #560 — Medium ⭐ Very important interview problem
Problem Description
Given an integer array nums and an integer k, return the total number of contiguous subarrays whose sum equals k.

Example 1
Input:
nums = [1, 1, 1]
k = 2

Expected Output:
2
Because:
[1,1]  indices 0–1
[1,1]  indices 1–2

Example 2
Input:
nums = [1, 2, 3]
k = 3

Expected Output:
2
Valid subarrays:
[1,2]
[3]

Example 3
Input:
nums = [1, -1, 0]
k = 0

Expected Output:
3
Valid subarrays:
[1,-1]
[0]
[1,-1,0]

Target Complexity
Time: O(n)
Space: O(n)
"""

nums = [1, 2, 3]
k = 3

p = 0
res = 0
d = {0:1}

for num in nums:
    p += num
    n = p - k
    if n in d:
        res += d[n]
    d[p] = d.get(p, 0) + 1
print(res)
