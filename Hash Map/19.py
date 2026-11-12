"""
Hash Map
Question 19 — Find the Difference of Two Arrays
LeetCode #2215 — Easy
Problem Description
Given two integer arrays nums1 and nums2, return a list containing two lists:
- The first contains all distinct integers in nums1 that are not present in nums2.
- The second contains all distinct integers in nums2 that are not present in nums1.
The order doesn't matter.

Example 1
Input:
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

Expected Output:
[[1, 3], [4, 6]]
Because:
nums1 only:
1, 3
nums2 only:
4, 6

Example 2
Input:
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

Expected Output:
[[3], []]
Notice that duplicates don't matter. We only want distinct values.

Target Complexity
Time: O(n + m) average
Space: O(n + m)
"""

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

n1 = set(nums1)
n2 = set(nums2)
a = []
b = []
for i in n1:
    if i not in n2:
        a.append(i)
for i in n2:
    if i not in n1:
        b.append(i)
print([a,b])