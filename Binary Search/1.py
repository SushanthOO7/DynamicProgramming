"""
Binary Search
Question 1 — Binary Search
LeetCode #704 — Easy ⭐ Foundation problem
Problem Description
You are given an array of integers nums sorted in ascending order and an integer target.
Return the index of target if it exists.
If it doesn't exist, return -1.

Example 1
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9

Expected Output:
4
because:
index:   0   1  2  3  4   5
nums:   [-1, 0, 3, 5, 9, 12]
                     ↑
                  target

Example 2
nums = [-1, 0, 3, 5, 9, 12]
target = 2

Expected:
-1
because 2 doesn't exist.

Target Complexity
Time: O(log n)
Space: O(1)
"""

nums = [-1, 0, 3, 5, 9, 12]
target = 9

res = -1
l = 0
r = len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target == nums[m]:
        res = m
        break
    elif target > nums[m]:
        l = m + 1
    else:
        r = m - 1
print(res)
