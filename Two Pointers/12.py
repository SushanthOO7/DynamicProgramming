"""
Two pointers:
Question 12 — Trapping Rain Water (LeetCode #42)
Problem Description
Requirement:
The array represents wall heights, and you need to calculate how much rainwater can be trapped between the walls.
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
Expected Output:
6
Input:
height = [4,2,0,3,2,5]
Expected Output:
9
"""
h = [0,1,0,2,1,0,1,3,2,1,2,1]
l = 0
r = len(h) - 1
lmax = 0
rmax = 0
w = 0

while l < r:
    if h[l] <= h[r]:
        if h[l] >= lmax:
            lmax = h[l]
        else:
            w += lmax - h[l]
        l += 1
    else:
        if h[r] >= rmax:
            rmax = h[r]
        else:
            w += rmax - h[r]
        r -= 1
print(w)
