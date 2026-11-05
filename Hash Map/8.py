"""
Hash Map
Question 8 — Happy Number
LeetCode #202 — Easy
This teaches a useful Hash Set → cycle detection pattern.
Problem Description
Given a positive integer n, repeatedly replace it with the sum of the squares of its digits.
If the process eventually reaches 1, return True.
If the process enters a cycle and will never reach 1, return False.

Example 1
Input:
n = 19

Expected Output:
True
Because:
19
↓
1² + 9² = 82
↓
8² + 2² = 68
↓
6² + 8² = 100
↓
1² + 0² + 0² = 1

Example 2
Input:
n = 2

Expected Output:
False

Eventually the calculations start repeating, meaning we've entered a cycle and will never reach 1.
Target Complexity
For interview purposes, focus on the cycle-detection idea rather than the unusual mathematical bound of this particular problem.
Space: use a hash set to remember previously seen numbers.
"""

def cal(n):
    s = 0
    while n // 10 != 0:
        s += (n % 10) ** 2
        n = n // 10
    s += (n % 10) ** 2
    return s
s = set()
n = 19
flag = True
while n != 1:
    if n in s:
        flag = False
        break
    s.add(n)
    n = cal(n)
print(flag)