"""
Binary Search
Question 4 — Search in Rotated Sorted Array
LeetCode #33 — Medium ⭐
Problem Description
You are given a sorted array that has been rotated at some unknown position.
For example, originally:
[0, 1, 2, 4, 5, 6, 7]
After rotation:
[4, 5, 6, 7, 0, 1, 2]
Given a target, return its index. If it doesn't exist, return -1.
All values are distinct.

Example 1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

Expected:
4

Example 2
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

Expected:
-1

Example 3
nums = [1]
target = 0

Expected:
-1

Target Complexity
Time: O(log n)
Space: O(1)
"""

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
l = 0
r = len(nums) - 1
res = -1
while l <= r:
    m = (l + r) // 2
    if target == nums[m]:
        res = m
        break
    if nums[l] <= nums[m]:
        if nums[l] <= target < nums[m]:
            r = m - 1
        else:
            l = m + 1
    else:
        if nums[m] < target <= nums[r]:
            l = m + 1
        else:
            r = m - 1
print(res)