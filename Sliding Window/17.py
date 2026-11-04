"""
Sliding Window:
Question 17 — Minimum Operations to Reduce X to Zero
LeetCode #1658 — Medium
Problem Description
You are given an integer array nums and an integer x.
In one operation, you can remove either the leftmost or rightmost element from nums and subtract its value from x.
Return the minimum number of operations needed to reduce x to exactly 0.
If it's impossible, return -1.

Example 1
Input:
nums = [1, 1, 4, 2, 3]
x = 5

Expected Output:
2
Remove 2 elements from the right:
3 + 2 = 5

Example 2
Input:
nums = [5, 6, 7, 8, 9]
x = 4

Expected Output:
-1
You cannot remove elements from the ends that sum to exactly 4.

Example 3
Input:
nums = [3, 2, 20, 1, 1, 3]
x = 10

Expected Output:
5

Target Complexity
Time:  O(n)
Space: O(1)
"""

nums = [1, 1, 4, 2, 3]
x = 5
ts = sum(nums)
need = ts - x


if need < 0:
    print(-1)
elif need == 0:
    print(len(nums))
else:
    l = 0
    s = 0
    res = -1
    for r in range(len(nums)):
        s += nums[r]
        while s > need:
            s -= nums[l]
            l += 1
        if need == s:
            res = max(res, r - l + 1)

    if res == -1:
        print(-1)
    else:
        print(len(nums) - res)





