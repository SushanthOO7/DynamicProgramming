"""Two pointers:
Question 7 — Squares of a Sorted Array (LeetCode #977)
Input
nums = [-4, -1, 0, 3, 10]
Expected Output
[0, 1, 9, 16, 100]
"""

"""Solution: 1
n = [-4, -1, 0, 3, 10]
l = 0
r = len(n) - 1
res = []
while l <= r:
    ll = n[l] ** 2
    rr = n[r] ** 2
    if ll > rr:
        res.append(ll)
        l += 1
    else:
        res.append(rr)
        r -= 1

print(res[::-1])
"""

n = [-4, -1, 0, 3, 10]
l = 0
r = len(n) - 1
res = [0] * len(n)
i = len(n) - 1

while l <= r:
    ll = n[l] ** 2
    rr = n[r] ** 2
    if ll > rr:
        res[i] = ll
        l += 1
    else:
        res[i] = rr
        r -= 1
    i -= 1
print(res)