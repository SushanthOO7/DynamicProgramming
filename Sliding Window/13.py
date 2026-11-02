"""
Sliding Window:
Question 11 — Maximum Points You Can Obtain from Cards
LeetCode #1423 — Medium
Problem Description
You are given an integer array cardPoints and an integer k.
You must take exactly k cards.
On each move, you may take a card only from the beginning or the end of the array.
Return the maximum score you can obtain.

Example 1
Input:
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

Expected Output:
12
One optimal choice is taking the last three relevant end choices to get:
1 from left + 6 from right + 5 from right = 12

Example 2
Input:
cardPoints = [2, 2, 2]
k = 2

Expected Output:
4

Example 3
Input:
cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7

Expected Output:
55

Target Complexity
Time: O(n)
Space: O(1)
"""

cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
n = len(cardPoints)
m = float("inf")
t = sum(cardPoints)
s = 0

if n == k:
    m = t
else:
    w = n - k
    s = sum(cardPoints[:w])
    m = s
    for r in range(w, len(cardPoints)):
        s += cardPoints[r]
        s -= cardPoints[r - w]
        m = min(m, s)
    m = t - m
print(m)