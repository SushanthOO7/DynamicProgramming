"""
Sliding Window:
Question 14 — Longest Subarray With Absolute Diff ≤ Limit
LeetCode #1438 — Medium
This introduces an important advanced sliding-window idea:
maintaining the minimum and maximum values inside the current window.
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

nums = [10, 1, 2, 4, 7, 2]
limit = 5
max_ = float("-inf")
min_ = float("inf")
l = 0
res = 0
w = []
for r in range(len(nums)):
    w.append(nums[r])
    if nums[r] > max_:
        max_ = nums[r]
    if nums[r] < min_:
        min_ = nums[r]
    d = max_ - min_
    while d > limit and r != l:
        if max_ == nums[l]:
            w.remove(nums[l])
            max_ = max(w)
            d = max_ - min_
        elif min_ == nums[l]:
            w.remove(nums[l])
            min_ = min(w)
            d = max_ - min_
        else:
            w.remove(nums[l])
        l += 1
    if d <= limit:
        res = max(res, r - l + 1)
print(res)
