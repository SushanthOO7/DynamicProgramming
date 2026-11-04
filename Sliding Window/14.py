"""
Sliding Window:
Question 14 — Longest Subarray With Absolute Diff ≤ Limit
LeetCode #1438 — Medium
Problem Description
Given an integer array nums and an integer limit, return the length of the longest contiguous subarray
such that the absolute difference between any two elements in that subarray is less than or equal to limit.
In other words, a window is valid when:
max(window) - min(window) <= limit

Example 1
Input:
nums = [8, 2, 4, 7]
limit = 4

Expected Output:
2
For example:
[2, 4]
has:
max = 4
min = 2
4 - 2 = 2 <= 4
But:
[8, 2] is invalid:
8 - 2 = 6 > 4

Example 2
Input:
nums = [10, 1, 2, 4, 7, 2]
limit = 5

Expected Output:
4

One longest valid subarray is:
[2, 4, 7, 2]
because:
max = 7
min = 2
7 - 2 = 5

Target Complexity
Aim for:
Time:  O(n)
Space: O(n)
"""
from collections import deque
nums = [8, 2, 4, 7]
limit = 4
max_q = deque()
min_q = deque()
l = 0
res = 0

for r in range(len(nums)):

    while max_q and nums[r] > nums[max_q[-1]]:
        max_q.pop()
    max_q.append(r)

    while min_q and nums[r] < nums[min_q[-1]]:
        min_q.pop()
    min_q.append(r)

    while nums[max_q[0]] - nums[min_q[0]] > limit:
        if max_q[0] == l:
            max_q.popleft()
        if min_q[0] == l:
            min_q.popleft()
        l += 1

    res = max(res, r - l + 1)
print(res)
