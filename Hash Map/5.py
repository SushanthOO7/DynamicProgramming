"""
Hash Map
Question 5 — Top K Frequent Elements
LeetCode #347 — Medium ⭐ Common interview problem
Problem Description
Given an integer array nums and an integer k, return the k most frequent elements.
The answer can be returned in any order.

Example 1
Input:
nums = [1, 1, 1, 2, 2, 3]
k = 2

Expected Output:
[1, 2]
Because:
1 appears 3 times
2 appears 2 times
3 appears 1 time
So the two most frequent elements are 1 and 2.

Example 2
Input:
nums = [1]
k = 1

Expected Output:
[1]

Example 3
Input:
nums = [4, 4, 4, 6, 6, 7, 7, 7, 7]
k = 2

Expected Output:
[7, 4]

Target Complexity
Time:  O(n)
Space: O(n)
"""

nums = [1, 1, 1, 2, 2, 3]
k = 2

d = {}
for i in nums:
    d[i] = d.get(i, 0) + 1
b = [[] for i in range(len(nums) + 1)]
for num, f in d.items():
    b[f].append(num)
res = []
for i in range(len(b) - 1, 0, -1):
    for j in b[i]:
        res.append(j)
        if len(res) == k:
            break
print(res)
