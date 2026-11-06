"""
Hash Map
Question 13 — Contiguous Array
LeetCode #525 — Medium ⭐ Great prefix-sum + hash-map problem
Problem Description
Given a binary array nums containing only 0s and 1s, return the maximum length of a contiguous subarray containing an equal number of 0s and 1s.

Example 1
Input:
nums = [0, 1]

Expected Output:
2
Because:
[0, 1]
zeros = 1
ones  = 1

Example 2
Input:
nums = [0, 1, 0]

Expected Output:
2
Both [0,1] and [1,0] have equal numbers of zeros and ones.

Example 3
Input:
nums = [0, 0, 1, 0, 0, 0, 1, 1]

Expected Output:
6
A longest valid contiguous subarray has 3 zeros and 3 ones.
Target Complexity
Time: O(n)
Space: O(n)
"""