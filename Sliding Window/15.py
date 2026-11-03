"""
Sliding Window:
Question 15 — Sliding Window Maximum
LeetCode #239 — Hard ⭐ Important monotonic deque problem
This is a perfect follow-up to Question 14 because you'll reuse the deque you just learned.
Problem Description
You are given an integer array nums and a fixed window size k.
The window moves from left to right one position at a time.
Return the maximum value inside each window.

Example 1
Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Expected Output:
[3, 3, 5, 5, 6, 7]

The windows are:
[1, 3, -1]             → max = 3
   [3, -1, -3]         → max = 3
       [-1, -3, 5]     → max = 5
           [-3, 5, 3]  → max = 5
               [5,3,6] → max = 6
                 [3,6,7] → max = 7

Example 2
Input:
nums = [1]
k = 1

Expected Output:
[1]

Target Complexity
Time:  O(n)
Space: O(k)
"""
from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

max_q = deque()
res = []

for r in range(len(nums)):
    if max_q and max_q[0] <= r - k:
        max_q.popleft()
    while max_q and nums[max_q[-1]] < nums[r]:
        max_q.pop()
    max_q.append(r)
    if r >= k - 1:
        res.append(nums[max_q[0]])
print(res)