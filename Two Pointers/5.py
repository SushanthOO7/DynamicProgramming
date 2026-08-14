"""Two pointers:
Question 5 — Move Zeroes(LeetCode #283)
Input
nums = [0, 1, 0, 3, 12]
Expected Output
[1, 3, 12, 0, 0]
"""

n = [1, 0, 2]
l = 0

for r in range(0, len(n)):
    if int(n[r]) != 0:
        t = n[r]
        n[r] = n[l]
        n[l] = t
        l += 1

print(n)

