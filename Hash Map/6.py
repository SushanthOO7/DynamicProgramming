"""
Hash Map
Question 6 — Longest Consecutive Sequence
LeetCode #128 — Medium ⭐ Very common interview problem
Problem Description
Given an unsorted array of integers nums, return the length of the longest consecutive sequence.
The numbers must be consecutive by value, but they do not need to appear consecutively in the input array.
You must solve it in O(n) time.

Example 1
Input:
nums = [100, 4, 200, 1, 3, 2]

Expected Output:
4
Because:
1, 2, 3, 4

is the longest consecutive sequence.
Example 2
Input:
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Expected Output:
9
Because:
0, 1, 2, 3, 4, 5, 6, 7, 8
has length 9.

Example 3
Input:
nums = [1, 0, 1, 2]

Expected Output:
3
Sequence:
0, 1, 2
Duplicates don't increase the sequence length.

Target Complexity
Time: O(n)
Space: O(n)
"""

nums = [100, 4, 200, 1, 3, 2, 6, 7, 8, 9]
n = set(nums)
m = 0
for num in n:
    if num - 1 not in n:
        l = 1
        cn = num
        while num + 1 in n:
            l += 1
            num += 1
        m = max(m, l)
print(m)
