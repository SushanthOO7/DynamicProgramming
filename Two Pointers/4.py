"""Two pointers:
Question 4 — Remove Duplicates from Sorted Array
nums = [1, 1, 2]

After modification:
nums = [1, 2, ...]

Return:
2
"""

n = [0,0,1,1,1,2,2,3,3,4]
l = 0
for r in range(1, len(n)):
    if n[r] != n[l]:
        l += 1
        n[l] = n[r]
print(n[:l+1])
