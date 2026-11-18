"""
Binary Search
Question 12 — Split Array Largest Sum
LeetCode #410 — Hard ⭐ Binary Search on Answer
Problem Description
Given an integer array nums and an integer k, split nums into exactly k non-empty contiguous subarrays.
Your goal is to minimize the largest sum among those subarrays.
Return that minimum possible largest sum.

Example 1
nums = [7, 2, 5, 10, 8]
k = 2

Expected Output:
18
One optimal split is:
[7, 2, 5] | [10, 8]

sum = 14     sum = 18

largest sum = 18
Other splits:
[7] | [2,5,10,8]
 7         25        → largest = 25

[7,2] | [5,10,8]
  9          23      → largest = 23

[7,2,5,10] | [8]
     24         8     → largest = 24

So the minimum possible largest sum is:
18

Example 2
nums = [1, 2, 3, 4, 5]
k = 2

Expected Output:
9
One optimal split:
[1,2,3] | [4,5]
sum = 6    sum = 9

Example 3
nums = [1, 4, 4]
k = 3

Expected Output:
4
Split:
[1] | [4] | [4]

Target Complexity
Time:  O(n log(sum(nums)))
Space: O(1)
"""