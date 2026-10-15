"""
Sliding Window:
Question 6 — Max Consecutive Ones III
LeetCode #1004 — Medium
This is a high-value interview sliding-window problem and reinforces the variable-size window pattern.
Problem Description
You are given a binary array nums containing only 0s and 1s, and an integer k`.
You can change at most k zeros into ones.
Return the maximum number of consecutive 1s you can obtain.
Example 1
Input:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
Expected Output:
6
You can flip at most two 0s, allowing a consecutive section of length 6.
Example 2
Input:
nums = [0,0,1,1,1,0,0]
k = 0
Expected Output:
3
Since k = 0, you cannot change any zeros.
Example 3
Input:
nums = [1,1,0,1,1]
k = 1
Expected Output:
5
"""
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
l = 0
m = 0
z = 0
for r in range(len(nums)):
    if nums[r] == 0:
        z += 1
    while z > k:
        if nums[l] == 0:
            z -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)