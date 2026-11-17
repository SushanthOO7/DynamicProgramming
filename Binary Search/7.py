"""
Binary Search
Question 7 — Koko Eating Bananas
LeetCode #875 — Medium ⭐ Very important Binary Search on Answer problem
We're searching for the minimum valid answer.
Problem Description
Koko has piles of bananas:
piles = [3, 6, 7, 11]
h = 8
Koko chooses an eating speed k bananas per hour.
For each pile, she spends:
ceil(pile / k) hours.
She must finish all bananas within h hours.
Return the minimum eating speed k that allows her to finish on time.

Example 1
piles = [3, 6, 7, 11]
h = 8

Expected:
4
If:
k = 4 bananas/hour
then:
pile 3  → ceil(3/4)  = 1 hour
pile 6  → ceil(6/4)  = 2 hours
pile 7  → ceil(7/4)  = 2 hours
pile 11 → ceil(11/4) = 3 hours

total = 1 + 2 + 2 + 3
      = 8 hours ✅
But speed 3:
3  → 1 hour
6  → 2 hours
7  → 3 hours
11 → 4 hours
total = 10 hours ❌
Therefore minimum speed = 4.

Hint:
Where is Binary Search?
Think about all possible speeds:
1  2  3  4  5  6  7 ... 11
❌ ❌ ❌ ✅ ✅ ✅ ✅ ... ✅
         ↑
     first valid
Once a speed is fast enough, every larger speed will also be fast enough.
That's the property that allows binary search.
Your search space is:
l = 1r = max(piles)
For each:
m = (l + r) // 2
calculate how many hours speed m requires.
Then ask:
hours <= h ?
If yes, m works—but maybe a smaller speed also works, so search left.
If no, m is too slow, so search right.

Target Complexity
O(n log(max(piles)))
"""
from math import ceil

piles = [3, 6, 7, 11]
h = 8

l = 1
r = max(piles)
res = float("inf")
while l <= r:
    m = (l + r) // 2
    total_t = 0
    for i in piles:
        total_t += ceil(i / m)
    if total_t <= h:
        res = min(res, m)
        r = m - 1
    else:
        l = m + 1
print(res)
