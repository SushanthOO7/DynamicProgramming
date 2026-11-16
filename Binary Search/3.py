"""
Binary Search
Question 3 — Find First and Last Position of Element in Sorted Array
LeetCode #34 — Medium ⭐ Very common binary-search variation
Problem Description
Given a sorted integer array nums and a target, return the starting and ending index of the target.
If the target doesn't exist, return:
[-1, -1]
You must achieve O(log n) time.

Example 1
nums = [5, 7, 7, 8, 8, 10]
target = 8

Expected:
[3, 4]
Because:
index:  0  1  2  3  4   5
nums:  [5, 7, 7, 8, 8, 10]
                  ↑  ↑
                first last

Example 2
nums = [5, 7, 7, 8, 8, 10]
target = 6

Expected:
[-1, -1]

Example 3
nums = [2, 2, 2, 2, 2]
target = 2

Expected:
[0, 4]

Target Complexity
Time: O(log n)
Space: O(1)
"""

nums = [2, 2, 2, 2, 2]
target = 2

def search(left_side):
    l = 0
    r = len(nums) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            res = m
            if left_side:
                r = m - 1
            else:
                l = m + 1
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return res
first = search(True)
last = search(False)
print([first, last])