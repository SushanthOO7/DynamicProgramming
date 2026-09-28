"""
Sliding Window:
Question 3 — Maximum Average Subarray I
LeetCode #643 — Easy
Problem Description
You are given an integer array nums and an integer k.
Find a contiguous subarray of exactly k elements that has the maximum average, and return that average.
Input:
nums = [1, 12, -5, -6, 50, 3]
k = 4
Expected Output:
12.75
All windows of size 4 are:
[1, 12, -5, -6]    sum = 2
[12, -5, -6, 50]   sum = 51
[-5, -6, 50, 3]    sum = 42
Input:
nums = [5]
k = 1
Expected Output:
5.0
"""
nums = [1, 12, -5, -6, 50, 3]
k = 4
m = 0
s = 0
for i in range(k):
    s += nums[i]
m = s
for i in range(k, len(nums)):
    s = s + (nums[i] - nums[i - k])
    m = max(m, s)
print(m/k)