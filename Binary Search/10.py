"""
Binary Search
Question 10 — Peak Index in a Mountain Array
LeetCode #852 — Medium
Problem Description
You are given a mountain array arr.
A mountain array:
- strictly increases to a peak
- then strictly decreases
Return the index of the peak element.

Example 1
arr = [0, 1, 0]

Expected Output:
1
Because:
[0, 1, 0]
    ↑
   peak

Example 2
arr = [0, 2, 1, 0]

Expected Output:
1

Example 3
arr = [0, 10, 5, 2]

Expected Output:
1

Target Complexity
Time:  O(log n)
Space: O(1)
"""

arr = [0, 10, 5, 2]

l = 0
r = len(arr) - 1
while l < r:
    m = (l + r) // 2
    if arr[m] < arr[m+1]:
        l = m + 1
    else:
        r = m
print(l)
