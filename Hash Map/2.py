"""
Hash Map
Question 2 — Contains Duplicate
LeetCode #217 — Easy
Problem Description
Given an integer array nums, return True if any value appears at least twice.
Return False if every element is unique.

Example 1
Input:
nums = [1, 2, 3, 1]

Expected Output:
True
Because 1 appears twice.

Example 2
Input:
nums = [1, 2, 3, 4]

Expected Output:
False
Every number is unique.

Example 3
Input:
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

Expected Output:
True

Target Complexity
Time:  O(n)
Space: O(n)
"""

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

s = set()
flag = False
for i in nums:
    if i in s:
        flag = True
        break
    s.add(i)
print(flag)