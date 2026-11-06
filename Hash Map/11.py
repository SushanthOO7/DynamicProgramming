"""
Hash Map
Question 11 — Contains Duplicate II
LeetCode #219 — Easy
Problem Description
Given an integer array nums and an integer k, return True if there are two different indices i and j such that:
nums[i] == nums[j] and: |i - j| <= k
Otherwise return False.
In simpler terms:
Find whether the same number appears twice within at most k positions of each other.
Example 1
Input:
nums = [1, 2, 3, 1]
k = 3

Expected Output:
True
Because:
nums[0] = nums[3] = 1
|3 - 0| = 3
3 <= k

Example 2
Input:
nums = [1, 0, 1, 1]
k = 1

Expected Output:
True
The last two 1s are at indices 2 and 3:
3 - 2 = 1 <= k

Example 3
Input:
nums = [1, 2, 3, 1, 2, 3]
k = 2

Expected Output:
False
Each duplicate is 3 positions away, which is greater than k.

Target Complexity
Time: O(n)
Space: O(n)
"""

nums = [1, 2, 3, 1]
k = 3

d = {}
flag = False
for i, num in enumerate(nums):
    if num in d and (i - d[num]) <= k:
        flag = True
        break
    d[num] = i
print(flag)
