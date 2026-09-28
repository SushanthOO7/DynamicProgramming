"""
Two pointers:
Question 11 — Sort Colors (LeetCode #75)
Problem Description
Requirement: Sort the array in-place with O(1) extra space.
Input:
nums = [2, 0, 2, 1, 1, 0]
Expected Output:
[0, 0, 1, 1, 2, 2]
"""

a = [2, 0, 2, 1, 1, 0]

l = 0
m = 0
r = len(a) - 1

while m <= r:
    if a[m] == 0:
        a[l], a[m] = a[m] , a[l]
        l += 1
        m += 1
    elif a[m] == 1:
        m += 1
    else:
        a[r], a[m] = a[m], a[r]
        r -= 1

print(a)