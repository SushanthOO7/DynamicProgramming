"""
Sliding Window:
Question 12 — Subarray Product Less Than K
LeetCode #713 — Medium
Problem Description
Given an array of positive integers nums and an integer k,
return the number of contiguous subarrays where the product of all elements is strictly less than k.

Example 1
Input:
nums = [10, 5, 2, 6]
k = 100

Expected Output:
8

The valid subarrays are:
[10]
[5]
[2]
[6]
[10,5]
[5,2]
[2,6]
[5,2,6]
That's 8.

Example 2
Input:
nums = [1, 2, 3]
k = 0

Expected Output:
0

Target Complexity
Time: O(n)
Space: O(1)
"""

nums = [10, 5, 2, 6]
k = 100

l = 0
p = 1
c = 0

for r in range(len(nums)):
    p *= nums[r]
    while p >= k:
        p //= nums[l]
        l += 1
    c += r - l + 1
print(c)