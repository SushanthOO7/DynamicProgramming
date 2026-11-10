"""
Hash Map
Question 15 — 4Sum II
LeetCode #454 — Medium
Problem Description
You are given four integer arrays:
nums1, nums2, nums3, nums4
Return the number of tuples (i, j, k, l) such that:
nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0

Example 1
Input:
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

Expected Output:
2
The two valid combinations are:
1 + (-2) + (-1) + 2 = 0
2 + (-1) + (-1) + 0 = 0

Example 2
Input:
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]

Expected Output:
1
Don't use four nested loops
The brute-force approach would be:
for a
  for b
    for c
      for d
which is:
O(n⁴) ❌

Target Complexity
Aim for:
Time:  O(n²)
Space: O(n²)
"""

nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

need_d = {}
res = 0

for a in nums1:
    for b in nums2:
        s = a + b
        need_d[s] = need_d.get(s, 0) + 1

for c in nums3:
    for d in nums4:
        need = -(c + d)
        if need in need_d:
            res += need_d[need]
print(res)