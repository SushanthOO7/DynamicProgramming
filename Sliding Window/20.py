"""
Sliding Window:
Question 20 — Binary Subarrays With Sum
LeetCode #930 — Medium
Problem Description
Given a binary array nums and an integer goal, return the number of contiguous non-empty subarrays whose sum is exactly goal.

Example 1
Input:
nums = [1, 0, 1, 0, 1]
goal = 2

Expected Output:
4

The valid subarrays are:
[1,0,1]       indices 0–2
[1,0,1,0]     indices 0–3
[0,1,0,1]     indices 1–4
[1,0,1]       indices 2–4

Example 2
Input:
nums = [0, 0, 0, 0, 0]
goal = 0

Expected Output:
15

Target Complexity
Time:  O(n)
Space: O(1)
"""

nums = [0, 0, 0, 0, 0]
goal = 0
ans = 0

def atMost(k):
    if k < 0:
        return 0
    res = 0
    s = 0
    l = 0
    for r in range(len(nums)):
        s += nums[r]
        while s > k:
            s -= nums[l]
            l += 1
        res += r - l + 1
    return res

print(atMost(goal) - atMost(goal - 1))

