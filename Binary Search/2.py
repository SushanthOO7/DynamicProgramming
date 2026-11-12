"""
Binary Search
Question 2 — Search Insert Position
LeetCode #35 — Easy ⭐ Important binary-search variation
Problem Description
You are given a sorted array of distinct integers nums and a target.
- If target exists, return its index.
- If it doesn't exist, return the index where it should be inserted so the array remains sorted.

Example 1
nums = [1, 3, 5, 6]
target = 5

Expected:
2
because 5 already exists at index 2.

Example 2
nums = [1, 3, 5, 6]
target = 2

Expected:
1
Because inserting 2 here maintains sorted order:
[1, 2, 3, 5, 6]
    ↑
  index 1

Example 3
nums = [1, 3, 5, 6]
target = 7

Expected:
4
Insert after everything:
[1, 3, 5, 6, 7]
             ↑
           index 4

Example 4
nums = [1, 3, 5, 6]
target = 0

Expected:
0

Target Complexity
Time: O(log n)
Space: O(1)
"""

nums = [1, 3, 5, 6]
target = 7

l = 0
r = len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target == nums[m]:
        l = m
        break
    elif target > nums[m]:
        l = m + 1
    else:
        r = m - 1
print(l)