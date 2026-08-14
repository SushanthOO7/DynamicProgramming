"""Two pointers:
Question 3 — Two Sum II
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
"""

n = [1, 2, 4, 6, 10]
t = 8
l = 0
r = len(n) - 1

while l < r:
    s = n[l] + n[r]
    if s == t:
        print([l, r])
        break
    elif s > t:
        r -= 1
    else:
        l += 1