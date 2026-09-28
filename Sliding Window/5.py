"""
Sliding Window:
Question 5 — Minimum Size Subarray Sum
LeetCode #209 — Medium
Problem Description
Given an array of positive integers nums and a positive integer target, find the smallest length of a contiguous subarray whose sum is greater than or equal to target.
Return 0 if no such subarray exists.
Input:
nums = [2, 3, 1, 2, 4, 3]
target = 7
Expected Output:
2
4 + 3 = 7
Input:
nums = [1, 4, 4]
target = 4
Expected Output:
1
Input:
nums = [1, 1, 1, 1, 1]
target = 11
Expected Output:
0
"""
nums = [2, 3, 1, 2, 4, 3]
t = 7
l = 0
s = 0
m = float("inf")

for r in range(len(nums)):
    s += nums[r]
    while s >= t:
        m = min(m, r - l + 1)
        s -= nums[l]
        l += 1
if m == float("inf"):
    m = 0
print(m)


