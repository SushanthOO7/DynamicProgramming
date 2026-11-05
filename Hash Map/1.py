"""
Hash Map
Question 1 — Two Sum
LeetCode #1 — Easy ⭐ Extremely common foundational problem
Problem Description
Given an integer array nums and an integer target, return the indices of two numbers such that they add up to target.
You may assume exactly one valid answer exists, and you cannot use the same element twice.
Example 1
Input:
nums = [2, 7, 11, 15]
target = 9

Expected Output:
[0, 1]
Because:
nums[0] + nums[1]
2 + 7 = 9

Example 2
Input:
nums = [3, 2, 4]
target = 6

Expected Output:
[1, 2]
Because:
2 + 4 = 6

Example 3
Input:
nums = [3, 3]
target = 6

Expected Output:
[0, 1]
You can't use index 0 twice, but there are two separate 3s.

Target Complexity
Time:  O(n)
Space: O(n)
"""

nums = [2, 7, 11, 15]
target = 9

d = {}
for i, n in enumerate(nums):
    w = target - n
    if w in d:
        print(d[w], i)
        break
    d[n] = i