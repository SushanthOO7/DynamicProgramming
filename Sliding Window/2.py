"""
Sliding Window:
Question 2 — Best Time to Buy and Sell Stock
LeetCode #121 — Easy
Problem Description
You are given an array prices where: prices[i] is the price of a stock on day i.
You can:
- Buy the stock once
- Sell the stock once
- You must buy before you sell
Return the maximum profit you can make. If you cannot make a profit, return 0.
Input:
prices = [7, 1, 5, 3, 6, 4]
Expected Output:
5
Input:
prices = [7, 6, 4, 3, 1]
Expected Output:
0
"""
p = [7, 1, 5, 3, 6, 4]
c = 0
l = 0
r = 1

while r < len(p):
    if p[l] < p[r]:
        c = max(c, p[r] - p[l])
    else:
        l = r
    r += 1
print(c)