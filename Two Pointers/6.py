"""Two pointers:
Question 6 — Remove Element (LeetCode #27)
Input
nums = [3, 2, 2, 3]
val = 3
Expected Output
k = 2
nums[:k] = [2, 2]
"""

n = [0, 1, 2, 2, 3, 0, 4, 2]
v = 2

l = 0

for r in range(0, len(n)):
    if n[r] != 2:
        t = n[r]
        n[r] = n[l]
        n[l] = t
        l += 1
k = l

print(k)
print(n)



