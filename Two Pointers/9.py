"""Two pointers:
Question 9 — Container With Most Water (LeetCode #11)
Input
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Expected Output
49
You need to find the maximum amount of water that can be contained between two vertical lines.
"""

h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
m = 0
l = 0
r = len(h) - 1
while l < r:
    s = min(h[l], h[r]) * (r - l)
    if h[l] < h[r]:
        l += 1
    else:
        r -= 1
    if s > m:
        m = s
print(m)