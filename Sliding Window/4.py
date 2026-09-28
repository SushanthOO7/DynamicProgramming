"""
Sliding Window:
Question 4 — Longest Subarray of 1's After Deleting One Element
LeetCode #1493 — Medium
Problem Description
Given a binary array nums containing only 0 and 1.
You must delete exactly one element from the array.
Return the length of the longest contiguous subarray containing only 1s after that deletion.
Input:
nums = [1,1,0,1]
Expected Output:
3
Delete the 0:
[1,1,1]
Length = 3.
Input:
nums = [0,1,1,1,0,1,1,0,1]
Expected Output:
5
Input:
nums = [1,1,1]
Expected Output:
2
"""

nums = [0,1,1,1,0,1,1,0,1]
z = 0
l = 0
s = 0

for r in range(len(nums)):
    if nums[r] == 0:
        z += 1
    while z > 1:
        if nums[l] == 0:
            z -= 1
        l += 1
    s = max(s, r - l)

print(s)




