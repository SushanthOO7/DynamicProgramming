"""
Binary Search
Question 5 — Find Minimum in Rotated Sorted Array
LeetCode #153 — Medium ⭐
Problem Description
You are given a sorted array of distinct integers that has been rotated.
Return the minimum element.
You must solve it in O(log n) time.
Example 1
nums = [3, 4, 5, 1, 2]

Expected:
1

Example 2
nums = [4, 5, 6, 7, 0, 1, 2]

Expected:
0

Example 3 — Not rotated
nums = [11, 13, 15, 17]

Expected:
11

Target Complexity
Time: O(log n)
Space: O(1)
"""

nums = [3, 4, 5, 1, 2]

l = 0
r = len(nums) - 1
while l < r:
    m = (l + r) // 2
    if nums[m] > nums[r]:
        l = m + 1
    else:
        r = m
print(nums[l])
