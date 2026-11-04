"""
Sliding Window:
Question 16 — Frequency of the Most Frequent Element
LeetCode #1838 — Medium
Problem Description
You are given an integer array nums and an integer k.
In one operation, you may choose an element and increase it by 1.
You can perform at most k operations.
Return the maximum possible frequency of any element after performing at most k operations.
You can only increase numbers, not decrease them.
Example 1
Input:
nums = [1, 2, 4]
k = 5

Expected Output:
3

We can turn everything into 4:
1 → 4 requires 3 operations
2 → 4 requires 2 operations
4 → 4 requires 0
Total = 5
So:
[1, 2, 4]
     ↓
[4, 4, 4]
Frequency = 3.

Example 2
Input:
nums = [1, 4, 8, 13]
k = 5

Expected Output:
2

For example:
4 → 8 requires 4 operations
[4, 8] → [8, 8]
But we don't have enough operations to make 3 elements equal.

Example 3
Input:
nums = [3, 9, 6]
k = 2

Expected Output:
1

Target Complexity
Aim for:
Time:  O(n log n)
Space: depends on sorting implementation
"""

nums = [3, 9, 6]
k = 2
nums.sort()
s = 0
l = 0
res = 0
for r in range(len(nums)):
    s += nums[r]
    while nums[r] * (r - l + 1) - s > k:
        s -= nums[l]
        l += 1
    res = max(res, r - l + 1)
print(res)

