"""Two pointers:
Question 7 — 3Sum (LeetCode #15)
Input
nums = [-1, 0, 1, 2, -1, -4]
Expected Output
[[-1, -1, 2], [-1, 0, 1]]
Find all unique triplets such that:
a + b + c = 0
"""

n = [-1, 0, 1, 2, -1, -4]
res = []
n.sort()
for i in range(len(n)):
    if i > 0 and n[i] == n[i - 1]:
        continue
    l = i + 1
    r = len(n) - 1
    while l < r:
        s = n[i] + n[l] + n[r]
        if s == 0:
            res.append([n[i],n[l],n[r]])
            while l < r and n[l] == n[l + 1]:
                l += 1
            while l < r and n[r] == n[r - 1]:
                r -= 1
            l += 1
            r -= 1
        elif s > 0:
            r -= 1
        else:
            l += 1

print(res)